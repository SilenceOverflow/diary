---
layout: post
title: "所丫日报" 
date: 2016-12-31 
category: soyainedaily 
excerpt: "关于 GitHub 图片加载的问题手记，关于 HTTP header 中的 Content-Length"
---

## 关于 GitHub 图片加载的问题手记

在 GitHub 的 README.md 文档里有的图片无法显示，我换了很多图片都无效，于是去查了一下原因。

[https://help.github.com/articles/why-do-my-images-have-strange-urls/](https://help.github.com/articles/why-do-my-images-have-strange-urls/)

所有上传到 GitHub 的图片都会经过 Camo 的处理，以 SSL 的形式改变其 URL，这是出于安全的考虑，防止信息被跟踪。所以在 GitHub 上的图片会被转化成这样：

```html
<img 
src="https://camo.githubusercontent.com/ae881a1274370b23bcd0cf8eb677ce104aa1764b/687474703a2f2f6f666a6b75376d6c6d2e626b742e636c6f7564646e2e636f6d2f53637265656e2532307265636f7264696e67253230323031362d31322d3330253230617425323030392e30312e3134253230504d2e676966" 
data-canonical-src="http://ofjku7mlm.bkt.clouddn.com/Screen%20recording%202016-12-30%20at%2009.01.14%20PM.gif" 
style="max-width:100%;">
```

这是我写的一个 README.md，其中的 `data-canonical-src` 才是我图片的源地址。但是在 GitHub 上无法显示图片，点击图片链接后提示 Content length exceeded，看来是图片太大了，这一张 GIF 有 10M，那图片限制到底是多少呢？查了一下源代码。

```js
// https://github.com/atmos/camo/blob/master/server.coffee#L18

content_length_limit = parseInt(process.env.CAMO_LENGTH_LIMIT || 5242880, 10)
```
所以 5242880 换算一下得到的内容限制是 5MB。

## 关于 HTTP header 中的 Content-Length

上一部分中 5242880 是指的 HTTP Response Header 中的 content-length，在 Chrome 中可以查看如下：

![HTTP Response Header](https://cl.ly/2v2q0L2I2h02/Image%202016-12-31%20at%209.51.36%20AM.png)

关于 Content-length 的细节，看了一些相关的问答（[What's the “Content-Length” field in HTTP header?](http://stackoverflow.com/questions/2773396/whats-the-content-length-field-in-http-header)）

> The Content-Length entity-header field **indicates the size of the entity-body**, in decimal number of OCTETs, sent to the recipient or, in the case of the HEAD method, the size of the entity-body that would have been sent had the request been a GET. 
>
> from [https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.13](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.13)
>
>If a Content-Length header field (section 14.13) is present, its decimal **value in OCTETs represents both the entity-length and the transfer-length.** The Content-Length header field MUST NOT be sent if these two lengths are different (i.e., if a Transfer-Encoding header field is present). If a message is received with both a Transfer-Encoding header field and a Content-Length header field, the latter MUST be ignored.
>
> from [https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.4](https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.4)

其中有两个概念需要区分一下：

- OCTET：指计算机中的八位字节数，也就是等于 8bit 大小的数据。（any 8-bit sequence of data，[from w3.org](https://www.w3.org/Protocols/rfc2616/rfc2616-sec2.html#sec2.2)）
- Byte：指最小的可寻址的存储单元，1Byte 并不一定都等于 8bit，这和所处的体系架构有关。

不同的 Header 类型如下：（[https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2](https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2)）

- Message Headers ( Header Fields )
	- general-header
	- request-header
	- response-header
	- entity-header
	
区分另外两个概念：

- message：HTTP 协议通信中的基本单位，分为 Request 和 Response 两种。
- entity：如果 HTTP-message （不都会有）有一个 message-body 的话，那么也有 entity-body，此时这两者相等。但如果 HTTP 传输过程中进行了 Transfer-Encoding 的话，这两者会有差异。

以上参考：

- [http://stackoverflow.com/questions/2273837/which-one-is-the-message-and-which-one-the-entity-in-http-terminology](http://stackoverflow.com/questions/2273837/which-one-is-the-message-and-which-one-the-entity-in-http-terminology)
- 《图解 HTTP》p.44






