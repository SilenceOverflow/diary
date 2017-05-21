---
layout: post 
title: "所丫日报"
date: 2016-05-06
category: soyainedaily
excerpt: "学习笔记，观剧心得，读书心得"
---

## 学习笔记 IFE

### 设置两列表格的不同对齐方式

在  stackoverflow( [How to apply text-align left in the first column and text-align right in the others](http://stackoverflow.com/questions/11984767/how-to-apply-text-align-left-in-the-first-column-and-text-align-right-in-the-oth)) 上看到两种不同的解决方式，应用如下：

第一个用了 first-child ，注意到这里是 ``td:first-child`` 而非 ``tr:first-child``，这里就要注意 first-child 的意思：

> E:first-child  
>
> Matches element E when E is the firstchild of its parent. 

我最开始理解成为了选择 E 的第一个子节点，但其实是选择作为第一个子节点的 E。

```
table.twocolumn td:first-child {
    text-align: right;
}
table.twocolumn td {
    text-align: left;
}
```

第二种方法，用了 + 来选择  sibling node，和上一种的思路正好相反。

```
table.twocolumn td {
    text-align: right;
}
table.twocolumn td + td {
    text-align: left;
}
```

另外这里我用 ``table.twocolumn`` 是选中 table 中 class 为 twocolumn 的节点。

### CSS 里 Child vs Descendant selectors 的区别是什么？

[CSS Child vs Descendant selectors](http://stackoverflow.com/questions/1182189/css-child-vs-descendant-selectors)

> Just think of what the words "child" and "descendant" mean in English:
>
> - My daughter is both my child and my descendant
> - My granddaughter is not my child, but she is my descendant. 

一个是指直接后继，另一个是指所有后继。

CSS selector 中 child 用 > ，descendant 用空格，速度上 child 要快于 descendant：

> E F   Matches any F element that is a descendant ofan E element.
>
> E > F  Matches any F element that is a child ofan element E.

### 解决问题

1. 设置两列表格的不同对齐方式：CSS Selector
2. 调整确认提交按钮的高度：因为 body 设置了 padding，所以重新在此处将 padding 设小一些
3. table 内部的线条样式：一直在 table 中改没有作用，最后发现应该在 td 改才行。
4. [待解决]input 框有的边无法完整显示

## 观剧心得

天知道我这是看第几遍《琅琊榜》了，现在已经是不抱任何目的地看。今天以感冒不舒服需要休息为借口，静下心来认真看了几集，现在的眼睛开始能注意到那些奇奇怪怪的地方了，比如画面颜色的突变、背景人的表情、演员的站位妆容、房间院落的装修、道具的布置……以及此前看的时候不会记住的，回头来再看才能发现的伏笔。

## 读书心得

|2016-05-06-19:13

何夕-《伤心者》

《伤心者》是一篇很短的科幻，放在《伤心者》这本书的第一篇。讲的是一个数学系硕士何夕花了很多年时间在当时那个时代没有人能理解的理论上，最后疯了。当然精髓不在于此，故事是以后来人的角度去看、去描述的， 150 年后的诺贝尔获奖者在台上讲述这个故事，包含科研的辛酸苦楚。

故事让我联想到王一生的妈妈为他磨的那副棋，何夕的妈妈从来都坚信自己的孩子是最棒的，在这一点上她又何尝不是另一个何夕，以至于她在儿子出书之后欣喜若狂，甚至被当做疯子也要把书硬塞到各个图书馆，只为不让孩子失落，也是由此才留下了对 150 年后的人珍贵无比的资料。

百年之后世人感激她出自母爱的举动，二十年未开口说话的何夕却在母亲离世之后喃喃「妈妈」二字，这番亲子相依，在理论的世界里也足以让人动容。

《爱别离》是第二篇，刘慈欣评论这本书是压垮泪腺的最后一根稻草，但我却是看到这第二篇才开始掉眼泪。美与丑、善与恶往往被放在了一起，但当这些交汇的时候，冲突产生了，泪点也来了。

叶青杉的血液突变让他虽感染了 HIV 却不发病，叶青杉的血液从此变成了宝贝，有人想要他的血，有为科研的、有为保命的。而被他传染了的妻子林小菲却只是普通的感染者，生命一步步的被病毒所吞噬。两人间的爱情也在这个过程中慢慢感人起来。

其实从叶青杉被科研团队带走，他就几乎没有和林小菲再说过话，期间他去看过她一次，后来就再也得不到准许出去。住院的林小菲情况越来越差，叶青杉对她的愧疚感也有增无减，后来忍不住自己逃了出去，几经波折见到了早已「面目全非」的妻子，准备换血给她之时看到了她写的信，这大概是他们这么久以来唯一一次交流，还是通过书信的形式。也是这封信，将林小菲的善良展现了出来，她相信叶青杉，知道他会做但不希望他做出傻事（换血），因为这关系到人类的对抗 HIV 的进程。这就是泪点。

2016-05-06-20:19|

