---
layout: post
title: "所丫日报" 
date: 2016-12-22 
category: soyainedaily 
excerpt: "学习笔记"
---

## 学习笔记

### `forEach` 的用法

我用这个是不成功的：

```javascript
 inputs.forEach( input => function(input) {
	  input.addEventListener('change', handleUpdate)
  });
```

但是修改成这个就可以添加事件监听成功了：

```javascript
 inputs.forEach( input => input.addEventListener('change', handleUpdate));
```

这是 ES6 的新语法中的写法。上面这个语句类似于：

```javascript
// ES5
 inputs.forEach(function(input){
	input.addEventListener('change', handleUpdate);
 });
```


	