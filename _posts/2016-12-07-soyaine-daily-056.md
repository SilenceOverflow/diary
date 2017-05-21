---
layout: background
title: "所丫日报" 
date: 2016-12-07 
category: soyainedaily 
excerpt: ""
---

## 学习笔记

### Liquid 模板语言

在把模板和 Jekyll 结合起来的时候需要用到这个语言，简单学习了一下语法，下面是我犯的一些错误。

受以前写 JSP 的影响，最开始我把标记符号错写为了 `<% %>`，字符串直接未解析就显示在 HTML 上，后来意识到正确的写法是 { }，它在 Liquid 进行语法解析时是用正则获取，在 Markdown 文件中直接写相应的代码会报错，下面的错误信息中 `%` 两侧的点号是我加上去的。

```
Error: Liquid syntax error (line 7): Tag '{.% %.}' was not properly terminated with regexp: /\%\}/
```

Liquid 里有 Filter 可以处理字符串，需要显示每一篇文章的日期和编号，用了下面的语句来实现，我去掉了花括号：

`````liquid
page.id | slice: -3, 3  // 从字符串末尾开始
page.id | slice: 14, 10  // 第二个指截取长度
`````

在处理每篇文章的链接的时候，使用了其中的 `replace` 来替换分隔符以便于创建 `Date` 对象时使用，以及用 `strip` 来去除空格：

````liquid
post.date | replace: '-', '/' | replace: '/0', '/' | slice: 0, 10 | strip
````

参考文档：

- https://help.shopify.com/themes/liquid/
- http://jekyllcn.com/docs/variables/

## 整理思考

一个写公众号的前辈想要了解一下大学生是如何了解技术信息的，我先思考一下我在学校时主要获取信息的渠道，方便整理回复。

- GitHub —— 搜索用，会搜一些项目，在做的时候如果用到会去相关的库。然后有很多人整理了很多资料，通常这里是第一手的，可以看到别人的代码是如何组织如何写的。
- Twitter —— 关注一些相关的人和组织，主要是可以关注到一些作者，每个语言都有自己的社区，可以了解到最新出现的有意思的变化
- 知乎 —— 关注了一些知乎上前端方向的人，看看他们的回答，但是手机上卸载了 APP 之后就很少去看了，知乎信息太杂，适合放松的时候扩宽视野，但培养技术能力不如看书。
- 知乎 Live —— 技术方面的一些分享
- StackOverflow —— 搜索用
- 书 —— 入门学习时的材料
- Coursera —— 有些地方有难点的时候去找相关的课程来听一听
- Medium —— 偶尔会读一读一些文章（频率挺低）
- 技术大会及分享 —— 有不同形式，线下的遇到有学生票或者有读者优惠的时候会去参加一些，但我比较宅，只参加过几个 InfoQ 、CSDN；线上的免费直播的质量可能不是很高，听过 AWS 和阿里技术论坛的技术分享，但是有些枯燥不太能全神贯注听下去。
- 社群 —— 一些技术社群，目前我只参加过池老师组织的攻城狮群，几乎每月都会请来一些技术上的大牛来群里分享，同时还会有社群内部的小伙伴们的工作经验分享，有的会反复的听很多遍。这是目前我加入的唯一一个技术社群，也是我觉得技术质量最高的。
- 公众号 —— 这个是效率最低的，关注了不少的公众号，但是我基本上只会读那些个人运营的公众号，也就是带有个人色彩比较浓的。而以前端为主题的公众号，很容易发现同一篇文章就被几个公众号之间转来转去，很明显不是第一手的资料，而这些文章，源头可能是在某些社区，比如掘金的专栏作家，或是某个技术大牛的个人博客。像 InfoQ 这样质量比较高的文章在移动端又很难读下去，我通常是在需要研读的时候保存到印象笔记里，然后分段一点点的啃下来。
- 设计相关 —— 偶尔去逛一逛 CodePen、Dribble 会遇到很多有意思的设计
- 即刻 —— 作为被动接收信息的主要来源，我关注设计相关的主题，此外会关注 V2EX 的招聘信息，帮助我偶尔看看别人的招聘需求是什么样的。
- 线上社区 —— 比如 DIV.IO 这样的专业技术社区，利用率很少，这可能是我现在做得不足的地方，偶尔去逛一逛可能是会有不小的收获的。
- 邮件订阅 —— 很少会打开来看，所以几乎可以忽略

以上整理形成[文章](http://www.jianshu.com/p/72e7c334d977)。

其他：卷福在 BBC 朗读的小说 http://www.bbc.co.uk/programmes/b007k3r4