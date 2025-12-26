import yaml
import copy
import os
import sys

# 配置文件名称
USER_CONFIG_FILE = 'user_config.yaml'

# 默认过滤关键词（作为备份，如果配置文件里没写）
DEFAULT_FILTER_KEYWORDS = ['剩余', '到期', '套餐', '官网', 'Traffic', 'Expire', 'Reset']

def load_yaml(filepath):
    """安全读取 YAML 文件"""
    if not os.path.exists(filepath):
        print(f"[!] 找不到文件: {filepath}")
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"[!] 读取文件 {filepath} 失败: {e}")
        return None

def save_yaml(filepath, data):
    """保存 YAML 文件"""
    try:
        # 自定义 PyYAML 格式，增加可读性
        class MyDumper(yaml.Dumper):
            def increase_indent(self, flow=False, indentless=False):
                return super(MyDumper, self).increase_indent(flow, False)

        with open(filepath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, Dumper=MyDumper, allow_unicode=True, default_flow_style=False, sort_keys=False)
        print(f"[√] 成功! 文件已生成: {filepath}")
    except Exception as e:
        print(f"[!] 写入文件出错: {e}")

def get_smart_filter_regex(original_filter, exclude_keywords):
    """
    构造智能过滤正则
    逻辑: (忽略大小写) + (必须不包含排除词) + (必须匹配原有规则)
    """
    # 构造排除部分: (?!.*(词1|词2|词3))
    # 使用 re.escape 并不是完全必要，因为关键词通常是简单文本，但在严谨代码中推荐，
    # 不过 Clash 的正则引擎可能不支持过度转义，这里直接拼接
    exclude_pattern = "|".join(exclude_keywords)
    
    # 核心逻辑：
    # (?i) : 忽略大小写
    # ^ : 匹配开头
    # (?!.*(A|B|C)) : 负向先行断言，确保整行不包含 A 或 B 或 C
    # .* : 匹配剩余字符
    
    smart_prefix = f"(?i)^(?!.*({exclude_pattern}))"
    
    if original_filter:
        # 如果原来有规则 (比如 "HK|Hong Kong")
        # 新规则: (?i)^(?!.*(排除词)).*(?:原规则)
        # 注意: (?:...) 是非捕获组，用于包裹原规则以防优先级问题
        return f"{smart_prefix}.*(?:{original_filter})"
    else:
        # 如果原来没有规则 (比如手动选择组)
        # 新规则: (?i)^(?!.*(排除词)).*$
        return f"{smart_prefix}.*$"

def generate_config():
    print(f"[-] 正在读取用户配置: {USER_CONFIG_FILE}...")
    user_config = load_yaml(USER_CONFIG_FILE)
    
    if not user_config:
        print(f"[!] 无法读取 {USER_CONFIG_FILE}，请确保文件存在。")
        # 创建一个简单的默认配置提示
        print(f"    提示: 你可以手动创建一个 {USER_CONFIG_FILE} 文件。")
        return

    # 获取配置项
    template_file = user_config.get('files', {}).get('template', 'template.yaml')
    output_file = user_config.get('files', {}).get('output', 'final_clash_config.yaml')
    subscriptions = user_config.get('subscriptions', [])
    source_files = user_config.get('local_source_files', [])
    filter_keywords = user_config.get('filter_keywords', DEFAULT_FILTER_KEYWORDS)

    print(f"[-] 正在读取模板文件: {template_file}...")
    template_config = load_yaml(template_file)
    if not template_config:
        return

    # 初始化容器
    if 'proxies' not in template_config or template_config['proxies'] is None:
        template_config['proxies'] = []
    if 'proxy-providers' not in template_config or template_config['proxy-providers'] is None:
        template_config['proxy-providers'] = {}

    all_node_names = []
    all_provider_names = []

    # --- 1. 处理订阅链接 ---
    if subscriptions:
        print(f"[-] 正在处理 {len(subscriptions)} 个订阅链接...")
        provider_template = {
            'type': 'http',
            'interval': 3600,
            'health-check': {'enable': True, 'interval': 600, 'url': 'http://www.gstatic.com/generate_204'},
            'path': './providers/default.yaml'
        }
        
        for sub in subscriptions:
            p_name = sub.get('name', 'Airport')
            p_url = sub.get('url', '')
            if not p_url: continue
            
            new_provider = copy.deepcopy(provider_template)
            new_provider['url'] = p_url
            new_provider['path'] = f"./providers/{p_name}.yaml"
            
            template_config['proxy-providers'][p_name] = new_provider
            all_provider_names.append(p_name)

    # --- 2. 处理本地源文件 ---
    for src_file in source_files:
        if not os.path.exists(src_file):
            # 只有当用户真的填了文件但找不到时才提示
            if src_file != 'my_old_config.yaml': 
                print(f"[!] 跳过不存在的文件: {src_file}")
            continue
            
        print(f"[-] 正在读取本地文件: {src_file}")
        src_data = load_yaml(src_file)
        if not src_data: continue

        # 提取自建节点
        if 'proxies' in src_data and src_data['proxies']:
            count = 0
            for node in src_data['proxies']:
                if not any(n['name'] == node['name'] for n in template_config['proxies']):
                    template_config['proxies'].append(node)
                    all_node_names.append(node['name'])
                    count += 1
            print(f"    > 提取了 {count} 个节点")
        
        # 提取已有订阅
        if 'proxy-providers' in src_data and src_data['proxy-providers']:
            for p_name, p_config in src_data['proxy-providers'].items():
                if p_name not in template_config['proxy-providers']:
                    template_config['proxy-providers'][p_name] = p_config
                    all_provider_names.append(p_name)

    # --- 3. 更新策略组 & 智能过滤 ---
    print("[-] 正在更新策略组并注入智能过滤规则...")
    
    # 定义需要注入内容的组（核心组）
    target_groups_nodes = ['🚀 节点选择', '🚀 手动切换', '♻️ 自动选择', '🌐 国际流量', '🌍 国外媒体']
    
    if 'proxy-groups' in template_config:
        for group in template_config['proxy-groups']:
            group_name = group['name']

            # (A) 注入自建节点
            if group_name in target_groups_nodes:
                if 'proxies' not in group or group['proxies'] is None:
                    group['proxies'] = []
                for node_name in all_node_names:
                    if node_name not in group['proxies']:
                        group['proxies'].append(node_name)

            # (B) 注入订阅源 (逻辑: 所有使用了use的组 + 核心组)
            has_use = 'use' in group and group['use']
            is_target = group_name in target_groups_nodes
            
            if has_use or is_target:
                if 'use' not in group or group['use'] is None:
                    group['use'] = []
                for p_name in all_provider_names:
                    if p_name not in group['use']:
                        group['use'].append(p_name)

            # (C) ★★★ 智能过滤非节点信息 ★★★
            # 无论是否是核心组，都加上过滤逻辑，防止垃圾信息进入列表
            # 获取当前组已有的 filter
            original_filter = group.get('filter', '')
            
            # 生成新的组合正则
            new_filter = get_smart_filter_regex(original_filter, filter_keywords)
            
            # 更新 filter 字段
            group['filter'] = new_filter
            
            # 调试输出 (可选)
            # print(f"    > 组 [{group_name}] 更新过滤规则.")

    # --- 4. 保存 ---
    save_yaml(output_file, template_config)

if __name__ == '__main__':
    generate_config()