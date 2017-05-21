---
layout: post
title: "所丫日报" 
date: 2016-05-28
category: soyainedaily 
excerpt: "生活的思考，学习笔记 CSS Transform"
---

## 生活的思考

日报断了两天——这是生活陷入混乱的征兆，是时候做出一些调整了。觉得该做而未做的事，无论是恐惧、不屑、担忧抑或是不安，今天出来的时候，想到「不能容错的系统不是一个好系统」，我的这个「日报成长系统」面临了一些问题，但这也正好是一个更新升级的机会。

## 学习笔记

主要参考这个教程[ CSS3 Transform ](http://www.w3cplus.com/content/css3-transform)。

2016-05-28 09:15 

transform 一共有五种属性。简单记忆为「悬疑锁牛镇」（看天龙八部的后遗症^_^）——旋转 rotate 、移动 translate 、缩放 scale 、扭曲（斜切） skew 、矩阵 matrix，这些属性值可以混合使用，用**空格**隔开。所有的简单效果如下：

<p data-height="265" data-theme-id="light" data-slug-hash="EyxypK" data-default-tab="css,result" data-user="soyaine" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/soyaine/pen/EyxypK/">CSS tramsform</a> by soyaine (<a href="http://codepen.io/soyaine">@soyaine</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

其中的 skew 为斜切，可以理解为一个四边形的框，框的宽度和高度固定，四个角可旋转，而 skew 设定的角度即是从 90° 旋转的角度，skewX(正数)可以想象成将四边形的 bottom 边往右拉，skewY(正数)则是 right 边往下拉。如下：

<p data-height="265" data-theme-id="light" data-slug-hash="gMOMov" data-default-tab="css,result" data-user="soyaine" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/soyaine/pen/gMOMov/">gMOMov</a> by soyaine (<a href="http://codepen.io/soyaine">@soyaine</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

摘抄总结一下语法：

```css
rotate(<angle>) 

translate(<translation-value>[, <translation-value>不提供默认为零])——(x, y)

translateX(<translation-value>) 

translateY(<translation-value>) 

scale(<number>[, <number>不提供默认为零])

scaleX(<number>)

scaleY(<number>)

skew(<angle> [, <angle>])——(bottom 右, right 下)——下右右下

skewX(<angle>)

skewY(<angle>) 

matrix(<number>, <number>, <number>, <number>, <number>, <number>)——这个我没有细究
```

2016-05-28 10:33