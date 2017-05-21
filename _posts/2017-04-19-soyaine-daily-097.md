---
layout: post
title: "所丫日报" 
date: 2017-04-19 
category: soyainedaily 
excerpt: "开发手记"
---

## 开发手记

1. Webstorm 中的 Debug/Run Configuration 中是可以设置多个 Node.js 的运行配置的，也就很容易在调试的时候同时启动多个 Process，会导致某个 Process 中的断点变成灰色，而无法调试。
2. 使用 node-mysql 的 `conn.query(sql, param, fn(err, result){})` 方法返回的 `result` 是一个 包含了 RowDataPacket Object 型数据的数组。可以通过 `JSON.stringify(result)` 将其转化成 JSON 数据，也可以直接视为对象来进行操作。
3. flex 的一些相关基础
	- parent container: display, flex-direction, flex-wrap, flex-flow, justify-content, align-items, align-content
	- flexbox children item: order, flex-grow, flex-shrink, flex-basis, flex, align-self
	- 参考：[A Visual Guide to CSS3 Flexbox Properties](https://scotch.io/tutorials/a-visual-guide-to-css3-flexbox-properties) 很喜欢这个网站的排版，响应式，清晰简洁，文章内容也很棒。

斟酌了很久是把模板的参数拼接成一个字符串，还是新建一个表来存储。参数的特点是个数不固定但格式固定，若另建表，每次渲染页面会增加数据库的读取操作，所以最后尝试拼接字符串，之后处理的时候用正则来匹配解析，每组以对象形式存入数组，传递给 Pug 模板。  

一些正则小 Tips：
1. `&`不需要斜杠转义，但 `#` `$` 就需要。
2. 中文 `[\u4e00-\u9fa5]`
3. [在线正则测试工具](http://tool.oschina.net/regex) 