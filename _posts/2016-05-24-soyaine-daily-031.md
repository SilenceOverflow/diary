---
layout: post
title: "所丫日报" 
date: 2016-05-24 
category: soyainedaily 
excerpt: "关于日报，学习笔记，其他想法"
---

## 关于日报

我用 Python 写了一小段代码，为了写日报的流程更简单一些，代码帮助我做的事情有：

1. 获取当日日期—— `time.localtime()`
2. 创建有特定格式文件名的 Markdown 文件 —— `time.strftime()`
3. 自动添加 jekyll 所需的文件头
4. 设置了开机启动-文件夹——在 ..\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup 里添加快捷方式即可

所以现在我每天写日报的操作就是：开机（_post 文件夹自启动）→ 双击 .py 创建当日新日报 → 双击文件 → 写。

不得不说，前面 30 篇，我都是每天复制粘贴一份文件，修改文件名和文件里的日期，删掉上一份日报的内容，开始写。

完整代码如下：

``` python
# -*- coding: UTF-8 -*-
import codecs
import time
date = time.strftime("%Y-%m-%d", time.localtime())
days = time.strftime("%j", time.localtime())
count = int(days) - 114
filename = date + "-soyaine-daily-0" + str(count) + ".md"
with codecs.open( filename , "w", encoding="utf-8" ) as f :
         f.write("---\nlayout: post\ntitle: \"所丫日报\" \ndate: " + date + " \ncategory: soyainedaily \nexcerpt: \"\"\n---")
```

因为写得很简单，还有很多我没有实现的，比如：

1. 当天第一次开机时执行创建操作
2. 创建文件之后，在 Windows 系统中打开 Markdown 文件。（这个我没有找到解决的办法，如果可以，便能和上一步结合起来完成了）
3. 自动生成摘要
4. 自动同步到 GitHub

但目前的改进，可以帮助我，在打开电脑的时候就提醒了自己要写日报，这样无论我做什么、看到什么、刷什么，想记录的东西都能很方便的记录下来。也不用我在临睡前才慢慢的去一点一点回想、粘贴。(以上从开始鼓捣 Python 代码到写完这段花了 1h 48m 15:06)

## 学习笔记

### transparent border with background-clip

这是查 transparent(透明) 时查到的内容，一篇文章 [Transparent Borders with background-clip](https://css-tricks.com/transparent-borders-with-background-clip/)，关于如何实现透明边框，可以使用 CSS3 的新特性 `background-clip` 。 

实例是这样，`border: 20px solid rgba(0,0,0,0.3)`

这里的 rgba 的最后一个数字用于设置透明度，取值为 0~1，但要想实现边框的透明效果，单靠上面这一句是不够的。

这时再加一句 `background-clip: padding` 则可以实现相关的效果。

## 其他想法

在群里见识了同龄人的优秀，觉得又鼓励自己去好好的花心思改简历和练技术了。以及早读君分享如何积累项目经验。

今天听了王勇睿（老师？）的分享，下载下来听了第三遍了吧？他讲的几个故事，一个是坚持的。对于我自己，现在也是该沉下心来去进行刻意练习的时候。唯有行动而已。