---
layout: post
title: "深度解析 Claude Code：顶级 AI Agent 的 Prompt / Context / Harness 设计哲学"
subtitle: "从源码实现看大模型应用的工程化进阶，别再只盯着提示词了"
date: 2026-04-28 10:00:00 +0800
tags: [AI Agent, 大模型, 架构设计, Claude Code]
comments: true
---

<!-- 终端风格引言块：用于开篇制造认知缺口，吸引读者注意力 -->
<div style="background-color: #1e1e1e; color: #00ff00; font-family: 'Courier New', Courier, monospace; border-radius: 8px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); margin-bottom: 30px; margin-top: 20px; position: relative; overflow: hidden;">
    <div style="display: flex; align-items: center; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid #333;">
        <div style="display: flex; gap: 8px; margin-right: 15px;">
            <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #ff5f56;"></div>
            <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #ffbd2e;"></div>
            <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #27c93f;"></div>
        </div>
        <div style="color: #ccc; font-size: 0.9em;">bash</div>
    </div>
    <div>
        <p style="margin: 5px 0; line-height: 1.6;"><span style="color: #008AFF; font-weight: bold;">ckhuang@macbookpro:~$</span> 很多开发者在构建 Agent 时都有个错觉：写个几百字的 System Prompt，就以为大功告成了。结果一上生产，模型动不动就“失忆”、胡编乱造，甚至一通乱操作把库给删了。为什么？因为你只是在教它“怎么做”，却忘了给它“戴上缰绳”。读完这篇文章，带你从 Claude Code 的底层设计，揭秘如何构建一个能干脏活累活的 95 分生产级 Agent。 <span style="display: inline-block; width: 8px; height: 16px; background-color: #00ff00; vertical-align: middle;"></span></p>
    </div>
</div>

在日常使用 Claude Code 时，它处理复杂长程任务的稳定性常令人直呼“Amazing”。剖析其背后的原理，你会发现，除了 Claude 3.7 (Opus 4.6) 基座模型本身的强大，真正让它脱颖而出的是极致的工程化设计。

要构建一个靠谱的 Agent，仅靠 Prompt 是不够的。现代 AI 系统的设计必须经历三大关键阶段：**Prompt Engineering（如何说） -> Context Engineering（看什么） -> Harness Engineering（运行环境）**。

### 1. Prompt Engineering：从静态文本到动态积木组装

很多人对“提示词工程”的理解还停留在“写一段漂亮的话”。但在真实的业务场景中，Prompt 是一套**复杂的、动态的组装机制**。

Claude Code 的 System Prompt 构建过程就像搭积木，包含以下核心模块：
- **静态部分**：明确身份人设、系统行为规则、任务执行指南（比如警告它不要随便重构代码）、操作安全守则（高危操作必须确认）、工具使用规范以及输出风格。
- **动态部分**：根据不同的用户会话，实时注入会话指导、记忆片段、MCP 服务器指令、当前环境信息等。

**深度洞见：**
为什么要这么麻烦？因为不同的上下文和任务需要不同的约束。如果你的 Agent 在执行简单查询和执行危险代码修改时用的是同一个 Prompt，那出事只是时间问题。这种“静态基座+动态插件”的组装模式，是构建灵活 Agent 的第一步。

### 2. Context Engineering：打破 Token 爆炸的魔咒

随着对话的深入，工具调用的海量输出会迅速撑爆上下文窗口，导致模型“变傻”。Claude Code 提供了一套堪称教科书级别的三层渐进式压缩体系：

1. **MicroCompact（微压缩）**：纯规则驱动，针对 `Grep`、`Glob` 等容易产生大量无用输出的工具，基于时间和缓存边界直接截断。
2. **Session Memory Compact（会话记忆压缩）**：当 Token 数逼近危险水位时，直接复用已有的会话摘要，替换掉冗长的历史记录，零 LLM 推理成本。
3. **Full LLM Compact（完全压缩）**：如果前两招不管用，则调用 LLM 严格按照 9 段式结构化模板（问题、关键概念、代码文件等）进行全量压缩。这里还有一个巧妙的设计：在 Prompt 中强制模型在 `<analysis>` 标签内进行思考，且严厉禁止在压缩过程中调用任何工具（防止产生副作用）。

此外，Claude Code 还引入了 **Memdir 结构化记忆系统**，将记忆分为 User、Feedback、Project 和 Reference 四类，并让大模型充当“图书管理员”进行语义检索。这就让它从一个“一次性工具”进化成了有持续学习能力的编码伙伴。

<!-- 金句/洞见引用块：用于突出核心技术洞见和观点 -->
<div style="text-align: center; font-size: 1.2em; font-style: italic; color: #008AFF; margin: 40px 0 20px; padding: 20px; border-top: 1px dashed #ccc; border-bottom: 1px dashed #ccc;">
    “真正的 Agent 工程不是把模型当神供着，而是把它当成员工管着——用精细的流程约束它的随性，用系统的脚手架放大它的才华。” —— CK·黄
</div>

### 3. Harness Engineering：给野马套上马具

大模型就像一匹千里马，跑得快但容易失控。Harness Engineering（驾驭工程）就是为它套上马具，确保它在复杂的开发环境中不搞破坏。

#### 系统级强提醒 (`<system-reminder>`)
如何防止模型混淆“系统指令”和“用户输入”？Claude Code 会将配置文件、日期、工具结果等元信息，统一包裹在 `<system-reminder>` 标签中。这等于明确告诉模型：“这是不可反驳的系统客观事实，不是用户的聊天记录”，极大降低了幻觉风险。

#### 六大系统内置 Agent 的精细分工
你以为在和单一的 Claude 交流？其实背后是一个团队在运作：
- **Explore Agent（侦察兵）**：遇到大工程，先派个速度快、只读的小模型去摸底，防止污染主上下文。
- **Verification Agent（质量检验官）**：这是设计最精彩的一环！它的核心设定是“红蓝对抗”——它的工作不是确认代码能跑，而是想尽办法把代码搞崩。它甚至自带了一套反偷懒话术，专门对付那些“看起来是对的”、“大概没问题”的 AI 常见甩锅说辞。

#### 异步生成器与钩子机制
Claude Code 将主循环重构为异步生成器 (`async function*`)，实现了流式处理、协作式控制和优雅的取消机制。同时，它开放了 20 多种生命周期钩子（Hooks），允许开发者在工具调用前后注入自定义逻辑，比如阻断高危操作或清洗敏感数据。

### 4. 写在最后：技术人的幽默与温度

有趣的是，在如此严谨的架构之下，Anthropic 的工程师们还埋了不少彩蛋：
- 怕你等太久电脑休眠，它会悄悄调用 `caffeinate` 命令给 macOS 灌咖啡。
- 为了防止被竞争对手“蒸馏”，它会在 API 请求里注入假工具定义去“投毒”。
- 甚至，你还能在命令行里孵化专属的“电子宠物”（比如一只头顶螺旋桨的稀有企鹅），宠物属性完全由你的 UserID 决定，不能作弊刷初始。

<!-- 终端风格结论块：用于硬核总结，强化读者印象 -->
<div style="background-color: #1e1e1e; color: #00ff00; font-family: 'Courier New', Courier, monospace; border-radius: 8px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); margin-bottom: 30px; margin-top: 20px; position: relative; overflow: hidden;">
    <div style="display: flex; align-items: center; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid #333;">
        <div style="display: flex; gap: 8px; margin-right: 15px;">
            <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #ff5f56;"></div>
            <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #ffbd2e;"></div>
            <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #27c93f;"></div>
        </div>
        <div style="color: #ccc; font-size: 0.9em;">bash</div>
    </div>
    <div>
        <p style="margin: 5px 0; line-height: 1.6;"><span style="color: #008AFF; font-weight: bold;">ckhuang@macbookpro:~$</span> 总结一下，构建生产级 Agent 的密码在于：用 Prompt 筑基，用 Context 控场，用 Harness 托底。在这个 AI 技术狂飙的时代，不沉溺于单点突破，掌握全局工程架构的设计思维，才是我们驾驭 AI、而不是被 AI 取代的关键所在。 <span style="display: inline-block; width: 8px; height: 16px; background-color: #00ff00; vertical-align: middle;"></span></p>
    </div>
</div>
