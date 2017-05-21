---
layout: post 
title: "所丫日报"
date: 2016-05-03
category: soyainedaily
excerpt: "关于日报，学习笔记 CSS盒模型，IFE Practice，阅读，运动"
---

|2016-05-03-08:40

## 关于日报

昨天运动完之后太困了，发完邮件之后就直接睡过去了，眼镜都没有摘 o(≧口≦)o ，所以积累起来的 12 streaks 就这么没……有……了……不过也不算是「一切重头再来」，至少辅助我形成了习惯，之后倒是可以专注于内容而非数量了。

##  IFE Practice

### CSS 盒模型

|2016-05-03-15:00

#### BOX SHADOWS

三种语句分别是为了支持不同版本的浏览器，我此前一直没加 box-shadow ，所以在 Firefox 中无法显示出效果，查到如下：[参考文章 CSS3 box-shadow](http://www.cnblogs.com/gaoxue/articles/2287311.html)

```css
//Firefox4.0-
-moz-box-shadow: ;
//Safari and Google chrome10.0-
-webkit-box-shadow: ;
//Firefox4.0+ 、 Google chrome 10.0+ 、 Oprea10.5+ and IE9
box-shadow:  ;
```

具体的 shadow 语法：

```CSS
E {box-shadow: <length> <length> <length>?<length>?||<color>}

E {box-shadow:inset x-offset y-offset blur-radius spread-radius color}

E {box-shadow:投影方式 X轴偏移量 Y轴偏移量 阴影模糊半径 阴影扩展半径 阴影颜色}
```

其中 x 偏移量和 y 偏移量的负数分别代表向左和向上。

除颜色外只写 3 位的时候，第 3 个值代表模糊半径。

用逗号分隔可以叠加阴影（投影）。

```
box-shadow: 5px -5px 5px 0px #4BC63B, 
            5px -5px 5px 0px #154054, 
            5px -5px 5px 0px #7A94F4;
```

辅助工具 [Box-shadow generator](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Box-shadow_generator) -- This tool lets you construct CSS box-shadow effects, to add box shadow effects to your CSS objects.

**inset** keyword for inner-shadow:

```css
box-shadow: inset 5em 1em gold;
```

> The inset keyword can also bu used before these value to create an **inner-shadow.**

2016-05-03-15:46|

### Practice 情况

主要在做任务二，学了 CSS 的盒模型相关知识后，发现了很多之前没有注意到的细节，把学到的东西都应用进去了：阴影、圆角、margin 设为 auto 来居中布局。

这么一些才发现虽然看书用的时间长，但是实际收获的知识点有些细碎和「少」。或许这是刚开始学习时需要克服的「重力」带来的惯性。

看到豆瓣和小米的计划在 5 月要结束了，这回我想要用心准备了。

## 阅读

看了一点《奇特的一生》，专注能力有些下降，旁边有人说话时需要费劲的集中精力，特别是中午醒来好几个人在「高谈阔论」的时候，又想起了「一个女人相当于 7 只鸭子」那句话，神烦。（起床气犯了……）

看了读库小报前几天推送的「老六写得最文艺的一篇文章」，是他关于一本被拍成电影的书的感想，书里两人一个在伦敦一个在纽约，通过书信来往，一人帮另一人找那些绝版的书籍……想去看看这部电影。看老六的这篇文章，明明看起来是很简单普通的句子和事情，到最后却泪眼朦胧。

看了一点奥巴马最近在白宫晚宴的演讲……「段子手」果真实至名归。

## 其他-运动

跑步结束的时候，想到一个坚持下去的理由。当我的马甲线越来越明显，线条围度越来越棒，我就越有机会去匹配心中理想的另一半。虽然这些外延的东西好像并不是主要决定因素，但当我是这样的人时，我才能在人群中轻松的识别出这样的人。这是突然的想法。