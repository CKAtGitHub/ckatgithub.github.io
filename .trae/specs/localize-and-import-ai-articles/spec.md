# 博客中文化与 AI 文章导入 Spec

## Why
将个人博客全面中文化，提升中文读者的阅读体验。同时清理旧文章，引入 InfoQ 最新的 AI 方向热门文章作为新的内容基础，并清理无效链接，添加友情链接，使博客内容更加聚焦于新潮技术分享。

## What Changes
- **配置文件修改**：修改 `_config.yml`，设置语言为中文，翻译导航栏等可见文本。
- **链接清理与添加**：清理无效和不相关的链接（如社交链接中的默认占位符），在导航栏或专门页面增加“友情链接”：森林有鱼 (`https://iyouyu.tech/`)、有鱼智界 (`https://zhijie.iyouyu.tech/`)。
- **内容重置**：**BREAKING** 删除 `_posts/` 目录下的所有现有文章。
- **内容导入**：从 InfoQ 获取最新的 AI 方向前 20 篇热门文章，按博客风格总结并生成 Markdown 文件存入 `_posts/`。

## Impact
- Affected specs: 博客界面语言、导航栏结构、文章内容。
- Affected code: `_config.yml`, `_posts/*`。

## ADDED Requirements
### Requirement: 友情链接展示
系统应在导航栏中展示友情链接菜单，包含指定的两个外部网站链接。

### Requirement: AI 文章自动总结
系统应能获取 InfoQ 的 AI 热门文章并自动生成符合 Jekyll 格式的 Markdown 文章。

## MODIFIED Requirements
### Requirement: 界面中文化
所有的导航、提示信息应显示为中文。

## REMOVED Requirements
### Requirement: 旧有文章与占位链接
**Reason**: 重构博客定位为新潮技术分享，旧内容和无关占位链接不再需要。
**Migration**: 直接删除，无需迁移。
