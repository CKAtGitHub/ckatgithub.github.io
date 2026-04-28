# 黄炳龙@终身学习 (Personal Blog)

本项目是 CK.黄 (黄炳龙) 的个人博客网站，基于 [Beautiful Jekyll](https://beautifuljekyll.com/) 主题构建，托管在 GitHub Pages 上 (ckatgithub.github.io)。

## 1. 本地编译与启动项目 (Local Build & Run)

如果你希望在本地编译和预览本项目，请按照以下步骤操作：

### 安装依赖
确保你已经安装了 Ruby 和 Bundler 环境。然后在项目根目录下运行：
```bash
# 安装 Gemfile 中定义的所有依赖包
bundle install
```

### 本地启动开发服务器
运行以下命令来启动 Jekyll 的本地服务器：
```bash
# 启动本地服务器，并监听文件修改自动重新构建
bundle exec jekyll serve
```
启动成功后，打开浏览器访问 [http://localhost:4000](http://localhost:4000) 即可预览网站。当你修改 `_config.yml` 以外的文件时，网站会自动重新构建。

## 2. 常见问题排查 (Troubleshooting)

**macOS 下报错 `can't find gem bundler` 或 `Insecure world writable dir` 等**
如果你在 Mac 上遇到找不到 `bundler` 或目录权限警告的问题，通常是因为使用了 macOS 系统自带的、受限且老旧的 Ruby 环境。**强烈建议使用 Homebrew 安装独立的 Ruby 环境：**

```bash
# 1. (可选) 修复目录权限警告
sudo chmod go-w /usr/local/bin

# 2. 安装 Homebrew 版 Ruby
brew install ruby

# 3. 将新版 Ruby 注入到环境变量中 (针对 zsh 终端)
echo 'export PATH="/usr/local/opt/ruby/bin:/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# 4. 如果你在使用较新的 Ruby (例如 Ruby 3.4+)，可能需要手动安装一些被移出标准库的 gem。
# 如果执行 bundle exec jekyll serve 时报错找不到 base64 或 bigdecimal 等，请在 Gemfile 中添加：
# gem "base64"
# gem "bigdecimal"

# 5. 删除可能由旧版生成的 Gemfile.lock (可选，如果遇到依赖版本冲突时)
rm Gemfile.lock

# 6. 安装依赖并启动
bundle install
bundle exec jekyll serve
```

## 3. 打包构建 (Build & Package)

如果你只需要生成静态文件（例如用于离线检查或部署到其他静态托管平台），可以运行：
```bash
# 将网站编译为纯静态 HTML/CSS/JS，并输出到 _site/ 目录下
bundle exec jekyll build
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
