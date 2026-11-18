# rift-rules

Rift（Android 代理客户端）的规则数据仓：每天用 GitHub Actions 编译一次，
产物放在 `srs` 分支根目录，供 Rift 的“路由资源更新”直接下载。

## 产物（`srs` 分支）

| 文件 | 内容 |
|---|---|
| `geosite-cn.srs` | 合并表：MetaCubeX cn ∪ SagerNet cn ∪ 自有补充（`sources/cn-extra.txt`） |
| `geoip-cn.srs` | 镜像 Loyalsoldier `release/srs/cn.srs` |
| `geosite-category-ads-all.srs` | 镜像 SagerNet 现用文件 |

合并表只做并集、不做剪枝：两家全保留、零回归。文件约 460 KB，
sing-box 1.15 可直接读取（SRS v2）。

## 数据来源与致谢

- [MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat)（cn 域名表）
- [SagerNet/sing-geosite](https://github.com/SagerNet/sing-geosite)（cn 域名表、ads 表）
- [Loyalsoldier/geoip](https://github.com/Loyalsoldier/geoip)（CN IP 段，数据来自高依凡）
- [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community) 与
  [felixonmars/dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)
  （上游数据源）

编译用官方 sing-box 二进制，版本钉死在 `v1.15.0-alpha.13`（与 Rift 核心一致）。

## 补充域名

想加域名：往 `sources/cn-extra.txt` 里加一行（`#` 注释），下次定时运行即进表。
只加实测需要的，不要批量抄。

## 说明

本仓只有公开的规则数据与编译脚本，没有任何用户隐私。
工作流见 `.github/workflows/build-rules.yml`；任一验证关卡失败即不提交，
旧文件保留。
