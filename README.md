# Self-Configuration

<p align="center">
  <img src="https://img.shields.io/badge/Clash-Meta-blue?style=flat-square&logo=clash" alt="Clash">
  <img src="https://img.shields.io/badge/Surge-5-orange?style=flat-square" alt="Surge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
</p>

<p align="center">
  <b>Personal Proxy Tool Configuration Collection</b><br>
  <i>个人代理工具配置文件集合</i>
</p>

<p align="center">
  <a href="#-file-structure">Clash</a> •
  <a href="#-surge-configuration">Surge</a> •
  <a href="#-rule-sources">Rule Sources</a> •
  <a href="#️-notes">Notes</a>
</p>

<p align="center">
  <b>🌐 Language / 语言切换</b><br>
  <a href="README_CN.md">🇨🇳 简体中文</a> | <a href="README.md">🇺🇸 English</a>
</p>

---

## 📁 File Structure

```
Self-Configuration/
├── Clash.yaml      # Clash / Clash Meta configuration
├── Surge.conf      # Surge configuration
├── README.md       # English documentation (default)
└── README_CN.md    # 中文文档
```

---

## 🔷 Clash Configuration

> **Compatible Clients**: Clash, Clash for Windows, Clash Meta, Stash, FlClash

### ⚙️ Basic Settings

| Setting | Value | Description |
|:-------:|:-----:|:-----------:|
| Mixed Port | `7890` | Shared HTTP/SOCKS5 port |
| Controller | `9090` | Web dashboard port |
| Mode | `Rule` | Rule-based mode |
| Allow LAN | `true` | Allow LAN connections |

### 🌐 DNS Configuration

| Type | Server | Provider |
|:----:|:------:|:--------:|
| DoT | `tls://223.5.5.5:853` | Alibaba |
| DoT | `tls://223.6.6.6:853` | Alibaba |
| DoH | `https://doh.pub/dns-query` | DNSPod |
| DoH | `https://dns.alidns.com/dns-query` | Alibaba |

- **Enhanced Mode**: Fake-IP
- **IPv6**: ✅ Enabled

### 🎯 Proxy Groups

#### 🚀 Main Selection Groups

| Group | Type | Description |
|:-----:|:----:|:-----------:|
| 🚀 节点选择 | `select` | Main entry point |
| 🚀 手动切换 | `select` | Manual node selection |
| ♻️ 自动选择 | `url-test` | Auto-select lowest latency |

#### 🌍 Regional Groups

| Group | Filter | Region |
|:-----:|:------:|:------:|
| 🇭🇰 Hong Kong | `港\|HK\|Hong Kong` | Hong Kong |
| 🇯🇵 Japan | `日\|JP\|Japan` | Japan |
| 🇺🇸 United States | `美\|US\|United States` | USA |
| 🇸🇬 Singapore | `新\|SG\|Singapore` | Singapore |
| 🇹🇼 Taiwan | `台\|TW\|Taiwan` | Taiwan |
| 🇰🇷 Korea | `韩\|KR\|Korea` | Korea |
| 🇬🇧 United Kingdom | `英\|UK\|United Kingdom` | UK |
| 🇩🇪 Germany | `德\|DE\|Germany` | Germany |
| 🇫🇷 France | `法\|FR\|France` | France |
| 🌍 Other Regions | Exclude above | Others |

#### 📦 Service Groups

| Group | Default | Purpose |
|:-----:|:-------:|:-------:|
| 🤖 AI服务 | Proxy | ChatGPT, Claude, Gemini |
| 📹 YouTube | Proxy | YouTube videos |
| 🔍 谷歌服务 | Proxy | Google Search, Maps |
| 📧 Google FCM | Proxy | Push notifications |
| ✈️ Telegram | Proxy | Messaging |
| 🍎 Apple服务 | DIRECT | Apple services |
| Ⓜ️ 微软服务 | DIRECT | Microsoft services |
| 🌍 国外媒体 | Proxy | Netflix, Disney+, etc. |
| 🎯 国内流量 | DIRECT | Mainland China sites |
| 🫧 WeChat | DIRECT | WeChat |
| 🚫 广告拦截 | REJECT | Ad blocking |

### 📋 Rule Priority

```
 1. 🚫 Ad Blocking      AdBlock, HTTPDNS → REJECT
 2. ⚡ Special Rules    Special → DIRECT
 3. 🤖 AI Services      AI Suite → Proxy
 4. 🎬 Streaming        Netflix, Disney+, YouTube → Proxy
 5. 📺 CN Media         Bilibili, iQIYI, Youku → DIRECT
 6. 💬 Messaging        Telegram, Discord → Proxy
 7. 🔧 Tech Services    Google, Microsoft, Apple
 8. 💰 Cryptocurrency   Crypto → Proxy
 9. 🎮 Gaming           Steam, miHoYo
10. 🇨🇳 CN Rules        Domestic → DIRECT
11. 🌏 GeoIP CN         China IP → DIRECT
12. 🌐 Final Rule       MATCH → Proxy
```

### 🚀 Usage

1. **Import Configuration**
   - Download `Clash.yaml` and import to your client

2. **Update Subscription URL**
   ```yaml
   proxy-providers:
     all-proxies:
       type: http
       url: "https://your-subscription-url"
       interval: 3600
   ```

3. **Enable and Select Nodes**

---

## 🔶 Surge Configuration

> **Compatible Clients**: Surge for iOS / macOS

### ⚙️ Basic Settings

| Setting | Value | Description |
|:-------:|:-----:|:-----------:|
| HTTP Port | `6152` | Wi-Fi sharing port |
| SOCKS5 Port | `6153` | Wi-Fi sharing port |
| Controller | `6160` | API control port |
| Dashboard | `6166` | Web dashboard port |
| IPv6 | `false` | Disabled by default |

### 🌐 DNS Configuration

| Type | Server | Provider |
|:----:|:------:|:--------:|
| System | `223.5.5.5`, `223.6.6.6`, `119.29.29.29` | China DNS |
| DoH | `https://doh.pub/dns-query` | DNSPod |
| DoH | `https://dns.alidns.com/dns-query` | Alibaba |
| Hijack | `8.8.8.8:53`, `8.8.4.4:53` | Google DNS |

### 🎯 Proxy Groups

#### 🚀 Core Groups

| Group | Type | Description |
|:-----:|:----:|:-----------:|
| NoAuto | `select` | Main entry point |
| Automatic | `select` | Regional selection |
| AllServer | `select` | All subscription nodes |
| Proxy | `select` | Proxy policy |

#### 🌍 Regional Groups (Auto URL-Test)

| Group | Filter | Interval |
|:-----:|:------:|:--------:|
| Hong Kong | `港\|🇭🇰\|香港\|HK\|Hong` | 300s |
| Taiwan | `台\|🇹🇼\|台湾\|TW\|Tai` | 300s |
| Japan | `日\|🇯🇵\|日本\|JP\|Japan` | 300s |
| Singapore | `坡\|🇸🇬\|新加坡\|狮城\|SG` | 300s |
| United States | `美\|🇺🇸\|美国\|US\|States` | 300s |
| United Kingdom | `🇬🇧\|英国\|UK` | 300s |
| Korea | `韩\|韩国\|Korea\|KR\|🇰🇷` | 300s |
| Other | Exclude above | 300s |

#### 📦 Service Groups

| Group | Default | Purpose |
|:-----:|:-------:|:-------:|
| AI | Automatic | ChatGPT, Claude, Gemini, Bing |
| YouTube | Automatic | YouTube videos |
| Netflix | Hong Kong | Netflix streaming |
| Disney+ | Hong Kong | Disney+ streaming |
| TikTok | Taiwan | TikTok unlock |
| Telegram | Automatic | Messaging |
| X | Automatic | Twitter/X |
| Microsoft | Mainland | Microsoft services |
| OneDrive | Mainland | Cloud storage |
| Apple | Mainland | Apple services |
| WeChat | Mainland | WeChat |
| Bilibili | Mainland | Bilibili (HK/TW unlock) |
| Speedtest | Mainland | Speed test |

### 📋 Rule Priority

```
 1. 🔧 Unbreak Rules    Fix broken connections → DIRECT
 2. ✏️ Manual Rules     Custom domains/processes
 3. 🚫 Ad Blocking      SKK Ruleset → REJECT
 4. 🔒 Privacy          Block trackers
 5. 📱 CN Apps          WeChat, NetEase, Bilibili, Weibo
 6. 🍎 Apple Services   App Store, Apple News, Apple TV
 7. 🤖 AI Services      OpenAI, Claude, Gemini, Bing
 8. 🎬 Streaming        Disney+, Netflix, TikTok, YouTube
 9. 🌏 Regional Unlock  US, EU, JP, KR, HK, TW streams
10. 💬 Social Media     Twitter, Telegram, Facebook, Instagram
11. 🔧 Other Global     OneDrive, Microsoft, GitHub, Speedtest
12. 🇨🇳 CN Rules        SKK + ChinaMax ruleset
13. 🌐 Global Rules     CDN, Global ruleset
14. 🏠 LAN              Local network → DIRECT
15. 🎯 Final Rule       FINAL → NoAuto
```

### ✨ Special Features

#### 🔄 URL Rewrite

| Original | Target | Type |
|:--------:|:------:|:----:|
| `google.cn` | `google.com` | 302 Redirect |
| `maps.google.cn` | `maps.google.com` | 302 Redirect |
| `taobao.com` | HTTPS | Force upgrade |
| `jd.com` | HTTPS | Force upgrade |

#### 🏠 Host Mapping

| Service | DNS Server | Description |
|:-------:|:----------:|:-----------:|
| Taobao/Tmall/Alipay | `223.5.5.5` | Alibaba services |
| JD/QQ/WeChat | `119.28.28.28` | Tencent services |
| Bilibili/NetEase | `119.29.29.29` | Entertainment |
| Router Admin | System DNS | Local devices |

### 🚀 Usage

1. **Import Configuration**
   - Download `Surge.conf` and import to Surge

2. **Update Subscription URL**
   ```
   AllServer = select, ..., policy-path=https://your-subscription-url
   ```

3. **Configure MITM Certificate** (required for URL rewrite)
   - Install and trust the certificate

4. **Enable Configuration**

---

## 📚 Rule Sources

| Source | Description |
|:------:|:-----------:|
| [dler-io/Rules](https://github.com/dler-io/Rules) | Main Clash ruleset |
| [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | Cross-platform rules |
| [SukkaW/Surge](https://github.com/SukkaW/Surge) | SKK ruleset (ruleset.skk.moe) |
| [VirgilClyne/GetSomeFries](https://github.com/VirgilClyne/GetSomeFries) | ASN rules |
| [Semporia/TikTok-Unlock](https://github.com/Semporia/TikTok-Unlock) | TikTok unlock rules |

---

## ⚠️ Notes

| Item | Description |
|:----:|:-----------:|
| 🔗 Subscription | Must replace with your own subscription URL |
| 🔄 Rule Update | Rules auto-update every 7 days |
| ⏱️ Speed Test | 300s interval, 3s timeout |
| 🔐 MITM Cert | Required for Surge URL rewrite |
| 🔍 Node Filter | Auto-filter nodes with "traffic/reset/expire" keywords |

---

<p align="center">
  <sub>Made with ❤️ for better internet experience</sub>
</p>

## 📄 License

MIT
