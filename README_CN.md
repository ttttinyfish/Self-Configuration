# Self-Configuration

<p align="center">
  <img src="https://img.shields.io/badge/Clash-Meta-blue?style=flat-square&logo=clash" alt="Clash">
  <img src="https://img.shields.io/badge/Surge-5-orange?style=flat-square" alt="Surge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
</p>

<p align="center">
  <b>个人代理工具配置文件集合</b><br>
  <i>Personal proxy tool configuration collection</i>
</p>

<p align="center">
  <a href="#-文件结构">Clash</a> •
  <a href="#-surge-配置">Surge</a> •
  <a href="#-规则来源">规则来源</a> •
  <a href="#️-注意事项">注意事项</a>
</p>

<p align="center">
  <b>🌐 Language / 语言切换</b><br>
  <a href="README_CN.md">🇨🇳 简体中文</a> | <a href="README.md">🇺🇸 English</a>
</p>

---

## 📁 文件结构

```
Self-Configuration/
├── Clash.yaml      # Clash / Clash Meta 配置文件
├── Surge.conf      # Surge 配置文件
├── README.md       # English documentation (default)
└── README_CN.md    # 中文文档
```

---

## 🔷 Clash 配置

> **适用客户端**: Clash, Clash for Windows, Clash Meta, Stash, FlClash

### ⚙️ 基础设置

| 配置项 | 值 | 说明 |
|:------:|:--:|:----:|
| 混合端口 | `7890` | HTTP/SOCKS5 共用端口 |
| 控制端口 | `9090` | Web 面板控制端口 |
| 运行模式 | `Rule` | 规则模式 |
| 局域网访问 | `true` | 允许其他设备连接 |

### 🌐 DNS 配置

| 类型 | 服务器 | 提供商 |
|:----:|:------:|:------:|
| DoT | `tls://223.5.5.5:853` | 阿里云 |
| DoT | `tls://223.6.6.6:853` | 阿里云 |
| DoH | `https://doh.pub/dns-query` | DNSPod |
| DoH | `https://dns.alidns.com/dns-query` | 阿里云 |

- **增强模式**: Fake-IP
- **IPv6**: ✅ 已启用

### 🎯 策略组

#### 🚀 主选择组

| 策略组 | 类型 | 说明 |
|:------:|:----:|:----:|
| 🚀 节点选择 | `select` | 主入口，手动选择策略 |
| 🚀 手动切换 | `select` | 手动选择具体节点 |
| ♻️ 自动选择 | `url-test` | 延迟最低自动切换 |

#### 🌍 地区节点组

| 策略组 | 筛选规则 | 地区 |
|:------:|:--------:|:----:|
| 🇭🇰 Hong Kong | `港\|HK\|Hong Kong` | 香港 |
| 🇯🇵 Japan | `日\|JP\|Japan` | 日本 |
| 🇺🇸 United States | `美\|US\|United States` | 美国 |
| 🇸🇬 Singapore | `新\|SG\|Singapore` | 新加坡 |
| 🇹🇼 Taiwan | `台\|TW\|Taiwan` | 台湾 |
| 🇰🇷 Korea | `韩\|KR\|Korea` | 韩国 |
| 🇬🇧 United Kingdom | `英\|UK\|United Kingdom` | 英国 |
| 🇩🇪 Germany | `德\|DE\|Germany` | 德国 |
| 🇫🇷 France | `法\|FR\|France` | 法国 |
| 🌍 Other Regions | 排除以上地区 | 其他 |

#### 📦 服务分流组

| 策略组 | 默认策略 | 用途 |
|:------:|:--------:|:----:|
| 🤖 AI服务 | 代理 | ChatGPT, Claude, Gemini |
| 📹 YouTube | 代理 | YouTube 视频 |
| 🔍 谷歌服务 | 代理 | Google 搜索、地图 |
| 📧 Google FCM | 代理 | Google 推送服务 |
| ✈️ Telegram | 代理 | Telegram 通讯 |
| 🍎 Apple服务 | 直连 | Apple 相关服务 |
| Ⓜ️ 微软服务 | 直连 | Microsoft 服务 |
| 🌍 国外媒体 | 代理 | Netflix, Disney+ 等 |
| 🎯 国内流量 | 直连 | 国内网站 |
| 🫧 WeChat | 直连 | 微信 |
| 🚫 广告拦截 | 拒绝 | 广告过滤 |

### 📋 分流规则优先级

```
 1. 🚫 广告拦截     AdBlock, HTTPDNS → 拒绝
 2. ⚡ 特殊规则     Special → 直连
 3. 🤖 AI 服务     AI Suite → 代理
 4. 🎬 国际流媒体   Netflix, Disney+, YouTube → 代理
 5. 📺 国内媒体     Bilibili, 爱奇艺, 优酷 → 直连
 6. 💬 通讯工具     Telegram, Discord → 代理
 7. 🔧 科技服务     Google, Microsoft, Apple
 8. 💰 加密货币     Crypto → 代理
 9. 🎮 游戏服务     Steam, miHoYo
10. 🇨🇳 国内规则    Domestic → 直连
11. 🌏 GeoIP CN    中国 IP → 直连
12. 🌐 兜底规则     MATCH → 代理
```

### 🚀 使用方法

1. **导入配置**
   - 下载 `Clash.yaml` 导入客户端

2. **修改订阅地址**
   ```yaml
   proxy-providers:
     all-proxies:
       type: http
       url: "https://你的订阅地址"
       interval: 3600
   ```

3. **启用配置并选择节点**

---

## 🔶 Surge 配置

> **适用客户端**: Surge for iOS / macOS

### ⚙️ 基础设置

| 配置项 | 值 | 说明 |
|:------:|:--:|:----:|
| HTTP 端口 | `6152` | Wi-Fi 共享端口 |
| SOCKS5 端口 | `6153` | Wi-Fi 共享端口 |
| 外部控制 | `6160` | API 控制端口 |
| Web 面板 | `6166` | Dashboard 端口 |
| IPv6 | `false` | 默认关闭 |

### 🌐 DNS 配置

| 类型 | 服务器 | 提供商 |
|:----:|:------:|:------:|
| 系统 DNS | `223.5.5.5`, `223.6.6.6`, `119.29.29.29` | 国内 DNS |
| DoH | `https://doh.pub/dns-query` | DNSPod |
| DoH | `https://dns.alidns.com/dns-query` | 阿里云 |
| DNS 劫持 | `8.8.8.8:53`, `8.8.4.4:53` | Google DNS |

### 🎯 策略组

#### 🚀 核心策略组

| 策略组 | 类型 | 说明 |
|:------:|:----:|:----:|
| NoAuto | `select` | 主选择入口 |
| Automatic | `select` | 地区策略选择 |
| AllServer | `select` | 所有订阅节点 |
| Proxy | `select` | 代理策略 |

#### 🌍 地区节点组 (自动测速)

| 策略组 | 筛选规则 | 测试间隔 |
|:------:|:--------:|:--------:|
| Hong Kong | `港\|🇭🇰\|香港\|HK\|Hong` | 300s |
| Taiwan | `台\|🇹🇼\|台湾\|TW\|Tai` | 300s |
| Japan | `日\|🇯🇵\|日本\|JP\|Japan` | 300s |
| Singapore | `坡\|🇸🇬\|新加坡\|狮城\|SG` | 300s |
| United States | `美\|🇺🇸\|美国\|US\|States` | 300s |
| United Kingdom | `🇬🇧\|英国\|UK` | 300s |
| Korea | `韩\|韩国\|Korea\|KR\|🇰🇷` | 300s |
| Other | 排除以上地区 | 300s |

#### 📦 服务策略组

| 策略组 | 默认策略 | 用途 |
|:------:|:--------:|:----:|
| AI | Automatic | ChatGPT, Claude, Gemini, Bing |
| YouTube | Automatic | YouTube 视频 |
| Netflix | Hong Kong | Netflix 流媒体 |
| Disney+ | Hong Kong | Disney+ 流媒体 |
| TikTok | Taiwan | TikTok 解锁 |
| Telegram | Automatic | Telegram 通讯 |
| X | Automatic | Twitter/X |
| Microsoft | Mainland | 微软服务 |
| OneDrive | Mainland | OneDrive 云盘 |
| Apple | Mainland | Apple 服务 |
| WeChat | Mainland | 微信 |
| Bilibili | Mainland | B站 (支持港澳台解锁) |
| Speedtest | Mainland | 测速工具 |

### 📋 分流规则优先级

```
 1. 🔧 规则修正     Unbreak → 直连
 2. ✏️ 手动规则     自定义域名/进程
 3. 🚫 广告拦截     SKK 规则集 → 拒绝
 4. 🔒 隐私保护     拦截追踪域名
 5. 📱 国内应用     微信, 网易云, B站, 微博, 小红书
 6. 🍎 Apple 服务   App Store, Apple News, Apple TV
 7. 🤖 AI 服务      OpenAI, Claude, Gemini, Bing
 8. 🎬 国际流媒体   Disney+, Netflix, TikTok, YouTube
 9. 🌏 地区解锁     美区, 欧区, 日区, 韩区, 港区, 台区
10. 💬 国际社交     Twitter, Telegram, Facebook, Instagram
11. 🔧 其他国际     OneDrive, Microsoft, GitHub, Speedtest
12. 🇨🇳 国内规则    SKK + ChinaMax 规则集
13. 🌐 国际规则     CDN, Global 规则集
14. 🏠 本地网络     LAN → 直连
15. 🎯 兜底规则     FINAL → NoAuto
```

### ✨ 特色功能

#### 🔄 URL 重写

| 原地址 | 目标地址 | 类型 |
|:------:|:--------:|:----:|
| `google.cn` | `google.com` | 302 重定向 |
| `maps.google.cn` | `maps.google.com` | 302 重定向 |
| `taobao.com` | HTTPS | 强制升级 |
| `jd.com` | HTTPS | 强制升级 |

#### 🏠 Host 映射

| 服务 | DNS 服务器 | 说明 |
|:----:|:----------:|:----:|
| 淘宝/天猫/支付宝 | `223.5.5.5` | 阿里系服务 |
| 京东/QQ/微信 | `119.28.28.28` | 腾讯系服务 |
| B站/网易 | `119.29.29.29` | 娱乐服务 |
| 路由器管理 | 系统 DNS | 本地设备 |

### 🚀 使用方法

1. **导入配置**
   - 下载 `Surge.conf` 导入 Surge

2. **修改订阅地址**
   ```
   AllServer = select, ..., policy-path=https://你的订阅地址
   ```

3. **配置 MITM 证书**（如需 URL 重写功能）
   - 安装并信任证书

4. **启用配置**

---

## 📚 规则来源

| 来源 | 说明 |
|:----:|:----:|
| [dler-io/Rules](https://github.com/dler-io/Rules) | Clash 主要规则集 |
| [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | 全平台规则集 |
| [SukkaW/Surge](https://github.com/SukkaW/Surge) | SKK 规则集 (ruleset.skk.moe) |
| [VirgilClyne/GetSomeFries](https://github.com/VirgilClyne/GetSomeFries) | ASN 规则 |
| [Semporia/TikTok-Unlock](https://github.com/Semporia/TikTok-Unlock) | TikTok 解锁规则 |

---

## ⚠️ 注意事项

| 项目 | 说明 |
|:----:|:----:|
| 🔗 订阅地址 | 使用前必须替换为自己的订阅地址 |
| 🔄 规则更新 | 规则集自动更新周期为 7 天 |
| ⏱️ 节点测速 | 自动测速间隔 300 秒，超时 3 秒 |
| 🔐 MITM 证书 | Surge 的 URL 重写功能需要安装证书 |
| 🔍 节点过滤 | 自动过滤包含"流量/重置/到期"等关键词 |

---

<p align="center">
  <sub>Made with ❤️ for better internet experience</sub>
</p>

## 📄 License

MIT
