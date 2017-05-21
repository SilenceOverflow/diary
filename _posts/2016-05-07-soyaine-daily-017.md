---
layout: post 
title: "所丫日报"
date: 2016-05-07
category: soyainedaily
excerpt: "学习笔记，其他想法"
---

## 学习笔记 IFE

### CSS 布局

#### position

1. static： position 的默认值，表示未被  positioned，一个元素被设置成其他值，则表示被 positioned。
2. relative：如果没有设置 top、right、bottom、left 属性，表现和 static 相同。
3. fixed：元素相对于视窗进行定位，与页面是否滚动无关。top、right、bottom、left 属性可用。原本在页面应有的空隙不会被保留。（这里的原本指没有设置成 fixed 时。
4. absolute：相对于**最近的 positioned 祖先元素**（若没有则相对于 body 元素）定位。 positioned 指 position 值不是 static 的元素。

#### float

可以用于实现文字环绕图片。

摘抄 《CSS 权威指南》

> 1. 会以某种方式将浮动元素从文档的正常流中删除，不过它还是会影响布局。
> 2. 一个元素浮动时，其他内容会「环绕」 该元素。
> 3. 浮动元素周围的外边距不会合并。
> 4. float: none 用于防止元素浮动。如果没有 none 值，所有元素都会以某种方式浮动。
> 5. containning block(包含块)：浮动元素的包含块是其最近的块级祖先元素。
> 6. 如果没有足够的空间，浮动元素会被挤到新的行。

我觉得 float 的特点中外边距不会合并这点，会影响使用，如 无法用 margin 来为一些 float 元素预留空间，因为它会自动转到下一行。

float 还有很多要学的。

### 解决问题

#### 设置三栏式布局

我用目前所学的 position 来进行布局，首先父 div 的 position 值不能为 static，所以设置成 relative。左侧栏、右侧栏采用 absolute 定位，中间栏采用 relative 定位，并通过 margin-left 与 margin-right 的设定，空出左右两侧栏的位置。

### 参考链接

http://stackoverflow.com/questions/211383/which-method-of-clearfix-is-best

http://www.barelyfitz.com/screencast/html-training/css/positioning/

http://zh.learnlayout.com/position-example.html

## 其他想法

感冒，崩溃。排练曲子，被小伙伴们的欢快情绪感染了，回来竟然还能再学习一些东西，感谢这样一个正能量聚集的地方，只要跨出第一步，剩下的是不会让自己失望的。