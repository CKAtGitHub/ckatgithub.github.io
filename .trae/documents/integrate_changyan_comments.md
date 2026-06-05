# 集成畅言云评 (Changyan Comments) 计划

## 1. 总结

框架（Beautiful Jekyll）确实内置了集成第三方评论组件的能力，目前支持 Disqus、Facebook Comments、Utterances、Staticman 和 Giscus。然而，它并没有内置对“畅言云评”的支持。我们需要通过扩展框架的评论机制，将畅言的代码作为新的评论模板引入并挂载。

## 2. 现状分析

* **`_config.yml`**: 网站的全局配置文件中，包含了一个 `# --- Comments --- #` 区域，通过读取配置来控制不同评论组件的开启状态。

* **`_includes/comments.html`**: 该文件通过判断 `{% if page.comments %}`，并依次引入不同的评论模板文件（如 `disqus.html`）。

* 评论模板的通用逻辑是：在各自的模板文件中判断是否配置了该评论系统的密钥（如 `{% if site.disqus %}`），如果配置了则渲染对应的 HTML+JS 脚本。

## 3. 建议的修改

### 3.1 修改 `_config.yml`

在配置文件中的 `# --- Comments --- #` 区域，添加畅言的配置块，方便以后统一管理。

```yaml
# To use Changyan comments, fill in your appid and conf
changyan:
  appid: "" # 替换为畅言提供的 APP ID
  conf: ""  # 替换为畅言提供的 APP SECRET (Conf)
```

### 3.2 创建 `_includes/changyan-comment.html`

新建一个模板文件，用于存放畅言的集成代码。该代码将动态读取 `_config.yml` 中的 `appid` 和 `conf` 配置。
使用 `page.url` 作为文章的唯一标识符（`sid`）。

```html
{%- if site.changyan -%}
<div class="changyan-comments">
  <!--PC和WAP自适应版-->
  <div id="SOHUCS" sid="{{ page.url | replace: '/', '_' }}"></div>
  <script type="text/javascript">
  (function(){
    var appid = '{{ site.changyan.appid }}';
    var conf = '{{ site.changyan.conf }}';
    var width = window.innerWidth || document.documentElement.clientWidth;
    if (width < 960) {
      window.document.write('<script id="changyan_mobile_js" charset="utf-8" type="text/javascript" src="https://changyan.sohu.com/upload/mobile/wap-js/changyan_mobile.js?client_id=' + appid + '&conf=' + conf + '"><\/script>'); 
    } else { 
      var loadJs=function(d,a){
        var c=document.getElementsByTagName("head")[0]||document.head||document.documentElement;
        var b=document.createElement("script");
        b.setAttribute("type","text/javascript");
        b.setAttribute("charset","UTF-8");
        b.setAttribute("src",d);
        if(typeof a==="function"){
          if(window.attachEvent){
            b.onreadystatechange=function(){
              var e=b.readyState;
              if(e==="loaded"||e==="complete"){
                b.onreadystatechange=null;
                a();
              }
            }
          }else{
            b.onload=a;
          }
        }
        c.appendChild(b);
      };
      loadJs("https://changyan.sohu.com/upload/changyan.js",function(){
        window.changyan.api.config({appid:appid,conf:conf});
      }); 
    } 
  })(); 
  </script>
</div>
{%- endif -%}
```

### 3.3 修改 `_includes/comments.html`

在此文件中增加对新创建的畅言模板的引入。

```html
{% if page.comments %}
  {% include disqus.html %}
  {% include fb-comment.html %}
  {% include staticman-comments.html %}
  {% include utterances-comment.html %}
  {% include giscus-comment.html %}
  {% include changyan-comment.html %} <!-- 新增这一行 -->
{% endif %}
```

## 4. 假设与决定

* **唯一标识 (`sid`)**: 畅言需要一个 `sid` 作为文章的唯一标识，使用 `{{ page.url | replace: '/', '_' }}` 能够保证其唯一性且避免 URL 里的斜杠可能引起的潜在问题。

* **自适应加载**: 使用了畅言官方提供的自适应脚本，会在移动端和 PC 端自动加载不同样式的评论组件。

## 5. 验证步骤

1. 修改完上述代码后，前往畅言官网注册并获取 `appid` 和 `conf`。
2. 将获取到的密钥填入 `_config.yml`。
3. 运行 `bundle exec jekyll serve` 启动本地环境。
4. 打开任意一篇启用了评论的文章页面，检查页面底部是否成功渲染畅言评论框，并确认浏览器控制台无报错信息。

