# 项目简介 (Project Overview)
本项目是 CK·黄 (黄炳龙) 的个人博客网站，基于 [Beautiful Jekyll](https://beautifuljekyll.com/) 主题构建，托管在 GitHub Pages 上 (ckatgithub.github.io)。
网站名称：黄炳龙@终身学习

# 技术栈 (Tech Stack)
- **静态网站生成器**: Jekyll (Ruby)
- **标记语言**: Markdown, HTML
- **样式与脚本**: CSS, JavaScript (通过 Beautiful Jekyll 主题集成)
- **包管理**: Bundler (`Gemfile`)

# 项目结构 (Project Structure)
- `_posts/`: 存放所有博客文章 (Markdown 格式)，文件命名规范为 `YYYY-MM-DD-title.md`。
- `_config.yml`: 网站的全局配置文件，包含标题、导航栏、个人信息、第三方集成等配置。
- `_layouts/` & `_includes/`: HTML 模板文件，用于控制网站的布局和组件。
- `assets/`: 静态资源文件，包括图片 (`img/`)、样式 (`css/`) 和脚本 (`js/`)。
- `_data/`: 包含网站使用的数据文件（如 `ui-text.yml`）。

# 常用命令 (Commands)
- **安装依赖**: 
  ```bash
  bundle install
  ```
- **本地启动开发服务器**: 
  ```bash
  bundle exec jekyll serve
  ```
  *(注：启动后可在浏览器访问 `http://localhost:4000` 预览网站。修改 `_config.yml` 以外的文件时，网站会自动重新构建)*

# 写作规范 (Writing Guidelines)
- 所有博客文章必须放置在 `_posts/` 目录下。
- 文件名必须严格遵循日期和标题格式：`YYYY-MM-DD-title.md`。
- 每篇文章的顶部必须包含 YAML Front Matter，格式如下：
  ```yaml
  ---
  layout: post
  title: 文章标题
  subtitle: 文章副标题（可选）
  tags: [标签1, 标签2]
  comments: true
  ---
  ```
- 推荐使用 Markdown 编写内容，保持格式简洁。

# AI 助手行为准则 (AI Assistant Guidelines)
- **语言偏好**: 始终使用中文进行对话与文档输出。
- **代码注释**: 在生成或编辑代码（如 HTML/CSS/JS、Ruby 或 Markdown 结构）时，必须补充详细的中文注释说明。
- **解释说明**: 在修改文件或回答问题时，必须详细解释每一步改动的原因和逻辑。
