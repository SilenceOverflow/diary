---
layout: post
title: "0425 - 面试题" 
date: 2017-04-25 
category: soyainedaily 
excerpt: ""
---

### 笔试题目具体步骤的截图

#### Step1

Node.js server，[参考了简单示例](https://nodejs.org/dist/latest-v6.x/docs/api/synopsis.html#synopsis_example)

![Node.js server](https://cl.ly/3f0V0Q403Q3D/Image%202017-04-25%20at%206.07.38%20PM.png)
	
#### Step2

React:
![React](https://cl.ly/0P3U1z0G013h/Image%202017-04-25%20at%206.06.09%20PM.png)
  

Ant Desgin
![Ant Desgin](https://cl.ly/2v3K2X391743/ant%20design.PNG)
	
#### Step3

DatePicker：
![Date Picker](https://cl.ly/3K3B26361b0a/Screen%20recording%202017-04-26%20at%2012.38.44%20PM.gif)

核心代码[请见这里](https://github.com/soyaine/antd-react-app/blob/master/src/App.js)。

### 完成过程中遇到的问题

1. 在跑 [Webpack 的 demo](https://webpack.js.org/guides/get-started/#creating-a-bundle) 时，因为忘记在项目里 install webpack，导致 HTML 页面提示错误 `Uncaught SyntaxError: Unexpected token import`，最后查看 package.json 才发现这个问题。
2. 改变 React 运行的端口，参照了：
	- [Adding Temporary Environment Variables In Your Shell](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md#adding-temporary-environment-variables-in-your-shell) 中使用环境变量的写法。
	- [Advanced Configuration](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md#advanced-configuration) 中可选参数。
	```
	PORT=8080 npm start
	```
3. 运行 [Ant Design React 的 demo](https://ant.design/docs/react/getting-started-cn) 时报错 `Cannot find module 'webpack/lib/removeAndDo'`，原因是需要在项目中 install webpack，和上一个一样。参考：
	- [Error: Cannot find module 'webpack'](http://stackoverflow.com/questions/29492240/error-cannot-find-module-webpack)
	- [Error: Cannot find module 'webpack/lib/node/NodeTemplatePlugin'](http://stackoverflow.com/questions/43179531/error-cannot-find-module-webpack-lib-node-nodetemplateplugin)
4. Ant Design 中的日期问题
	[文档里的示例](https://ant.design/components/date-picker-cn/#components-date-picker-demo-disabled-date)是这样：
	```
	function disabledDate(current) {
	  // can not select days before today and today
	  return current && current.valueOf() < Date.now();
	}
	```
	API 中的说明是： disabledDate（不可选择的日期）类型为 function。
	需求是要将不可选的范围定为 `今天~2017.8.31` 之外，于是我这样改了：
	```
	return current.valueOf() > ddl || current.valueOf() < Date.now();
	```
	结果就是报错：`Uncaught TypeError: Cannot read property 'valueOf' of undefined`，于是我打印 `current` 的值出来看。它是一个 Moment 对象，`__proto__` 中是有 `valueOf` 这个方法的，所以出现 undefined 很有可能是因为传进去的值是空值，所以我增加了对 `current` 的过滤：
	```
	if(current){
		console.log(current.valueOf());
		return  (current.valueOf() > ddl || current.valueOf() < Date.now() );
	} else return false;
	```
	结果这样一来才发现，和示例中的写法达成的目的是一样的……ORZ 这种小 tips 之前完全没有注意到……
5. [Moment.js](http://momentjs.com) 是一个时间类的库，Ant Design 就用了它，看[文档](http://momentjs.com/docs/#/query/)提供了一些简易的方法，所以上面的再改进一下可以改成这样：
	```
	return  current && !current.isBetween(now, ddl, 'day', '[)');
	```
	
### 参考文档

除了上述的解决具体问题参考的链接外，阅读过的一些页面：

- [在 create-react-app 中使用 Ant Design](https://ant.design/docs/react/use-with-create-react-app-cn)
- [发布 React App 至 GitHub Pages](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md#github-pages)
- 看了几位以前求职者的答案：[Jinmeng Liu](https://github.com/fightingljm/redshift-datepicker)、[BaddbboY](https://github.com/BaddbboY/My-answer--Redshift)
- [package.json 中配置 babel 的写法](https://github.com/search?utf8=%E2%9C%93&q=babel-plugin-import+babel+plugins+libraryName+style+extension%3Ajson&type=Code)

### 整体感受

（请酌情忽略下面的碎碎念）

很喜欢这样的面试形式，这种解决具体问题的方式，出题者和做题者都要付出更大的精力。相比拿着一堆问答型的题目挨个问的形式，更能激起我的兴趣，总觉得这种更高明，所以很高兴有这样的面试经历。

关于开发的过程，刚拿到题目的时候心想我两小时就能搞定，做起来才发现自己 too simple，此前没有用过 React 和 Webpack，这样一趟做下来也算是学到了不少东西，不满意的就是用的时间太长，长到我已经不忍直视HR说的“尽快”这个词了。

时间紧张，暂时说到这里。