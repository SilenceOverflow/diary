---
layout: post
title: "所丫日报" 
date: 2016-12-25 
category: soyainedaily 
excerpt: ""
---

## 闭包相关的例子

### from 秋风

```js
function love(name) {
	var text = 'hello' + name;
	var me = function () {
		console.log(text);
    }
	return me;
}
	var loveme = love('WIND');
	loveme();
```	
	
### closure.js

```js
(function() {
function A(a, b, c) {
	var ar = [a, b, c];
	return function B(i) {
		return ar[i];
    };
}

var b = A('Here', 'I', 'am');
console.log( b(1) );

})()
```

### StackOverflow
 I would simply start with: closures are a neat way of dealing with the following two realities of JavaScript: 
 
 1. scope is at the function level, not the block level and, 
 2. much of what you do in practice in JavaScript is asynchronous/event driven. 
 
 其中有一个回答非常可爱，用了一个公主的比喻，让我联想到了堂吉诃德。
 
 https://developers.google.com/analytics/devguides/collection/analyticsjs/using-plugins
 
 