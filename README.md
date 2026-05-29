# 黄炳龙@终身学习 (Personal Blog)

本项目是 CK·黄 (黄炳龙) 的个人博客网站，基于 [Beautiful Jekyll](https://beautifuljekyll.com/) 主题构建，托管在 GitHub Pages 上 (ckatgithub.github.io)。

## 1. 本地编译与启动项目 (Local Build & Run)

本项目使用 [mise](https://mise.jdx.dev/) 来管理开发环境与执行任务。如果你希望在本地编译和预览本项目，请按照以下步骤操作：

### 安装环境与依赖
首先确保你已安装 `mise`。然后在项目根目录下运行：
```bash
# 1. 安装项目所需的 Ruby 版本
mise install

# 2. 安装 Gemfile 中定义的所有依赖包
mise run install
```

### 本地启动开发服务器
运行以下命令来启动 Jekyll 的本地服务器：
```bash
# 启动本地服务器，并监听文件修改自动重新构建
mise run serve
```
启动成功后，打开浏览器访问 [http://localhost:4000](http://localhost:4000) 即可预览网站。当你修改 `_config.yml` 以外的文件时，网站会自动重新构建。

## 2. 常见问题排查 (Troubleshooting)

**依赖或版本找不到报错**
由于本项目改用 `mise` 管理 Ruby 环境，你可以完全避开 macOS 自带的受限 Ruby。如果依然遇到问题：
1. 确认你已经正确执行了 `mise install`。
2. 确认 `mise run install` 是否成功安装了所有的依赖包。
3. 如果是在较新的 Ruby 版本（如 Ruby 3.4+）下执行报错找不到 `base64` 或 `bigdecimal`，请确认这些 gem 已经在 `Gemfile` 中声明（当前已配置好）。
4. 若遇到由于旧版生成的依赖冲突，可以尝试删除锁文件后重新安装：
   ```bash
   rm Gemfile.lock
   mise run install
   ```

## 3. 打包构建 (Build & Package)

如果你只需要生成静态文件（例如用于离线检查或部署到其他静态托管平台），可以运行：
```bash
# 将网站编译为纯静态 HTML/CSS/JS，并输出到 _site/ 目录下
mise run build
```
执行完毕后，所有生成的静态资源都将存放在项目根目录的 `_site/` 文件夹中。

## 4. 部署发布 (Deployment)

本项目通过 **GitHub Pages** 进行托管和自动化部署。由于仓库命名规范为 `<username>.github.io`，发布流程非常简单：

1. **编写文章**：在 `_posts/` 目录下新增或修改你的 Markdown 博客文章。
2. **提交代码**：将修改后的文件通过 Git 提交。
   ```bash
   git add .
   git commit -m "Add new blog post"
   ```
3. **推送代码**：推送到 GitHub 仓库的默认分支（通常是 `master`）。
   ```bash
   git push origin master
   ```
4. **自动部署**：推送完成后，GitHub 会自动触发后台构建流程（可以在仓库的 Actions 面板查看进度）。通常等待 1~3 分钟，线上网站即可更新。
