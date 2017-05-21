---
layout: post
title: "所丫日报" 
date: 2017-01-09 
category: soyainedaily 
excerpt: "TransChart 项目进程记录，阅读记录：EJS Jade MVC MVVM"
---

## TransChart 项目进程记录

参阅了几个链接走了一下 Hello World 的流程，项目所涉及到的功能大概可以跑通了。记录一下参考的链接：

http://www.alloyteam.com/2015/03/sexpressmysql/

跟着这篇文章，主要是弄清楚了路由和数据库连接池的操作，如何在响应里返回 JSON 数据、如何对 post 请求进行响应、如何在前端用 Jade 构建一个表单用于构建 post 请求 / 用 URL 参数形式构建 get 请求。

> 一个在线测试路由的工具：
>
> http://forbeslindesay.github.io/express-route-tester/?_ga=1.65779310.1159870132.1483853819

昨天把 MySQL 重装了一遍，换了 5.1 的版本，把 Navicat 也换成了 10，中途遇到了一些问题，版本冲突、卸载不干净。最后的解决办法是，把注册表里所有 MySQL 相关的删除，把 C:\ProgramData\MySQL\MySQL Server 5.0\data 下的数据删除，这里面是之间建立的数据库的数据。然后重装。

其中有个部分需要输密码，初始密码可以为空。今天导入剩下的数据，明天就可以处理真正的数据了。随手截了个图：

![2017-01-09-22:02 的截图](https://cl.ly/1K1o2r3V2h2H/Image%202017-01-09%20at%2010.02.27%20PM.png)

## 阅读过程记录

### MVC TO MVVM

在阮一峰的博客看到有人推荐这篇文章（[谈谈UI架构设计的演化](http://weibo.com/p/1001603808855434892996)），就找来看了看。

 大概经历的过程是：

> 注：以下部分基本是原文的缩略和摘抄。

- MVC(1979 Trygve Reenskaug) 

  ![Trygve Reenskaug的图](https://camo.githubusercontent.com/17749aa6915f9bab027dddc91783c86ac0a2010c/68747470733a2f2f6865696d2e6966692e75696f2e6e6f2f253745747279677665722f7468656d65732f6d76632f4d56432d323030362e676966)


- 控件系统（Control）：在 Windows 的 WIMP 风格成为主流时出现，Control 预制组件带有一定的交互功能，既有 View 也有 Controller。

  > controller的输入分配功能，则被操作系统提供的各种机制取代：
  >
  > ……（指针系统、文本系统、焦点系统）
  >
  > 所以时至今日，MVC，尤其是其中controller的功能已经意义不大，**若是在控件系统中，再令所有用户输入流经一个controller则可谓不伦不类、本末倒置**。

- MVP(1996 Taligent CTO Mike Potel)：Model-View-Presenter

  ![这个时期主流的 View 概念](https://camo.githubusercontent.com/c3dd0f9f77b116f5b5b4ce9fb82ac136a68664b3/687474703a2f2f7777322e73696e61696d672e636e2f6d773639302f34373465626633356777316570346f6b727a34716a6a32306f6d3065753430352e6a7067)

  在 MVC 的基础上规定了一些 Controller 中的概念。所以寒冬说 MVP 和 MVC 的依赖关系图是一样的：

  ![MVP](https://camo.githubusercontent.com/5dc631b7b8b34d3bd1e98debbbe138604e3186f5/687474703a2f2f7777322e73696e61696d672e636e2f6d773639302f34373465626633356777316570346f697a7575776f6a3230767730666f7768612e6a7067)

- MVVM(20世纪 微软架构师John Gossman)：由于标记语言和程序语言的组合开始火起来了。这时候 View 用标记语言来描述，于是在语言上和其他部分隔离开了。这种模式下，数据绑定是个重要的概念，View 和 Model 之间的互相通讯，用双向绑定来替代了，于是把逻辑代码变成了声明模式。

  ![这是寒冬画的图](https://camo.githubusercontent.com/2a09625439c430f360a770c80702f8df2c996156/687474703a2f2f7777332e73696e61696d672e636e2f6d773639302f34373465626633357477316476716e77786338746b6a2e6a7067)

而这是我以前上 Web 课的时候学习的模式：MVC时代下的 JSP+Servlet。

![MVC时代下的 JSP+Servlet](http://i1.piimg.com/567571/2a487392f7f2faa8.png)

### Jade or EJS 模板语言的选择

看了下人们关于 Jade 和 EJS 的讨论。发现一个 HTML 转 Jade 的工具：html2jade

另外有人提出 Jade 无法实现的需求，以及更贴给出了解决办法：

````jade
class="item{if xxx} active{/if}"

//@Daniel Wei 的答案，是用一个 `xxx ? x : y` 来实现判断
第一种：
.test-div(class=true ? 'active' : '')
写起来不是那么困惑的：
.test-div(class="#{true ? 'active' : ''}")
第二种：
- var test_css = (true ? 'active' : '')
.test-div(class=test_css)
以上两种都可以。

//@陶睡之 的答案，也是一样，不过用数组将类名包装了起来
- xxx = 0, yyy = 1
div(class=[
　　　'item',
　　　xxx ? 'active' : '',
　　　yyy ? 'collapsed' : 'expanded'
　　])
　content
````

之前我对 Liquid 比较熟，写我的 [Diary](https://github.com/soyaine/diary) 主题的时候，因为是 Jekyll 默认使用的模板语言，所以把它的文档翻来覆去看了好几遍。想想我在三个月前，连”模板“这个词都不知道，那时候提到这个，我第一想到的是 PowerPoint 里面的”母版“，汗颜。今天写的项目的过程中，用 Express 生成器的时候，在 views 中会自动生成一些模板文件，我也是第一次知道了这两种类型。

我两种都试了一下，最开始只能看出 Jade 是依靠缩进来表示结构，但后来看了一篇文章（[前端开发模板引擎 -- Jade系列之数据的动态传递和流程控制](http://www.html-js.com/article/Dynamic-data-front-end-development-template-engine--Jade-syntax-on-the-frontend-development-template-engine--Jade-transfer-and-process-control)~en）就可以很快上手了，代码风格真的是简洁明了，可以用 `var` 定义变量再使用。而 EJS 则是 JS 和 HTML 混排，有 JSP 和 PHP 的风格在里面。我个人比较偏向简洁一点的，所以现在这个项目先用这个写，自己写全栈顺手就好。

此外还有人推荐 swig（源自 jinja 风格）、Handlebars，我还未仔细去了解。


### 其他的东西

知乎的问题中，看到一个对于业务逻辑的解释，很不错：

> 基本上我们写代码只写有变化的代码，而尽量不写机械性重复性的代码，其实后面我们就会知道，这就叫专注于业务逻辑，所谓业务逻辑就是你这个项目中，与别的项目都不一样的地方，必须由你亲自去编写实现的部分。
>
> [Spring，Django，Rails，Express这些框架技术的出现都是为了解决什么问题，现在这些框架都应用在哪些方面？ - 回答作者: Intopass](http://zhihu.com/question/25654738/answer/31302541)

## 碎碎念

最近 Twitter 加载很慢，而这两天注意力都在新项目上，今天打开，才看到两天前 Nitish 给我的私信，祝贺我的 Repo 有辣么多的 Star。

其实从一开始有一两个 Star 就开心不已，到现在已经有些麻木了，只看着那些数字增长，心里会期待，不过没有最初最初的期待感那么强。现在主要担心的是，我什么时候可以完成所有的文章呢。

20 多天前，JS30 的项目刚开始，我点进 Wes Bos 的 Repo 里看到了 Nitish 写的 Guides，然后我就觉得这个是一个不错的输出方法，还可以顺便监督自己的学习效果，但是担心自己水平不够，写文章占据太多精力，于是就问了问他每篇得写多久。意想不到他火速回复，根据项目难度三十到四十分钟不等。这又让我惊呆了，这么少~好的，那我也尝试写一写。于是得到了他的鼓励。

嗯，之后就是基本每两天一篇的频率开始看视频、查资料、写文章，有时候完全不知道该怎么下笔，也会去问 Nitish，他也会给出他的经验和方法。真心的特别感恩他回复给我的私信，要不是他回复了我，我现在恐怕还沉浸在自我怀疑中。和他私信的时候，每次我都感叹自己英语水平太菜，翻来覆去只会说 Thank 的衍生词，说得自己都看不下去了，于是找了一篇如何用英文感谢的文章来照葫芦画瓢，或许等我写完所有的指南，那篇文章也可以被我实践完了。

大大的感恩啊。



想起来还有一点补充，今天看了 Sherlock Holmes 第四季第二集，比第一集带给人的惊喜要多得多，特别是最后，很让人意想不到，此前一直没有关注到她，也看不出来，竟然是一个人。这一集是魔法特写的剧本，和上一集即是分离也有联系，之后或许还会看几遍，期待下一集。好啦，晚安。