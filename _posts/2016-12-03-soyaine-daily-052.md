---
layout: background
title: "所丫日报" 
date: 2016-12-03 
category: soyainedaily 
excerpt: ""
---

## 练习笔记

### 事件处理

试图自己获取 DOM 元素作为参数传递，但事件处理无法按预期进行，最后又发现问题是事件的参数问题。

`addEventListener` 中的 `function` 的参数是触发事件的 `event` 对象。但无论使用 DOM0 级还是 DOM2 级的方法，都会将此对象传入事件处理程序中。