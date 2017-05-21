---
layout: post 
title: "所丫日报"
date: 2016-05-20
category: soyainedaily
excerpt: "学习笔记 CSS绘图"
---

## 学习笔记

参照一个教程做了练习。[纯CSS制作的图形效果](http://www.w3cplus.com/css/create-shapes-with-css)，下面记录一些心得。

`border-radius: top right bottom right;`

关于这四个属性值，对于绘制的扇形和圆的方向起着决定性作用，在写代码的时候可以这样理解：四个值依次对应从上方开始，顺时针的四个方向，确切的说对应的弧度方向是左上、右上、右下、左下，也就是说 `top` 对应的是正上方逆时针旋转 45° 后的方向。

绘制椭圆：椭圆的特点是纵向横向都对称，与圆的区别在于纵向与横向半径不相等，分别叫做长半轴和短半轴。教程里运用的思想是，使用 `border-radius` 的 X/Y 两轴取值，如下面这样：当这两个值与 `div` 的长和宽相等时，也就相当于横向（X）和纵向（Y）的轴长度，但这两个值小于宽和长时，。

```css
.oval {
    width: 300px;
    height: 200px;
    border-radius: 300px/200px;
}
```

参考一下 MDN 文档，解释得比较详细。

> ```
> 半径的第一个语法取值可取1~4个值:
> border-radius: radius             
> border-radius: top-left-and-bottom-right top-right-and-bottom-left 
> border-radius: top-left top-right-and-bottom-left bottom-right 
> border-radius: top-left top-right bottom-right bottom-left 
>
> 半径的第二个语法取值也可取1~4个值
> border-radius: (first radius values) / radius             
> border-radius: (first radius values) / top-left-and-bottom-right top-right-and-bottom-left 
> border-radius: (first radius values) / top-left top-right-and-bottom-left bottom-right 
> border-radius: (first radius values) / top-left top-right bottom-right bottom-left 
>
> border-radius: inherit
> ```

`border-radius` 用于设置边框的圆角，显示的是圆与边框交集的部分，共有两种语法，每种都可以取 4 个值，值的个数不同，意义分别如下：

1. 半径
2. 矩形两个对角线方向
3. 左上，「撇」字形对角线方向，右下
4. 左上，右上，右下，左下（顺时针）

在这里我注意到以下一些问题：

1. 一值语法中，值代表半径，这个值大于长度的 50% （可 px 或 %）时，效果是正圆或者正椭圆。注意这个不适用于 / 的情况。
2. 这些值是指的半径或半长轴、半短轴。

张鑫旭的[一篇文章](http://www.zhangxinxu.com/wordpress/2015/11/css3-border-radius-tips/) 讲了这件事，明天细读。

## 其他

我觉得应该认真思考下我的日报。另外每日时间记录也是。

每晚一困就什么都不想写了，这个或许需要调整一下。

正如现在，我困了。。21:51 晚安。