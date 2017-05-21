---
layout: post 
title: "所丫日报"
date: 2016-05-02
category: soyainedaily
excerpt: "学习笔记 CSS 盒模型"
---

## IFE Practice

|2016-05-02-08:17

### CSS 盒模型

摘抄 《 HTML & CSS 》 Chapter 13 BOXES

LIMITING WIDTH: 

> the min-width property specifies the smallest size a box can be displayed at when the browser window is narrow, and the max-width property indicates the maximum width a box can stretch to when the browser window is wide.

OVERFLOWING: 

> The overflow property tells the browser what to do if the content contained within a box is larger than the box itself. It can have one of two values -- hidden & scroll.

BORDER, MARGIN & PADDING: 

> The border separates the edge of one box from another. Margins site outside the edge of the border, you can set the width of a margin to create a gap between the borders of two adjacent boxes. Padding is the space between the border of a box and any content contained within it. 

这里的三个值中，如果以一座城来比喻的话：border 确定「系统」边界——像是城墙，margin 是「系统」外延部分——像是城墙外的护城河，padding 则是边界与内容之间的部分——像是主城建筑和城墙边之间的间隙。

> If you specify a width for a box, then the borders, margin, and padding are added to its width and height.

margin 可以保证 box 之间的空隙，padding 保证了盒子里的内容不要离边界太近，从而不易阅读。

> If the bottom margin of any box touches the top margins of another, the browser will render it differently than you might expect. It will only show the larger of the two margins. If both margins are the same size, it will only show one.

疑问：那么浏览器在定位的时候是根据什么定位的？渲染出每个元素的特性，然后再展示出来，那冲突是肿么解决的？

BORDER WIDTH

> You cannot use percentages with this property.

``border - width: top right bottom left;``

border - width 特性中除了单独设定每一边的宽度之外，还可以统一设定，连续的 4 个数依次从顶部开始顺时针方向的边，中间以空格分隔。

我用 WebStorm 试了一下，这里用 % 作单位会报错。

BORDER COLOR

这里提到了一种设置色彩的方法 HSL ，是 CSS3 的新特性。

PADDING

> Please note: If a width is specified for a box, padding is added onto the width of the box. 

也就是说 padding 是向外扩展的，当 width 确定时，在此基础上往外扩，而不是在原来的 border 中填充，总的大小会变大。和 border-width 相同，可以使用 shorthand，几个属性的顺序一样。margin 也是一样的道理。

> The value of the padding property is not inherited by child elements in the same way that the color value of the font-family property is; so you need to specify the padding for every element that needs to use it.

MARGIN

 一个 box 在另一个 box 的上面时，小的 margin 被丢弃，使用大的……还是英文说得比较清楚：

> If one box sits on top of another, margins are collapsed( 坍塌 ), which means the larger of the two margins will be used and smaller will be disregarded.

SHORTHAND

按照一定的顺序（width style color）在一条语句里声明 border 的属性。整理一下每个 property 的 shorthand 写法：

- border-width / margin / padding: top right bottom left;
- margin / padding: left right; 
- border: width style color;

 书里例子用的单位是 px，WebStorm 试了一下 margin / padding 可以用 %，border-width 不行。

对于 margin / padding: left right;  这样的写法，虽只写了两个，但是 Chrome 和 Firefox 中的 CSS 把四个边都自动生成了。如我写 ``margin: 20px 20px;padding: 20% 20%;``  Chrome 和 Firefox 里的样式是 

margin: 20px 20px;
    margin-top: 20px;
    margin-right: 20px;
    margin-bottom: 20px;
    margin-left: 20px;
padding: 20% 20%;
    padding-top: 20%;
    padding-right: 20%;
    padding-bottom: 20%;
    padding-left: 20%;
10:00

16:36

DISPLAY & VISIBILITY

display: inline / block / inline-block / none

visibility: hidden visible

> If you use display property, it is important to note that inline boxes are not supposed to create block-level elements.

17:09