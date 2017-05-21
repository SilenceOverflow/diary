---
layout: post
title: "所丫日报" 
date: 2017-01-10 
category: soyainedaily 
excerpt: "Diary 更新日志，TransChart 项目进程记录"
---

## Diary 日志

又有一个人通过博客关注了公众号，这促使我把 Diary 修一修。

### url 的 JSON 数据中日期的处理

刚才把部分日期链接无法加载的问题给解决了，主要是改变了一下获取日期的方式，以前是通过 `post.date`，其中夹杂着具体的时间，所以需要先替换 - 和 0 再切割字符串，于是我就改成了直接从 `post.url` 中获取日期，先切再替换。这样一想，其实之前的办法中，把切割的顺序替换一下也可以。修改后的代码如下（刚才写 raw 的时候又把 {} 写成了 <>……：

{% raw %}
```liquid
{{ post.url | slice: 1, 10 | replace: '-', '/' | replace: '/0', '/' | strip }}
```
{% endraw %}

### 其他：maximum-scale 拼写、CSS 细节

页面一直提示这样的错误信息 `The key "maximum-scala" is not recognized and ignored.` 查了一下发现是自己写错了一个字母，(⊙﹏⊙)b

以及移动端下页面宽度 > 屏幕宽度。是因为我 footer 中的说明 div 设置了 `width: 30em`，最初是为了和右对齐的元素撑开距离，但后来采用了另一种布局。在移动端下，这个长度过长，导致页面宽度被撑开。

此外 TODOlist 还很长，比如加个目录、还有日历的年份切换、链接的效果。在记录 SoyaineDaily 的时候，正确的流程应该是，先修改代码错误的地方，然后等待 Jekyll 重新生成页面，这个时间用来记录。简短的日志如下：

1. fix some css' bug
2. fix the date json pattern

## TransChart 项目进程记录

最大的一个数据文件导入完成，`[Msg] Finished - 5198527 queries executed successfully` 用时 59625.063s，换算一下是 16.5625175h，平均一秒运行 87.1869 条语句。

于是可以开始运行真实数据的 SQL 语句，获取到 JSON。

解决的问题：

### Jade 部分

1. **在 Jade 里引入其他的 JS 文件**

   ```jade
   script(src="/javascripts/echarts.js")
   ```

   这里有一点路径的问题，如果要访问 public 文件下的文件，路径按上面的写法，而不需要加 `./` 等。

2. **在 Jade 里引入内联的 JS 语句**

   ```jade
   script(type="text/javascript").
       var option = !{JSON.stringify(optionJSON)};
       option.xAxis["data"] = !{JSON.stringify(xAais)};
   ```

   后面加一个点，这样后面的语句就不会按照模板文本来解析。

3. **在 Jade 里引入变量中的 JSON 数据**

   也是上一点中的方法，先在变量之中获取 JSON 对象，然后将其转换成模板中的语句。因为里面还是要用到变量，所以用 `!{xxxx}` 来引入，这里是 `!` 而不是 `#`，用感叹号将不会把一些解析为转义字符的格式，区别如下：

   ```jade
   {"name": "Hello <em>World</em>"}
   li Say #{name} // <li>Say Hello &lt;em&gt;World&lt;/em&gt;</li>
   li Say !{name} // <li>Say Hello <em>World</em></li>
   ```

   用井号的时候， `<` 这样的符号会解析为转义字符 `&lt;` 然后在 HTML 中渲染出来的就是文本格式，无法读取为 JSON 对象。

参考链接：

- [naltatis 的可编辑 Jade 语法文档](https://naltatis.github.io/jade-syntax-docs/)
- [passing a variable from jade to javascript](http://stackoverflow.com/questions/21263337/passing-a-variable-from-jade-to-javascript)
- [How can I render inline JavaScript with Jade?](http://stackoverflow.com/questions/5858218/how-can-i-render-inline-javascript-with-jade)
- [Jade: How to include a javascript file](http://stackoverflow.com/questions/14348776/jade-how-to-include-a-javascript-file)


### Express 部分

记录一下，启动 APP 的语句有以下几种：

```shell
// SHELL 命令行中
$ DEBUG=myapp:* npm start

// Windows 的 cmd 中
> set DEBUG=myapp:* & npm start

// 其他
node app.js
```

### 整体思路

目前我打通的情况是，访问 URL 时，发送 GET/POST 请求，由 Express 的路由处理，连接 MySQL 数据库，运行 query 语句读取所需数据，通过 Response 返回 JSON 数据（包含图表的配置信息），再由 Jade 读取此数据并渲染页面。