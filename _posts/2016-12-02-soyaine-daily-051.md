---
layout: background
title: "所丫日报" 
date: 2016-12-02 
category: soyainedaily 
excerpt: ""
---

## 学习笔记

### 两端对齐

[拜拜了,浮动布局-基于display:inline-block的列表布局](http://www.zhangxinxu.com/wordpress/2010/11/%E6%8B%9C%E6%8B%9C%E4%BA%86%E6%B5%AE%E5%8A%A8%E5%B8%83%E5%B1%80-%E5%9F%BA%E4%BA%8Edisplayinline-block%E7%9A%84%E5%88%97%E8%A1%A8%E5%B8%83%E5%B1%80/)

[大小不固定的图片和多行文字的垂直水平居中](http://www.zhangxinxu.com/study/200908/img-text-vertical-align.html)

[我所知道的几种display:table-cell的应用](http://www.zhangxinxu.com/wordpress/2010/10/%E6%88%91%E6%89%80%E7%9F%A5%E9%81%93%E7%9A%84%E5%87%A0%E7%A7%8Ddisplaytable-cell%E7%9A%84%E5%BA%94%E7%94%A8/)

[Spacing in  tags with display table-cell](http://stackoverflow.com/questions/23615895/spacing-in-li-tags-with-display-table-cell)

[Display: table-cell on new row](http://stackoverflow.com/questions/14772778/display-table-cell-on-new-row)

[How to vertical align an inline-block in a line of text?](http://stackoverflow.com/questions/5932201/how-to-vertical-align-an-inline-block-in-a-line-of-text)

[【原】css实现两端对齐的3种方法](http://www.cnblogs.com/PeunZhang/p/3289493.html)

尝试了几种之后，选择了 inline-block + justify 的方法，实现了两端对齐的效果。

### :before 等伪元素的 z-index 问题

在给父元素设置了 z-index 之后，它的伪元素设置无效。

解决办法是，重新建了一个 `div` 放在前面以达成我需要的它在底部的效果。但是想要实现奇形怪状的阴影并藏在块元素下面还是需要用到 `z-index` ，这个问题没有解决。

[Z-index with before pseudo-element](http://stackoverflow.com/questions/7822078/z-index-with-before-pseudo-element)

https://www.sitepoint.com/community/t/box-shadow-on-pseudo-elements-z-index-issue/94314