---
layout: post
title: "所丫日报" 
date: 2017-01-03 
category: soyainedaily 
excerpt: ""
---

## 统计公众号数据

话说手里拿着锤子，看见什么都是钉子。今天有人通过我的 GitHub 关注了我的公众号，这还是第一次有人通过这个途径关注，惊喜之余看了看微信公众平台，就手痒想要用那天新学的办法统计一下去年的数据。

首先分析了一下数据部分的 HTML 结构：

```html
<div class="appmsgSendedItem multiple_appmsg">
        <a class="title_wrp" href="http://mp.weixin.qq.com/s?__biz=...mid=...;idx=1;sn=....chksm=...#rd" target="_blank">
            <span class="icon icon_lh cover" style="background-image:url(https://mmbiz.qlogo.cn/mmbiz_jpg/...);"></span>
            <span class="title">[图文1]元学习课程的回顾和总结</span>
        </a>
        <div class="desc">
            <div>
                <span>阅读 112</span>
                <span>点赞 9</span>
            </div>
        </div>
</div>
```
	
所以主要的数据：
	
```
.appmsgSendedItem.multiple_appmsg （此处我忽略了只发图片的消息）
	.title_wrp 文章链接
		.cover 题图
		.title 文章标题
	.desc 点击数据
		span 阅读
		span 点赞
```

```js
var articles = Array.from(document.querySelectorAll('.appmsgSendedItem.multiple_appmsg'));
var data = [];
articles.map(item => {
	const article = {};
	article.url = item.querySelector('a.title_wrp').href;
	article.img = item.querySelector('span.cover').style["background-image"];
	article.title = item.querySelector('span.title').innerText;
	const visit = item.querySelectorAll('div.desc span')[0].innerText.replace(/[^0-9]/g,"");
	const like = item.querySelectorAll('div.desc span')[1].innerText.replace(/[^0-9]/g,"");
	article.visit = parseInt(visit);
	article.like = parseInt(like);
	data.push(article);
	return article;
});
JSON.stringify(data);
```

忘了日期重新修改一下，发现这里竟然可以用 `[id]` 来表示具有 id 属性的元素选择符。

```js
var articles = Array.from(document.querySelectorAll('tr.mass_item[id]')); 
articles = articles.filter(item => {
	return item.querySelector('div.multiple_appmsg');
});
var data = [];
articles.map(item => {
	const article = {};
	article.title = item.querySelector('span.title').innerText;
	article.time = item.querySelector('p.mass_time').innerText;
	article.url = item.querySelector('div.multiple_appmsg a.title_wrp').href || "";
	article.img = item.querySelector('span.cover').style["background-image"];
	const visit = item.querySelectorAll('div.desc span')[0].innerText;
	const like = item.querySelectorAll('div.desc span')[1].innerText;
	article.visit = visit.replace(/[^0-9]/g,"");
	article.like = like.replace(/[^0-9]/g,"");
	data.push(article);
	return article;
});
data.sort((a, b) => {
	return a.time.replace(/[^0-9]/g,"") - b.time.replace(/[^0-9]/g,"");
});
JSON.stringify(data);
```

<script>
var data = [
 {
  "title": "[图文1]今天没有更新",
  "time": "2016年11月16日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271053&idx=1&sn=f526110027ea79f536f0b29d5908d2d5&chksm=8fd24300b8a5ca16302f4f19ba5d52acf806c8d1a1dc7c3f0ccf6eff7b73db7ad169966fe972#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4sebcX73xZjH9StQeY8Tn6vdRKVPlzzph97JjttIZW8zepWQfaRC7PsDh4n8pmnen1adbYbP2u5vng/0?wx_fmt=jpeg\")",
  "visit": 37,
  "like": 7
 },
 {
  "title": "[图文1]元学习课程的回顾和总结",
  "time": "2016年11月11日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271049&idx=1&sn=3fb659ecf286b153a6052492a432cda5&chksm=8fd24304b8a5ca12b79e0a4af1d24b6376306126ef8fde6295fca7fec7a7c4037b5f7b50e93b#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4sf31JUqrjic5s70cUUoV2BKKKwyicqzLuS9nwqPgvepib5T9VeHnWTnHicLNZrw4Dx9ict1Bu6mbvJGQdA/0?wx_fmt=jpeg\")",
  "visit": 113,
  "like": 9
 },
 {
  "title": "[图文1]xRite 的元学习课程回顾和总结",
  "time": "2016年11月10日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271040&idx=1&sn=b3395400898b204b0f26c913fb6bb3bc&chksm=8fd2430db8a5ca1bc6db446f6aedef704516e91574c80cbfa2ef42ef754ffb04ad17801c357d#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4sf31JUqrjic5s70cUUoV2BKKKwyicqzLuS9nwqPgvepib5T9VeHnWTnHicLNZrw4Dx9ict1Bu6mbvJGQdA/0?wx_fmt=jpeg\")",
  "visit": 1,
  "like": 0
 },
 {
  "title": "[图文1]呓语 | 草木黄落兮雁南归",
  "time": "2016年11月02日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271037&idx=1&sn=74c9da72abdce6b59ab9900e39a39474&chksm=8fd24370b8a5ca667f7b191cf4196057ae7f93b7598d7a6ffadbd0ed031f618c81b145ecfc8c#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4sdDNuJzd68LWicBUzUcQ17oicc076Bibkh1Mp1M7OOlngsrrcpLz3Fye8beu32hWNfQDgvPH85GOicficA/0?wx_fmt=jpeg\")",
  "visit": 28,
  "like": 9
 },
 {
  "title": "[图文1]这不是一篇文章",
  "time": "2016年10月26日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271033&idx=1&sn=9b3487d146d68466a93306c4fe7073c6&chksm=8fd24374b8a5ca620ab6ae54850e9235099d41616ed8125515d3aa6868682fecc935a10f894a#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4scvMIdHzT94iahC7X3CFo9jtsoqNGvAa6Y5d4thiaBpPvbUMJ9ac8jeNxl1xYWn2C15YwK91xjd0zUQ/0?wx_fmt=jpeg\")",
  "visit": 26,
  "like": 5
 },
 {
  "title": "[图文1]我所向往的匠心",
  "time": "2016年10月19日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271029&idx=1&sn=9d5e2decdc810a6408b99b73406edfb5&chksm=8fd24378b8a5ca6ea06a9a04b9e1a8e698086bea09f642e8fc0d66fffa53982b84d7829c6f75#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4sdOOeRuteZPAMibdBxYEmiar4wTS5UoYJHx0xml3bkfUQDcqyVYu1ICN3niaibj34H7FfqjicibE5pNkqRg/0?wx_fmt=jpeg\")",
  "visit": 26,
  "like": 6
 },
 {
  "title": "[图文1]札记 | 与自己内心的非暴力沟通",
  "time": "2016年10月12日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271024&idx=1&sn=1e236b6d5ea17d9accb7f589f68e7def&chksm=8fd2437db8a5ca6b33a2fa58102e0ab0a11ab829fcf060ff1145c510e21a6c561aa996de010e#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4seYJhnCBxWCqZvNjySia4dRUcDGjRHPa4mnWDme7d5icBgr3UbYIIaI2v5xkUMJJs3fvZW4sySWHU6g/0?wx_fmt=jpeg\")",
  "visit": 50,
  "like": 12
 },
 {
  "title": "[图文1]不热闹的深夜独白",
  "time": "2016年10月06日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271021&idx=1&sn=8b0cd7e78650a5b678ec6de561a7d4d8&chksm=8fd24360b8a5ca760930196c3e4832d86b2012b6f7a3bc57e500428d02bc370523cff88b492d#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4seicg5FficD8h3WT0kjJN1uw1rNtdic0Wia6I2O5jcKaBLIYAibdf27y2hLsVCjnicuwbye89ibLDVuVwHPg/0?wx_fmt=jpeg\")",
  "visit": 32,
  "like": 10
 },
 {
  "title": "[图文1]札记 | 一把名为“泪”的茶勺",
  "time": "2016年09月29日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271018&idx=1&sn=1197820b7a62bcb08a928a5e77dee0e0&chksm=8fd24367b8a5ca7168483b5486cc33bc14f9f62700f4157ed4b8720404ab01bf7e3293052449#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4scEVspFJatUiceDcsckpqaTcQWc5h6Qib3ogQeo6fSVLUvsUvkcsKds2aolRINQX560uVtiaBHFuzicvA/0?wx_fmt=jpeg\")",
  "visit": 32,
  "like": 9
 },
 {
  "title": "[图文1]札记 | 杯水之间，狂波巨澜",
  "time": "2016年09月22日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271014&idx=1&sn=bdcdce8519cec0584cc19460fb195cdd&chksm=8fd2436bb8a5ca7dc6a40153a5167b03c0a3eb9d4b8bab535727f63d47a5bff97b4801feaf89#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4seHW2UiaXEltHvvjYaDtYvENkbeTmn5hnsAtk7uAafSqSefiaZjlevkiaIiaXBn1yDkLV3cGDvmVok6Lw/0?wx_fmt=jpeg\")",
  "visit": 48,
  "like": 7
 },
 {
  "title": "[图文1]日记的无用之用",
  "time": "2016年09月14日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271007&idx=1&sn=64865a33abce6ebe376d6c1a5a59e44d&chksm=8fd24352b8a5ca44b4a6bd606b15b55db29d30943a342f2390118e007ad094785c731f283645#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4sePF3fDsj7upHw6Fh6PWk3O4lqqol1ACpHe38BGZXl32XQaZfcXmlBrIpMMZn7t0aibZI1HjtGa5oQ/0?wx_fmt=jpeg\")",
  "visit": 81,
  "like": 14
 },
 {
  "title": "[图文1]遇上“我”，像遇上一朵雪花",
  "time": "2016年09月07日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650271003&idx=1&sn=fc3f7d057b6b00859e2d9ef8699ee290#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4sdqWNXos3NXbUPguMOuxrRiaUNj8sEyuhc8leBpWIrorSHSFTGFbqAHE059MTN9NJhdBicENRmYh69A/0?wx_fmt=jpeg\")",
  "visit": 42,
  "like": 7
 },
 {
  "title": "[图文1]苦难 · 生活 · 希望",
  "time": "2016年09月01日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270999&idx=1&sn=e2c814dbe782f4c51113dd50b322d36d#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4scFnhfKXzPQ4icE1PcKCAmowVR7MZc2ySGChpBOFzwoAlXibIiavvszCmNYkuCpkwZ9T4ldz8uN5IJmA/0?wx_fmt=jpeg\")",
  "visit": 34,
  "like": 6
 },
 {
  "title": "[图文1]札记 | 非黑即白与色彩斑斓",
  "time": "2016年08月25日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270996&idx=1&sn=210d8a806a63d140a71de231d9e6562a#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4scqUx7icctfaN3tibicBriasicYgiakmCSqX0X45IqmaP8icazYluUAXbsov2HoLdcsfWFY5YpztDU57pbJg/0?wx_fmt=jpeg\")",
  "visit": 44,
  "like": 4
 },
 {
  "title": "[图文1]札记 | 生活在信息时代的远古人",
  "time": "2016年08月17日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270992&idx=1&sn=bfe4420121f332d6ae43e505d650278d#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz_jpg/Penxjq6k4setggia2HGZ3ZHrM8ja4RTX6c7dNBGlq6n49PItEToz401csxkpibIfQ2DOUib8rxMHBjcejooQdTgYw/0?wx_fmt=jpeg\")",
  "visit": 56,
  "like": 4
 },
 {
  "title": "[图文1]札记 | 听说路漫漫，其修远兮",
  "time": "2016年08月11日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270988&idx=1&sn=7e46c3b14e4b4326005e9e757cd5814e#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sdfZzibHwmwZZ4TWhgV4klMq9KSHvNwD94l375zzb64XLutEudYk7Bod3owj1kjoNAz06OKribC5mhg/0?wx_fmt=jpeg\")",
  "visit": 24,
  "like": 6
 },
 {
  "title": "[图文1]生活只有一种英雄主义",
  "time": "2016年08月03日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270985&idx=1&sn=f90602b1af40ae2931d52e8e5da3d2a2#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sfRx57goDk9E38jakGhVLibDqeLxBW924YRqA2UIq74TII9xHg60PTJ5GPS0ujeRscLmJJGCuyyNBg/0?wx_fmt=jpeg\")",
  "visit": 22,
  "like": 5
 },
 {
  "title": "[图文1]札记 | 游走在死亡世界里的文学",
  "time": "2016年07月27日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270982&idx=1&sn=e16b9b9a1c1af9c9fcbc8cdf02f4b861#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sdqCQy0Z5RRJfG90RZ6nhxV2a07YaMibmjwBKxziaC7oZV4dMC1LyEbr2iczPxJ6ujtXicPbSlrqeCs5A/0?wx_fmt=jpeg\")",
  "visit": 47,
  "like": 8
 },
 {
  "title": "[图文1]札记 | 寻找命中注定的工作？",
  "time": "2016年07月13日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270977&idx=1&sn=86f595f0308aee49d15c8a982cc20d43#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4scEOEvXgcuLjxWVHjdwVdXa4rx6ibiaDI3mA30ZrwkXYxJqNEf2sKqmrZemsNPQgH254Vkv0D6R5UHA/0?wx_fmt=jpeg\")",
  "visit": 69,
  "like": 9
 },
 {
  "title": "[图文1]札记 | So Good They Can't Ingore You",
  "time": "2016年06月30日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270971&idx=1&sn=9f2e48a857f5e9768f0672f4c9dfddbe#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sez5B5HVeePlGqDNF7VcicGyMqZrMhxdeMjdt4zRMgsgxKoiaC36nZNTricraTb3NFnCGoSvfsZ6iawlg/0?wx_fmt=jpeg\")",
  "visit": 23,
  "like": 2
 },
 {
  "title": "[图文1]札记 | Find Mr.Right",
  "time": "2016年06月23日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270967&idx=1&sn=cbe27681a580ddd2f51e4a9b5aff407f#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sfKKwrhZQ2aQ3ibdvQbsoakaxvZOeHtyOE3YaMk7PAHvQU8geAu4R2m8paVjlYpq8FtttA6tv8bhxw/0?wx_fmt=jpeg\")",
  "visit": 18,
  "like": 2
 },
 {
  "title": "[图文1]新世相·图书馆的初次邂逅",
  "time": "2016年06月16日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270959&idx=1&sn=c48f52a9a471034581c71473f651297e#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sfblCToFmLKdBibDkOCSiakQ2htibwia8KjDn7Xmhic6Tbdrow66ZhQR3yfD6rGtNILACaH5ibntrr0oncA/0?wx_fmt=jpeg\")",
  "visit": 58,
  "like": 8
 },
 {
  "title": "[图文1]呓语 | 青春疯狂，可还在回望？",
  "time": "2016年06月09日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270956&idx=1&sn=bc130a1b03bfa49bf5058b29552852e6#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4seCpAY37icImibM2ZZwcryFrJLicG97ts2GBbpDBChucaxuaJV9D54qibAgZh4HTwVn5Qd22wt0odT6uA/0?wx_fmt=jpeg\")",
  "visit": 16,
  "like": 5
 },
 {
  "title": "[图文1]呓语 | 谁对谁错，谁真谁假？",
  "time": "2016年06月02日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270953&idx=1&sn=5274a989b2973f51d8d3e63c09714f51#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4scZ5ln04ic13lkLic8Jbx617g15CmQlFnbbJJybhNtndrVIDq3o7ruMC1BadmGTOB0Ribm3UpkKmpoxw/0?wx_fmt=jpeg\")",
  "visit": 22,
  "like": 4
 },
 {
  "title": "[图文1]纸质书的别样使用场景",
  "time": "2016年05月26日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270949&idx=1&sn=2bfe7c031da4e4528ca3c0703fd93952#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sfqPiccks6QmO8Ev5L255OwS8sggZ9rmCS1xYM0de3bt7JbF5PG6WdETjK4kxNs5ID4h9C8tQS7Gdg/0?wx_fmt=jpeg\")",
  "visit": 58,
  "like": 5
 },
 {
  "title": "[图文1]聊一聊我眼中的日本文化",
  "time": "2016年05月19日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270946&idx=1&sn=1e047e0806b586e30de8d8f1658fc050#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sf3wJaSfjyLahMGPv1mgGuBycLBSicvXSKWL5BL8wyoENnM8WPcA9BThicoiaCYcXQwvhk9caqf5yUVQ/0?wx_fmt=jpeg\")",
  "visit": 21,
  "like": 5
 },
 {
  "title": "[图文1]札记 | 初读《茶馆之殇》",
  "time": "2016年05月11日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270942&idx=1&sn=d12aed66589620a5ac85c32203ba1d34#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sdWoibYOgOh6ngEEMpzRRN5qUBJQHMdQiakMUXWGw93nickZ36WOic71m2dLjFBGtXCdoe8YicB5Tm78yg/0?wx_fmt=jpeg\")",
  "visit": 87,
  "like": 8
 },
 {
  "title": "[图文1]如何有策略的赞美和批评？",
  "time": "2016年05月05日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270936&idx=1&sn=e5babe4c0b318669504a24f273b9b918#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4seTFLtNlBStv6NichWtrd5J9QS6RvFN14ndrVE7kQz0Aqs76DVib3bUEXvFicvxIbpHFjN5ZfnV4aiadA/0?wx_fmt=jpeg\")",
  "visit": 40,
  "like": 6
 },
 {
  "title": "[图文1]问问时间都去了哪里",
  "time": "2016年04月27日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270931&idx=1&sn=3ff56eaf68f418a1cc75380ff9626402#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4seTSdbgfjekte7NyepAAziav4G3rK51yjMQRuKVGwcEXIasR137pDVoxPo0ehxeicUmQpwylgPWaBibA/0?wx_fmt=jpeg\")",
  "visit": 74,
  "like": 7
 },
 {
  "title": "[图文1]札记 | 一枚伪吃货的自我修养",
  "time": "2016年04月20日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270924&idx=1&sn=9ced83331d6633e10130379608ea0d7f#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sfr8ess2PlwDtyW55KSelyucTF7ibm6RFlRLykzSm8jeMJ5mib3A9K8sp31AwkPF2TMUTia2GCjxNgMA/0?wx_fmt=jpeg\")",
  "visit": 38,
  "like": 6
 },
 {
  "title": "[图文1]札记 | 为什么总实现不了美好愿望",
  "time": "2016年04月13日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270921&idx=1&sn=6fa044c8b4ad76a6641b4e02b69ebf22#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4scgicicrWYc4crd1vdHvb1FUq8rPpoDib1VD0GfgDwWQ4KYaOhDCIVPiaQjlnCzmeDXfOuwdVPk4WvE1A/0?wx_fmt=jpeg\")",
  "visit": 31,
  "like": 4
 },
 {
  "title": "[图文1]去回忆里，为青春上炷香",
  "time": "2016年04月06日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=2650270918&idx=1&sn=6454bed6ed2221ef5834daf848c7de30#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sfGrrCPonC2nqiaETyIicd7ib9rbeiaJnvdoYQJ5onLGkKg9V4mq0gXTgPTBJwnnkweQJfDesy0ROL1FA/0?wx_fmt=jpeg\")",
  "visit": 43,
  "like": 2
 },
 {
  "title": "[图文1]歪头看乡愁",
  "time": "2016年02月09日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=402014081&idx=1&sn=f9d35f66f6b985c4cc5981898e2a3eb5#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sd3GSv5FdHJ2nr7zsdRI7Z47R2AqgL04NudXIOpoiaAA9TnLshqBnRxUemJte4EiaStmhNztaJqVXrg/0?wx_fmt=jpeg\")",
  "visit": 27,
  "like": 2
 },
 {
  "title": "[图文1]最怕回忆突然翻滚绞痛着不停息",
  "time": "2016年01月31日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=401877631&idx=1&sn=70a28b8e3ccfc08fd01dfbc9cab5c362#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sdv9OHRvEgjZOuOQxDb2WYzQ1ts40AbOxyibO5hWYtp8jVsJGM4t25yj4iaqqyD8cFakywUv0uLDUDA/0?wx_fmt=jpeg\")",
  "visit": 37,
  "like": 6
 },
 {
  "title": "[图文1]致我们所缺少的匠人精神",
  "time": "2016年01月05日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=401555284&idx=1&sn=d28118ab9a35c1df584fe9820d06bd3d#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sdGFaLx8VdiblSzmghMus3AklSfQbNG90oQiabdmovf703FycICQdwbsIeaWwCpLwQYhmsa7IVEsITQ/0?wx_fmt=jpeg\")",
  "visit": 17,
  "like": 2
 },
 {
  "title": "[图文1]两个人说话 = 四个人交流",
  "time": "2016年01月04日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=401540274&idx=1&sn=90e95be8dd327a804e95656574d2493b#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sdVxzvvnJtP3xeKgj06o273ya104gApwy8OX8OzLTEFZp1ickocUdgzwZuRq03mYibcuPBdDNkDQhng/0?wx_fmt=jpeg\")",
  "visit": 24,
  "like": 0
 },
 {
  "title": "[图文1]这里最后的喜鹊是什么样？",
  "time": "2016年01月03日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=401522368&idx=1&sn=ac6a879afc312a1e900806e148f30413#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4seLItGKeqymy44ugQqTPaccTlIQwBOqLgLFTBhxJ1O89QNPYtluAA3Z3ZxWmficib07WmoTP8VQZbDQ/0?wx_fmt=jpeg\")",
  "visit": 10,
  "like": 0
 },
 {
  "title": "[图文1]关闭朋友圈只是开启改变的一种形式",
  "time": "2016年01月02日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=401509470&idx=1&sn=09f3c8179bbd7ed7d4864a8fd294e56e#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sdgakwakZjlrKImO5y22Lu6WrnzA2iaG4HOB5Z7NM99jnmrvz4s99Nob0454ToDY5R5N1Kof76Kkicw/0?wx_fmt=jpeg\")",
  "visit": 63,
  "like": 1
 },
 {
  "title": "[图文1]新年 · 用自己的节奏去长大",
  "time": "2016年01月01日",
  "url": "http://mp.weixin.qq.com/s?__biz=MzIyMDEwOTYwMg==&mid=401491291&idx=1&sn=216e5e21af23e891ccd2e52f47faa1d5#rd",
  "img": "url(\"https://mmbiz.qlogo.cn/mmbiz/Penxjq6k4sfOE1YtyOQIzTw9e6kx0IcEWDHSQnGU79YuhXX1cfoJGOZhKuxkwhbT9ECmkbpR8Y3COCWTFrJoSw/0?wx_fmt=jpeg\")",
  "visit": 22,
  "like": 3
 }
];
</script>

```js
data = data.map(item => {
	const title = item.title.replace("[图文1]","");
	const url = item.url;
	return `
		<li><a href="${ url }"> ${ title } </a></li>
	`;
});
data.join('');

```

把链接整理输出出来：（这里遇到了一个坑，我不小心把 JS 写在了 `<ul>` 标签前面，结果加载不出来，我在 Console 里面运行却没问题，后来才发现是这个问题）

<ul id="burenao">
here is the list of articles in 不热闹
</ul>

<script>
data = data.map(item => {
	const title = item.title.replace("[图文1]","");
	const url = item.url;
	return `
		<li><a href="${ url }"> ${ title } </a></li>
	`;
});

var list = document.getElementById("burenao");
list.innerHTML = data.join('');
</script>

哈哈，我可以为不热闹的文章们新安一个家了。另外在 Console 面板截了个图，除掉一篇删除的，去年一共推送了 38 篇文章，其中有两篇是好友友情支持的，还有两篇只写了几句话，剩下的 34 篇都是我原创完成。顺便附上 GitHub 的截图。

![2016 年的不热闹的文章数据](http://ofjku7mlm.bkt.clouddn.com/17-1-3/78346126-file_1483438759673_2378.png)

![2016 年的 GitHub 数据](http://ofjku7mlm.bkt.clouddn.com/17-1-3/48192782-file_1483438757303_13ffc.png)

