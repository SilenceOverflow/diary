---
layout: post
title: "所丫日报" 
date: 2016-12-27 
category: soyainedaily 
excerpt: ""
---

## 一些小发现

昨天掘金的运营通过了我申请的 Co-Editer，可以自由分享文章而不需审核，我顺手把 JavaScript30 的第四篇放了过去，不到一天的时间收藏量要高于上一篇文章（关于纯 JS 时钟）。早上看了一下数据，统计了一下：

````js
var time = Array.from(document.querySelectorAll('tr.read td.text-right span'));
const reduce = time.reduce( (obj, item) => {
      item = item.innerText;
	  if( !obj[item]  ) {
		  obj[item] = 0;
	  }
		  obj[item]++;
		  return obj;
  }, {});

````

得到下面的数据：

````json
{
 "1小时前": 7,
 "2小时前": 7,
 "3小时前": 7,
 "4小时前": 3,
 "8小时前": 1,
 "9小时前": 2,
 "10小时前": 4,
 "11小时前": 6,
 "12小时前": 3,
 "13小时前": 8
}
````

<div id="timeChart" style="width: 100%; height: 500px;"></div>

由于掘金上并没有显示具体的时间，所以这个数据只能得到一个粗略的推算值。大概有两个时间节点是收藏量比较高的，一个是午夜 12 点前后，另一个是早上 10 前后，一个是睡前而另一个则是早上刚上班的时间。其实如果好奇具体的阅读数据，可以直接把文章发布到 GitHub Pages 然后用 Google Analytics 来看。今天只是不小心注意到了不同时间点的数据量有差别，所以简单统计了一下。

## 闭包的一些链接

- http://nathansjslessons.appspot.com/
- https://github.com/windiest/Good-text-Share/issues/8
- https://www.youtube.com/watch?v=w1s9PgtEoJs
- http://stackoverflow.com/questions/111102/how-do-javascript-closures-work
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures


<script src="/diary/js/echarts.common.min.js"></script>
<script>
var timeChart = echarts.init(document.getElementById('timeChart'));
  timeChart.title = '阅读统计';

var option = {
	title: {
		text: 'JavaScript30 中文指南 04 掘金收藏量',
		link: 'https://gold.xitu.io/entry/58610c8161ff4b006ce9dffc/detail',
		subtext: '2016.12.27 11:28 统计值'
	},
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'line'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data:['收藏量']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            data : ["1小时前","2小时前","3小时前","4小时前","8小时前","9小时前","10小时前","11小时前","12小时前","13小时前"]
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'收藏量',
            type:'line',
			stack:'in',
            data:[7,7,7,3,1,2,4,6,3,8]
        }
    ],
	color: ['#009999']
};
timeChart.setOption(option);
</script>