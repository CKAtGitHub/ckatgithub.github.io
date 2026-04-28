---
layout: post
title: "Anthropic推出面向Claude Code的基于智能体的代码审查功能"
tags: [AI, InfoQ, 人工智能]
comments: true
author: "Daniel Dominguez"
---

Anthropic为[Claude Code](https://claude.com/product/claude-code)推出了新的[Code Review](https://claude.com/blog/code-review)功能，新增了一个基于智能体的拉取请求（pull request）审查系统，可由多个AI审查器协同分析代码变更。该功能目前以研究预览形式向Team和Enterprise用户开放。

该系统会在拉取请求创建后自动运行，并调度多个智能体并行检查变更。Anthropic表示，这些智能体会查找潜在的缺陷，并验证其发现以降低误报，按严重程度对问题排序，随后在拉取请求中发布汇总审查意见和行内评论。

Anthropic称，分配的智能体数量会随拉取请求规模和复杂度动态调整。规模更大或更复杂的变更会得到更深入的分析，而小型变更则采用更轻量的审查流程。该公司表示平均审查时间约为20分钟。

Anthropic表示，其内部已经在过去数月中将该系统应用于大多数自有拉取请求。[据该公司声称](https://claude.com/blog/code-review#:~:text=Code%20Review%20in%20action)，采用该系统后，包含实质性审查意见的拉取请求比例从16%提升至54%。在变更超过1000行的拉取请求中，84%发现了问题，平均识别出了7.5个问题；而在少于50行的拉取请求中，31%发现了问题，平均为0.5个问题。

Anthropic表示，在内部使用过程中，被工程师标记为错误的发现不到1%。公司强调，该工具旨在辅助而非替代人工审查者，并且不会自动批准拉取请求。

针对Anthropic发布Code Review的消息，[社区反应](https://x.com/claudeai/status/2031088176773976474)整体较为积极。开发者认为，该公司宣称的分析深度与多智能体方案，是与轻量级AI审查工具的关键差异。也有评论者指出，定价可能会限制中小团队采用；另一些人则质疑其宣称的单次审查约20分钟、每个拉取请求成本15–25美元，是否适用于高吞吐的工程流程。

AI研究员[Nir Zabari](https://x.com/nirzabari/status/2031108999337148864)评论说：

> 表面上听起来不错，但它并没有披露任何技术细节（例如每个并行的智能体具体关注什么），也没有解释除了成本15–25美元之外，它为何优于其他工具（按当前Opus定价，大致可理解为约300万Token）。换句话说，这类功能值得开源……

与此同时，用户[@rohini](https://x.com/rohinidr/status/2031235896692060576)发帖称：

> Claude在写代码，同时又由Claude来审代码？这甚至达不到最基本的安全标准。

这一发布让Anthropic更直接地进入AI代码审查市场。目前该市场中，像[GitHub的Copilot代码审查](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review)功能以及[CodeRabbit](https://www.coderabbit.ai/)等工具，已经提供自动化拉取请求分析能力。Anthropic的差异化点在于其多智能体审查架构，以及强调更深入、相对更慢的分析流程，而非轻量化快速审查。

查看英文原文：[Anthropic Introduces Agent-Based Code Review for Claude Code](https://www.infoq.com/news/2026/04/claude-code-review/)



> *本文由 AI 助手自动生成并排版自 InfoQ，原文链接：[Anthropic推出面向Claude Code的基于智能体的代码审查功能](https://www.infoq.cn/article/QyeZg05iakideMTGCQKi)*
