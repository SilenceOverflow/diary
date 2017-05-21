---
layout: post
title: "0319 箱线图是什么" 
date: 2017-03-19 
category: soyainedaily 
excerpt: "ECharts 中箱线图的数据问题"
---

## 学习手记

### ECharts 中箱线图计算后数据出现负值的问题

绘制箱线图的时候，用 `echarts.dataTool.prepareBoxplotData` 这个工具对数据进行计算，可能会出现负值。

#### 引用一下别人的解答

> prepareBoxplotData 这个工具方法参考了：https://en.wikipedia.org/wiki/Box_plot，其中，boxplot 的 两个『须』的端点有几个可能的定义，比如，
>
> - 可以是 Q1 - 1.5 * IQR 和 Q3 + 1.5 * IQR ，`prepareBoxplotData` 默认情况下，采用这种定义，也就是说，`echarts.dataTool.prepareBoxplotData([ ... ])` 可能出现负值。
> - 可以是『最大最小值』 `echarts.dataTool.prepareBoxplotData([ ... ], {boundIQR: 'none'})` 则使用这种定义，不会出现负值。
>
> via [100pah](https://github.com/ecomfe/echarts/issues/5094)

#### 箱线图是个啥

箱线图最常用的场景可能是股价图中的“开盘-盘高-盘低-收盘图”，英文是 Box plot，还有一个名字叫箱须图（Box-whisker Plot），从图示可以简单理解为这是用“箱”和“线”两种元素来表示一些统计数据。

![Box plot from Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Michelsonmorley-boxplot.svg/600px-Michelsonmorley-boxplot.svg.png)

其中对于“箱”的数据来源的定义是固定的，括号后是其他称呼：

1. box 顶：第三四分位数（上四分位数/Q3）
2. box 中的线：第二四分位数（中位数）
3. box 底：第一四分位数（下四分位数/Q1）

但对上下两条“须”的定义就有多种了：

- 数据的最大值、最小值
- Turkey Boxplot 的定义：在某个区间之外的数据应该被忽略，所以由此确定一个范围，此时有可能出现负值，这也是 ECharts 的默认定义。
  - 最大值区间：Q3 + 1.5*IQR
  - 最小值区间：Q1 -  1.5*IQR
- 第 9 百分位、91 百分位数
- 第 2 百分位、98 百分位数

注一些统计概念：
 - [四分位数（Quartile）](https://en.wikipedia.org/wiki/Quartile)：把所有数从小到大排列后四等分，三个分割点就是四分位数。从小到大就分别是 Q1 Q2 Q3。但这几个值的计算方式也有多种。
 - [四分位距](https://zh.wikipedia.org/wiki/%E5%9B%9B%E5%88%86%E4%BD%8D%E8%B7%9D)（[InterQuartile Range, IQR](https://en.wikipedia.org/wiki/Interquartile_range)）：Q3 - Q1

#### 引用并研究一下 ECharts 的源码

去 ECharts 查了一下源码，[附地址](https://github.com/ecomfe/echarts/blob/c7b62850ef9efa928415a91ae77b42928b823be6/dist/extension/dataTool.js#L287)。

```js
var __WEBPACK_AMD_DEFINE_RESULT__;!(__WEBPACK_AMD_DEFINE_RESULT__ = function (require) {

	    var quantile = __webpack_require__(7);
	    var numberUtil = __webpack_require__(1).number;

	    /**
	     * Helper method for preparing data.
	     * @param {Array.<number>} rawData like //传入的待计算的系列数据
	     *        [
	     *            [12,232,443], (raw data set for the first box)
	     *            [3843,5545,1232], (raw datat set for the second box)
	     *            ...
	     *        ]
	     * @param {Object} [opt]
	     *
	     * @param {(number|string)} [opt.boundIQR=1.5] Data less than min bound is outlier.
	     *                          default 1.5, means Q1 - 1.5 * (Q3 - Q1).
	     *                          If pass 'none', min bound will not be used.
	     *                          此处说明了 boundIQR 这个参数，默认为 1.5，但也可以修改为原数据值
	     * @param {(number|string)} [opt.layout='horizontal']
	     *                          Box plot layout, can be 'horizontal' or 'vertical'
	     */
	    return function (rawData, opt) {
	        opt = opt || [];
	        var boxData = [];
	        var outliers = [];
	        var axisData = [];
	        var boundIQR = opt.boundIQR;

	        for (var i = 0; i < rawData.length; i++) {
	            axisData.push(i + '');
	            var ascList = numberUtil.asc(rawData[i].slice());

	            var Q1 = quantile(ascList, 0.25);
	            var Q2 = quantile(ascList, 0.5);
	            var Q3 = quantile(ascList, 0.75);
	            var IQR = Q3 - Q1;

                // 根据 boundIQR 的值，得到求解办法，获取最小值和最大值，即须
	            var low = boundIQR === 'none'
	                ? ascList[0]  //原数据最小值
	                : Q1 - (boundIQR == null ? 1.5 : boundIQR) * IQR; //Q1 - 1.5*IQR
	            var high = boundIQR === 'none'
	                ? ascList[ascList.length - 1] //原数据最大值
	                : Q3 + (boundIQR == null ? 1.5 : boundIQR) * IQR; //Q3 + 1.5*IQR

	            boxData.push([low, Q1, Q2, Q3, high]);

	            for (var j = 0; j < ascList.length; j++) {
	                var dataItem = ascList[j];
	                if (dataItem < low || dataItem > high) {
	                    var outlier = [i, dataItem];
	                    opt.layout === 'vertical' && outlier.reverse();
	                    outliers.push(outlier);
	                }
	            }
	        }
	        return {
	            boxData: boxData,
	            outliers: outliers,
	            axisData: axisData
	        };
	    };
```

#### 小结论

所以有时绘制箱线图，提供的数据没有负值，但是绘图结果却出现了负值，可能是计算方式的问题。默认情况下的上下两线的定义是某个区间，这个区间由四分位距计算得到，分别是

- 最大值区间：Q3 + 1.5*IQR
- 最小值区间：Q1 -  1.5*IQR

若要让绘图结果按照原始数据的范围来绘制，则可以加入 `boundIQR` 的参数设定。

```js
var data = echarts.dataTool.prepareBoxplotData(
  			[
             	[12,232,443],  // (raw data set for the first box)
	            [3843,5545,1232],  //(raw datat set for the second box)
	            ...
	        ], {boundIQR: 'none'}
	);
```

即可。