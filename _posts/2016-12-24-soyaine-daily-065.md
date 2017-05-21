---
layout: post
title: "所丫日报" 
date: 2016-12-24 
category: soyainedaily 
excerpt: ""
---

## 学习笔记

研究了一下如何配置 _config.yml 里面的信息，我要展示的信息是

````yml
nav:
   Home: http://soyaine.cn
   Diary: http://soyaine.cn/diary/
   Blog: http://soyaine.cn/blog/
   Works: http://soyaine.cn/FE-Practice/
   About: http://soyaine.cn/about.html
````

用在页面上的 Liquid 模板是这样，原理是循环读取值的时候，每一个 `key: value` 对应的是 item[0]: item[1]。


{% raw %}
````html
<ul>
     <!--get the nav links in  _config.yml -->
     {% for link in site.nav %}
     <li><a href="{{ link[1] }}">{{ link[0] }}</a></li>
     {% endfor %}
</ul>
````
{% endraw %}


最后的输出是这样：

````html
<ul>			
	<li><a href="http://soyaine.cn">Home</a></li>
	<li><a href="http://soyaine.cn/diary/">Diary</a></li>
	<li><a href="http://soyaine.cn/blog/">Blog</a></li>
	<li><a href="http://soyaine.cn/FE-Practice/">Works</a></li>
	<li><a href="http://soyaine.cn/about.html">About</a></li>
</ul>
````

参考：

 - http://stackoverflow.com/questions/33880088/how-to-access-multiple-nested-variables-in-jekyll-yaml-config
 - http://www.userx.co.za/journal/displaying-key-value-pairs-in-jekyll-from-yaml-front-matter/
 - https://zh.wikipedia.org/wiki/YAML
 - https://jekyllrb.com/docs/variables/
 - http://jekyllcn.com/docs/variables/
 - https://thinkshout.com/blog/2014/12/creating-dynamic-menus-in-jekyll/
 - https://help.shopify.com/themes/liquid/objects/linklist
 - http://jekyll.tips/jekyll-casts/navigation/
 
## 关于日报
 
 （2016-12-24 17:14 ~ 2016-12-24 19:04）
 
 我今天作了很大的调整，首先是把页面中涉及到的链接和信息都从 _config.yml 的配置信息中导入。另外针对移动端把 CSS 作了调整，在不同宽度下有不同的表现。
 
 有关响应式设计的参考：
 
 - http://alistapart.com/article/responsive-web-design#section3
 - http://mediaqueri.es/
 - [基于vw等viewport视区相对单位的响应式排版和布局](http://www.zhangxinxu.com/wordpress/2016/08/vw-viewport-responsive-layout-typography/)
 - [响应式开发中合理选定CSS媒体查询分割点](https://segmentfault.com/a/1190000007567739)
 - [Naming Media Queries](https://css-tricks.com/naming-media-queries/)
 