---
layout: page
title: 关于作者
subtitle: 分布式架构专家 / 终身学习者
permalink: /aboutme/
---

<!-- 引入 ECharts 用于渲染雷达图 -->
<script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
<!-- 引入 Mermaid 用于渲染技能脑图 -->
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
  // 初始化 Mermaid 配置，设置主题为 base 并自定义颜色以匹配页面风格
  document.addEventListener("DOMContentLoaded", function() {
    mermaid.initialize({ 
        startOnLoad: true, 
        theme: 'base', 
        themeVariables: { 
            primaryColor: '#f8f9fa', 
            primaryTextColor: '#333', 
            primaryBorderColor: '#008AFF', 
            lineType: 'curve' 
        } 
    });
  });
</script>

<style>
/* ==========================================
   终端风格自我介绍容器样式
   ========================================== */
.terminal-window {
    background-color: #1e1e1e;
    color: #00ff00;
    font-family: 'Courier New', Courier, monospace;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
}
/* 终端顶部标题栏 */
.terminal-header {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 1px solid #333;
}
/* 终端左上角的红黄绿控制按钮 */
.terminal-buttons {
    display: flex;
    gap: 8px;
    margin-right: 15px;
}
.term-btn {
    width: 12px;
    height: 12px;
    border-radius: 50%;
}
.term-close { background-color: #ff5f56; }
.term-min { background-color: #ffbd2e; }
.term-max { background-color: #27c93f; }
/* 终端标题文字 */
.terminal-title {
    color: #ccc;
    font-size: 0.9em;
}
/* 终端内容区段 */
.terminal-content p {
    margin: 5px 0;
    line-height: 1.6;
}
.prompt { color: #008AFF; font-weight: bold; }
/* 闪烁的光标动画 */
.cursor {
    display: inline-block;
    width: 8px;
    height: 16px;
    background-color: #00ff00;
    animation: blink 1s step-end infinite;
    vertical-align: middle;
}
@keyframes blink { 50% { opacity: 0; } }

/* ==========================================
   图表区域容器样式 (包含雷达图和脑图)
   ========================================== */
.chart-section {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin: 40px 0;
}
.radar-container {
    flex: 1;
    min-width: 300px;
    height: 350px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    padding: 10px;
}
.mindmap-container {
    flex: 1;
    min-width: 300px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: zoom-in; /* 添加放大镜鼠标样式 */
    position: relative;
    transition: all 0.3s ease;
    /* overflow: hidden;  移除这个属性，避免遮挡渲染后的元素，交由内部自适应 */
}
/* 针对 Mermaid SVG 设定自适应宽高，防止留白和溢出 */
.mindmap-container .mermaid {
    width: 100%;
    height: 350px; /* 给外层容器固定高度，配合雷达图 */
    display: flex;
    align-items: center;
    justify-content: center;
}
.mindmap-container .mermaid svg {
    max-width: 100%;
    max-height: 100%;
    width: auto !important; /* 强制覆盖 mermaid 的内联宽度，实现等比缩放 */
    height: auto !important; /* 强制覆盖 mermaid 的内联高度，实现等比缩放 */
}
/* 放大提示角标 */
.mindmap-container::after {
    content: '🔍 点击放大';
    position: absolute;
    bottom: 10px;
    right: 10px;
    font-size: 12px;
    color: #888;
    background: rgba(255,255,255,0.8);
    padding: 2px 6px;
    border-radius: 4px;
    pointer-events: none;
}

/* 脑图全屏放大状态样式 */
.mindmap-fullscreen {
    position: fixed !important;
    top: 5vh;
    left: 5vw;
    width: 90vw !important;
    height: 90vh !important;
    z-index: 9999;
    background-color: rgba(255, 255, 255, 0.98) !important;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: zoom-out !important;
    padding: 40px !important; /* 增加放大状态下的内边距，防止内容贴边或被截断 */
    box-sizing: border-box;
    border-radius: 12px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    max-width: none !important;
    flex-direction: column;
}
/* 添加一个背景遮罩层 */
.mindmap-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0,0,0,0.5);
    z-index: 9998;
    display: none;
    cursor: zoom-out;
}
.mindmap-overlay.active {
    display: block;
}
.mindmap-fullscreen .mermaid {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
/* 放大 SVG 尺寸 */
.mindmap-fullscreen .mermaid svg {
    max-width: 100% !important; /* 充分利用弹窗内部空间 */
    max-height: 100% !important; /* 充分利用弹窗内部高度 */
    width: auto !important;
    height: auto !important;
    transform: none; /* 移除 transform，直接依赖 flex 和容器宽高自适应 */
    transition: all 0.3s ease;
}
/* 全屏时的关闭提示 */
.mindmap-fullscreen::after {
    content: '✖ 点击任意处关闭' !important;
    top: 20px;
    right: 30px;
    bottom: auto;
    font-size: 14px;
    background: #f1f1f1;
    color: #333;
    padding: 5px 10px;
    cursor: pointer;
    pointer-events: auto;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

/* ==========================================
   技能卡片网格布局样式
   ========================================== */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 30px;
}
.skill-card {
    background: #fff;
    border: 1px solid #eaeaea;
    border-top: 4px solid #008AFF;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}
/* 卡片悬停时的动态浮起效果 */
.skill-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 15px rgba(0,138,255,0.15);
    border-top-color: #0056b3;
}
.skill-card h4 {
    margin-top: 0;
    color: #333;
    display: flex;
    align-items: center;
    gap: 10px;
}
.skill-card ul {
    padding-left: 20px;
    color: #666;
    margin-bottom: 0;
}

/* ==========================================
   底部引用块美化样式
   ========================================== */
.quote-block {
    text-align: center;
    font-size: 1.2em;
    font-style: italic;
    color: #008AFF;
    margin: 50px 0 20px;
    padding: 20px;
    border-top: 1px dashed #ccc;
    border-bottom: 1px dashed #ccc;
}
</style>

<!-- 终端风格个人简介模块 -->
<div class="terminal-window">
    <div class="terminal-header">
        <div class="terminal-buttons">
            <div class="term-btn term-close"></div>
            <div class="term-btn term-min"></div>
            <div class="term-btn term-max"></div>
        </div>
        <div class="terminal-title">bash - ckhuang@macbook:~</div>
    </div>
    <div class="terminal-content">
        <p><span class="prompt">ckhuang@macbook:~$</span> whoami</p>
        <p>CK·黄</p>
        <p><span class="prompt">ckhuang@macbook:~$</span> cat profile.json</p>
        <p>{<br>
        &nbsp;&nbsp;"role": "分布式架构专家 / 终身学习者",<br>
        &nbsp;&nbsp;"status": "热爱技术与开源，对新技术保持高度敏感",<br>
        &nbsp;&nbsp;"mission": "致力于将技术与业务场景深度融合"<br>
        }</p>
        <p><span class="prompt">ckhuang@macbook:~$</span> <span class="cursor"></span></p>
    </div>
</div>

<!-- 可视化图表展示区 -->
<div class="chart-section">
    <!-- ECharts 雷达图容器 -->
    <div id="skills-radar" class="radar-container"></div>
    
    <!-- Mermaid 技能树容器 (支持点击放大) -->
    <div class="mindmap-overlay" id="mindmap-overlay"></div>
    <div class="mindmap-container" id="mindmap-box" title="点击放大查看脑图">
        <div class="mermaid">
        mindmap
          root((核心技能树))
            分布式架构
              Spring Cloud Alibaba
              Kubernetes
              微服务实战
            大数据与中间件
              Spark / Flink
              Kafka / RocketMQ
              Redis / MySQL
            AI工程化
              大语言模型 LLM
              Agent应用架构
              PyTorch / TensorFlow
            技术管理
              团队组建从0到1
              技术选型与评估
              Code Review
        </div>
    </div>
</div>

<h3 style="text-align: center; margin-top: 40px; margin-bottom: 20px;">技术栈与经验详解</h3>

<!-- 卡片式技能详情展示区 -->
<div class="skills-grid">
    <div class="skill-card">
        <h4>🛠️ 分布式架构专家</h4>
        <p><strong>10 年以上研发经验</strong>及 <strong>5 年以上架构设计经验</strong>，擅长高并发、高可用分布式系统设计。</p>
        <ul>
            <li>精通 <strong>Spring Cloud Alibaba</strong> 与 <strong>Kubernetes</strong> 云原生技术。</li>
            <li>具备丰富的微服务架构实战能力，提供稳定可靠的技术底座。</li>
        </ul>
    </div>

    <div class="skill-card">
        <h4>📊 大数据与中间件深度掌握</h4>
        <p>具备处理海量数据的实战经验与核心组件的深度调优能力。</p>
        <ul>
            <li>熟练掌握 <strong>Spark、Flink、Kafka</strong> 等大数据处理技术。</li>
            <li>深入理解 <strong>MySQL、Redis、RocketMQ</strong> 等，擅长性能调优与复杂排查。</li>
        </ul>
    </div>

    <div class="skill-card">
        <h4>🚀 技术管理与团队赋能</h4>
        <p>拥有 <strong>5 年以上技术团队管理经验</strong>，具备优秀的技术选型和评估能力。</p>
        <ul>
            <li>具备从 0 到 1 组建并带领团队攻坚的成功经验。</li>
            <li>通过 Code Review 与技术分享提升代码质量，推动技术演进。</li>
        </ul>
    </div>

    <div class="skill-card">
        <h4>🤖 AI 工程化能力</h4>
        <p>紧跟行业趋势，具备将 AI 算法落地到实际业务中的架构思维。</p>
        <ul>
            <li>熟悉 <strong>TensorFlow、PyTorch</strong> 等主流 AI 框架。</li>
            <li>深入了解 <strong>LLM</strong> 及 <strong>Agent 应用架构</strong>，解决模型服务化难题。</li>
        </ul>
    </div>
</div>

<!-- 底部金句 -->
<div class="quote-block">
    “终身学习，持续精进。” —— 逻辑思维与抽象能力 / 快速学习与适应能力
</div>

<!-- 脑图点击放大交互脚本 -->
<script>
    document.addEventListener("DOMContentLoaded", function() {
        var mindmapBox = document.getElementById('mindmap-box');
        var overlay = document.getElementById('mindmap-overlay');
        
        if (mindmapBox && overlay) {
            // 定义切换放大状态的函数
            function toggleFullscreen() {
                mindmapBox.classList.toggle('mindmap-fullscreen');
                overlay.classList.toggle('active');
                
                // 处于放大状态时，禁用底层页面滚动
                if (mindmapBox.classList.contains('mindmap-fullscreen')) {
                    document.body.style.overflow = 'hidden';
                } else {
                    document.body.style.overflow = '';
                }
            }

            // 监听点击事件实现放大/缩小
            mindmapBox.addEventListener('click', toggleFullscreen);
            // 点击遮罩层也可以关闭放大效果
            overlay.addEventListener('click', toggleFullscreen);
        }
    });
</script>

<!-- ECharts 初始化脚本 -->
<script>
    // 获取图表容器并初始化 ECharts 实例
    var chartDom = document.getElementById('skills-radar');
    var myChart = echarts.init(chartDom);
    var option;

    // 配置雷达图参数
    option = {
        title: {
            text: '能力维度雷达',
            left: 'center',
            top: 10,
            textStyle: {
                color: '#333',
                fontSize: 16,
                fontWeight: 'normal'
            }
        },
        tooltip: {
            trigger: 'item'
        },
        radar: {
            // 定义雷达图的各个维度及最大值
            indicator: [
                { name: '分布式架构', max: 100 },
                { name: '大数据&中间件', max: 100 },
                { name: 'AI工程化', max: 100 },
                { name: '技术管理', max: 100 },
                { name: '逻辑抽象', max: 100 },
                { name: '学习适应', max: 100 }
            ],
            radius: '60%',
            center: ['50%', '55%'],
            splitNumber: 4,
            axisName: {
                color: '#008AFF',
                fontWeight: 'bold'
            },
            // 雷达图背景分隔区域样式
            splitArea: {
                areaStyle: {
                    color: ['#f8f9fa', '#f1f3f5', '#e9ecef', '#dee2e6'],
                    shadowColor: 'rgba(0, 0, 0, 0.1)',
                    shadowBlur: 10
                }
            },
            axisLine: {
                lineStyle: { color: '#ced4da' }
            },
            splitLine: {
                lineStyle: { color: '#ced4da' }
            }
        },
        series: [
            {
                name: '核心能力评估',
                type: 'radar',
                data: [
                    {
                        // 对应的各项能力评分
                        value: [95, 90, 85, 90, 95, 100],
                        name: '技能指数',
                        itemStyle: {
                            color: '#008AFF'
                        },
                        areaStyle: {
                            color: 'rgba(0, 138, 255, 0.2)'
                        },
                        lineStyle: {
                            width: 2
                        },
                        symbolSize: 6
                    }
                ]
            }
        ]
    };

    // 渲染图表
    option && myChart.setOption(option);
    
    // 监听窗口大小变化，实现响应式重绘
    window.addEventListener('resize', function() {
        myChart.resize();
    });
</script>