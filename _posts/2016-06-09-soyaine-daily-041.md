---
layout: post
title: "所丫日报" 
date: 2016-06-09 
category: soyainedaily 
excerpt: "学习笔记 JavaScript下拉框选值"
---

## 学习笔记

JavaScript 获取 option 内选中值时，思路是先获取 option 中选中值的索引，再由此定位到 option 数组里，通过 value 或者 innerText（注意大小写） 来获取具体的值。

比如我的数组 id 为 "select-test"，那么我可以写下面的代码：

``` javascript
var selectOption = getElementById("select-test");
var selectText = selectOption.options[selectOption.selectedIndex].innetText;
var selectValue = selectOption.options[selectOption.selectedIndex].value;
```

