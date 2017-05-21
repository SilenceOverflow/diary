---
layout: post
title: "0320-生活小记录吧" 
date: 2017-03-20 
category: soyainedaily 
excerpt: "据说今天是国际幸福日，召唤了一次图片精灵"
---

## 生活瞎想

据说今天是国际幸福日，然而真正幸福的人，是不需要有个日子来提醒自己幸福这个概念的。以后的世界，会不会无论大事小事，都有一个特定的节日来纪念？尽管这其中的有些节日，又更进一步，从原本的纪念变成了消费的纪念。

近来的雾霾又将要持续一周，这时候我才开始注意到了，前不久那些清澈（原谅我想用这个词）的天空是多么的难得，那时的空气回归本身，消失在了视线里，也不知不觉间让人忽略了它的存在。失去要比拥有更容易让人成为诗人。

昨天新发现了一首叫《借我》的歌，最先看了 MV，是一个很年轻的姑娘，歌词、声线、吉他我都很喜欢。后来听着听着能恍惚听出《漂洋过海来看你》的味道，特别是下面男声版，这就是没有音准的人总会出现的幻觉。（因为版权问题，只能把这首翻唱的生成外链，但是我还是喜欢原版）

<p>
<style>
.img {
	width: 340px;
	height: 80px;
	content: "";
	display: inline-block;
	background-image: url('http://wx4.sinaimg.cn/mw690/e7947806ly1fdtcta6btsj20hs0bv3ze.jpg');
}
.img.nth {
	background-position: 10px -60px;
    background-size: 90%;
    background-repeat: no-repeat;
}
</style>
<span class="img nth"></span>
<embed src="//music.163.com/style/swf/widget.swf?sid=423104390&type=2&auto=1&width=320&height=66" width="340" height="86"  allowNetworking="all" style="margin: 0 auto 0 auto; display: inline;">
</p>

>*《借我》- 谢春花*  
借我十年   
借我亡命天涯的勇敢  
借我说得出口的旦旦誓言  
借我孤绝如初见  
借我不惧碾压的鲜活  
借我生猛与莽撞不问明天  
借我一束光照亮黯淡  
借我笑颜灿烂如春天  
借我杀死庸碌的情怀  
借我纵容的悲怆与哭喊  
借我怦然心动如往昔  
借我安适的清晨与傍晚  
静看光阴荏苒  
借我喑哑无言  
不管不顾不问不说  
>也不念  

所以想慢慢读书，享受那种一点一点滴水穿石的岁月感，这也是一种淡淡的幸福。

## 学习手记-图片精灵

所以为了弄出上面那张图片，用了以前只闻其名的图片精灵（CSS Sprites）。基本思想就是把需要的图片作为某个元素的背景，设定好所需的大小之后，用背景的 position 来实现只显示大图中的某个部分，此时还可以通过 `background-size` 来改变背景图片的大小。

这有点像在某个开了小口的玻璃板背后放了一张图，然后通过移动这张图，让在玻璃板之前的人看到其中的某一部分。此处我的语句如下：

```html
<style>
.img {
	width: 340px;
	height: 80px;
	content: "";
	display: inline-block;
	background-image: url('http://wx4.sinaimg.cn/mw690/e7947806ly1fdtcta6btsj20hs0bv3ze.jpg');
}
.img.nth {
	background-position: 10px -60px;
	background-size: 90%;
	background-repeat: no-repeat;
}
</style>
<span class="img nth"></span>
```

很奇怪，以前乍看一眼觉得有点麻烦没有花时间深究的东西，如今看来却不是那么回事了，或许可以把这叫做知识的力量？(*╯3╰)