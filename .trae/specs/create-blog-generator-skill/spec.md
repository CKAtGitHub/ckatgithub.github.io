# 博客文章生成智能体 (Blog Generator Skill) Spec

## Why
用户希望基于 `aboutme.md` 中的个人画像（分布式架构、AI Agent、大数据等专家）以及特定的高质量技术文章写作规范（认知缺口、信息流、深度洞见、人格化幽默），创建一个能够自动抓取文章链接、生成符合个人风格的博客文章，并自动提交推送至 Git 的智能体（Trae Skill）。

## What Changes
- 新增 Trae Skill: `blog-generator`
- 在 `.trae/skills/blog-generator/SKILL.md` 中定义智能体的提示词和执行逻辑。
- 规定智能体的工作流：获取链接内容 -> 分析提取 -> 按照四大黄金法则与 CK·黄 个人画像进行文章生成 -> 自动保存到 `_posts/` 目录 -> 执行 Git Commit & Push。

## Impact
- Affected specs: 增加了自动根据链接生成博客文章并发布的 AI 自动化能力。
- Affected code: 新增 `.trae/skills/blog-generator/SKILL.md` 文件。

## ADDED Requirements
### Requirement: 博客文章生成智能体
系统应提供一个名为 `blog-generator` 的专属技能。
#### Scenario: 成功生成并发布博客
- **WHEN** 用户调用该技能并提供一个文章链接。
- **THEN** 智能体会读取链接内容，结合用户画像和四大写作法则生成文章，保存为符合规范的 Jekyll markdown 文件，并自动推送到远程 Git 仓库。
