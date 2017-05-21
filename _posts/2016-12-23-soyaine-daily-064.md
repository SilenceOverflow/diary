---
layout: post
title: "所丫日报" 
date: 2016-12-23 
category: soyainedaily 
excerpt: ""
---

鼓捣了一下 echarts，把记录下来的 csv 数据导出来看了看（这个网站可以在线转换 [http://www.csvjson.com/csv2json](http://www.csvjson.com/csv2json)），顺便用了下今天练习时用到的几个 Array 的方法，感觉又很多可以玩的地方，关键在于我想怎么呈现数据，以及我想要如何分析。用的 Time Meter 可以备份文档，这比我上半年用手写 + 回忆要精确和便捷许多，这样可以允许我花更多的精力在思考上。

## 整理反思

整理一下最近四天在 JavaScript30 上的时间记录，思考一下要怎么调整改进。

<div id="timeChart" style="width: 100%; height: 500px;"></div>

其实我专注花在写作上的时间每天都固定在一个半小时左右，而花在整理发布文章上的时间则占了一大半。整理主要是指截图上传，发布到简书、分享到掘金，昨天我意识到这样做其实是分散了精力，倒不如把心思集中在练习和写作上面。 昨天把写的指南介绍分享到掘金，早上通知没通过审核，我想可能因为是那篇文章有太多的外链，并没有涉及到具体的技术问题，我就不信邪，又重新换了一篇 GitHub 上的时钟指南上去，通过了，反响要比简书好得多，截止到今天 23:28 的数据是——收藏 18、阅读 393，而简书同样这篇文章只有 55 的阅读量。掘金是个聚集技术文章的地方，而简书则是一个聚集文字的地方，两者相较而言，掘金上的人更有可能是我这个系列文章的主要受众。或许今后我会选择先写好文章，偶尔发到其他平台，以保留我的精力。

另外我筛出了之前花在 Diary 上的时间。用了下面的语句：

````js
const diary = json.filter( item => item["tag"] == "Diary")

const diary-time = diary.reduce( (obj, item) => {
const date = item["start"].slice(0, 10);
	if(!obj[date]){
	obj[date] = 0;
	} 
	obj[date] += item["time"];
	return obj;
},{});

console.log(Object.keys(date));
console.log(Object.values(date));
````

<div id="diaryChart" style="width: 100%; height: 500px;"></div>

只是大概实验了一下 echarts 的简单配置，后续再研究更高阶的玩法。晚安。

2016-12-24 0:19|

<!--<script src="//cdn.bootcss.com/echarts/3.3.2/echarts.common.min.js"></script>-->
<script src="/diary/js/echarts.common.min.js"></script>

<script>
var timeChart = echarts.init(document.getElementById('timeChart'));
  timeChart.title = 'JavaScript30 - 时间记录堆叠柱状图（12.20-12.23）';

var option = {
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data:['练习','写作','应用', '整理', '问题', '其它']
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
            data : ['12.20','12.21','12.22','12.23']
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'练习',
            type:'bar',
			stack:'in',
            data:[3.114, 3.829, 1.374, 1.602]
        },
        {
            name:'写作',
            type:'bar',
			stack:'in',
            data:[1.615, 1.187, 1.535, 1.205]
        },
        {
            name:'整理',
            type:'bar',
			stack:'out',
            data:[0.386, 2.68, 0.77, 0.657]
        },
        {
            name:'其它',
            type:'bar',
			stack:'out',
            data:[2.265, 0, 0.941, 1.25]
        }
    ]
};
timeChart.setOption(option);

var diaryChart = echarts.init(document.getElementById('diaryChart'));
diaryChart.title = 'Diary 时间记录';

var diaryOption  = {
    tooltip: {
        trigger: 'axis'
    },
    toolbox: {
        feature: {
            magicType: {show: true, type: ['line', 'bar']}
        }
    },
    legend: {
        data:['Time in Diary']
    },
    xAxis: [
        {
            type: 'category',
            data: ["2016-12-09","2016-12-08","2016-12-07","2016-12-06","2016-12-05","2016-12-04","2016-12-03","2016-12-02","2016-12-01","2016-11-30","2016-11-29"].reverse()
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: 'Time',
            min: 0
        }
    ],
    series: [
        {
            name:'Time in Diary',
            type:'bar',
            data:[1.6219999999999999, 4.6979999999999995, 3.4670000000000005, 0.588, 0.893, 3.196, 1.918, 2.199, 5.501, 6.6240000000000006, 2.033].reverse(),
            itemStyle: {
                normal: {
                    color: '#e78b91',
                    shadowBlur: 20,
                    shadowColor: 'rgba(0, 0, 0, 0.3)'
                }
            }
        }
    ]
};

diaryChart.setOption(diaryOption);
</script>