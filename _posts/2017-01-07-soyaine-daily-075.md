---
layout: post
title: "所丫日报" 
date: 2017-01-07 
category: soyainedaily 
excerpt: ""
---

<div id="timeChart" style="width: 100%; height: 500px;"></div>

<script>
const data = [
  {
    "time": "0.677",
    "no": "Javascript30-10",
    "info": "写作",
    "date": "2017/1/7"
  },
  {
    "time": "1.176",
    "no": "Javascript30-10",
    "info": "写作",
    "date": "2017/1/7"
  },
  {
    "time": "0.719",
    "no": "Javascript30-10",
    "info": "自己练习",
    "date": "2017/1/7"
  },
  {
    "time": "0.698",
    "no": "Javascript30",
    "info": "研究如何调试JS",
    "date": "2017/1/7"
  },
  {
    "time": "0.323",
    "no": "Javascript30-10",
    "info": "自己练习",
    "date": "2017/1/6"
  },
  {
    "time": "0.643",
    "no": "Javascript30-10",
    "info": "自己练习",
    "date": "2017/1/6"
  },
  {
    "time": "0.222",
    "no": "Javascript30-10",
    "info": "视频",
    "date": "2017/1/6"
  },
  {
    "time": "1",
    "no": "Javascript30-09",
    "info": "写作",
    "date": "2017/1/6"
  },
  {
    "time": "0.5",
    "no": "Javascript30-09",
    "info": "写作",
    "date": "2017/1/6"
  },
  {
    "time": "0.817",
    "no": "Javascript30-09",
    "info": "练习",
    "date": "2017/1/6"
  },
  {
    "time": "0.633",
    "no": "Javascript30-02",
    "info": "文章更新",
    "date": "2017/1/6"
  },
  {
    "time": "0.186",
    "no": "Javascript30-09",
    "info": "练习",
    "date": "2017/1/5"
  },
  {
    "time": "2.317",
    "no": "Javascript30-02",
    "info": "问题处理检索",
    "date": "2017/1/5"
  },
  {
    "time": "0.961",
    "no": "Javascript30-08",
    "info": "写作",
    "date": "2017/1/4"
  },
  {
    "time": "1.15",
    "no": "Javascript30-08",
    "info": "写作",
    "date": "2017/1/4"
  },
  {
    "time": "1.095",
    "no": "Javascript30-08",
    "info": "写作",
    "date": "2017/1/4"
  },
  {
    "time": "1.344",
    "no": "Javascript30-08",
    "info": "回想自己写",
    "date": "2017/1/4"
  },
  {
    "time": "0.663",
    "no": "Javascript30-08",
    "info": "练习",
    "date": "2017/1/3"
  },
  {
    "time": "0.133",
    "no": "Javascript30-07",
    "info": "整理上传",
    "date": "2017/1/3"
  },
  {
    "time": "0.903",
    "no": "Javascript30-07",
    "info": "写作",
    "date": "2017/1/3"
  },
  {
    "time": "0.698",
    "no": "Javascript30-07",
    "info": "练习",
    "date": "2017/1/3"
  },
  {
    "time": "0.5",
    "no": "Javascript30-06",
    "info": "整理发布",
    "date": "2017/1/3"
  },
  {
    "time": "1.933",
    "no": "Javascript30-06",
    "info": "写作",
    "date": "2017/1/3"
  },
  {
    "time": "1.3",
    "no": "Javascript30-06",
    "info": "写作",
    "date": "2017/1/2"
  },
  {
    "time": "1.45",
    "no": "Javascript30-06",
    "info": "写作",
    "date": "2017/1/1"
  },
  {
    "time": "0.278",
    "no": "Javascript30-06",
    "info": "写作",
    "date": "2016/12/31"
  },
  {
    "time": "0.7",
    "no": "Javascript30-06",
    "info": "细节调整录屏",
    "date": "2016/12/31"
  },
  {
    "time": "2.409",
    "no": "Javascript30-06",
    "info": "练习",
    "date": "2016/12/31"
  },
  {
    "time": "0.807",
    "no": "Javascript30-05",
    "info": "写作",
    "date": "2016/12/31"
  },
  {
    "time": "1.39",
    "no": "Javascript30-05",
    "info": "写作",
    "date": "2016/12/30"
  },
  {
    "time": "1.517",
    "no": "Javascript30-05",
    "info": "找图录屏",
    "date": "2016/12/30"
  },
  {
    "time": "2.031",
    "no": "Javascript30-05",
    "info": "回忆过程",
    "date": "2016/12/30"
  },
  {
    "time": "0.4",
    "no": "Javascript30-05",
    "info": "练习",
    "date": "2016/12/30"
  },
  {
    "time": "0.493",
    "no": "Javascript30-05",
    "info": "练习",
    "date": "2016/12/24"
  },
  {
    "time": "0.657",
    "no": "Javascript30-04",
    "info": "整理细节",
    "date": "2016/12/23"
  },
  {
    "time": "1.205",
    "no": "Javascript30-04",
    "info": "写作",
    "date": "2016/12/23"
  },
  {
    "time": "0.467",
    "no": "Javascript30-04",
    "info": "自己应用",
    "date": "2016/12/23"
  },
  {
    "time": "0.45",
    "no": "Javascript30-04",
    "info": "自己应用",
    "date": "2016/12/23"
  },
  {
    "time": "0.333",
    "no": "Javascript30-04",
    "info": "自己应用",
    "date": "2016/12/23"
  },
  {
    "time": "1.602",
    "no": "Javascript30-04",
    "info": "练习",
    "date": "2016/12/23"
  },
  {
    "time": "0.2",
    "no": "Javascript30",
    "info": "调整更新细节",
    "date": "2016/12/22"
  },
  {
    "time": "1.535",
    "no": "Javascript30-03",
    "info": "写作",
    "date": "2016/12/22"
  },
  {
    "time": "0.57",
    "no": "Javascript30-03",
    "info": "图片，录屏",
    "date": "2016/12/22"
  },
  {
    "time": "0.491",
    "no": "Javascript30-03",
    "info": "兼容IE",
    "date": "2016/12/22"
  },
  {
    "time": "0.45",
    "no": "Javascript30-03",
    "info": "搜索color、input相关",
    "date": "2016/12/22"
  },
  {
    "time": "1.374",
    "no": "Javascript30-03",
    "info": "练习",
    "date": "2016/12/22"
  },
  {
    "time": "2.239",
    "no": "Javascript30",
    "info": "文章修改，图片编辑",
    "date": "2016/12/21"
  },
  {
    "time": "0.441",
    "no": "Javascript30-02",
    "info": "文章发布",
    "date": "2016/12/21"
  },
  {
    "time": "1.187",
    "no": "Javascript30-02",
    "info": "文章写作",
    "date": "2016/12/21"
  },
  {
    "time": "0.583",
    "no": "Javascript30-02",
    "info": "练习",
    "date": "2016/12/21"
  },
  {
    "time": "0.828",
    "no": "Javascript30-02",
    "info": "练习",
    "date": "2016/12/21"
  },
  {
    "time": "0.333",
    "no": "Javascript30-02",
    "info": "练习",
    "date": "2016/12/21"
  },
  {
    "time": "1.241",
    "no": "Javascript30-02",
    "info": "练习",
    "date": "2016/12/21"
  },
  {
    "time": "0.844",
    "no": "Javascript30-02",
    "info": "练习",
    "date": "2016/12/21"
  },
  {
    "time": "0.386",
    "no": "Javascript30-01",
    "info": "提交git",
    "date": "2016/12/20"
  },
  {
    "time": "1.615",
    "no": "Javascript30-01",
    "info": "指南写作",
    "date": "2016/12/20"
  },
  {
    "time": "1.595",
    "no": "Javascript30-01",
    "info": "",
    "date": "2016/12/20"
  },
  {
    "time": "1.519",
    "no": "Javascript30-01",
    "info": "",
    "date": "2016/12/20"
  },
  {
    "time": "0.96",
    "no": "Javascript30-01",
    "info": "",
    "date": "2016/12/20"
  }
];

var timeChart = echarts.init(document.getElementById('timeChart'));
  timeChart.title = 'JavaScript30 - 时间记录堆叠柱状图（12.20-01.07）';

var option  = {
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
            data: []
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
            data: ,
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

var x = data.map(item => item.date);
var y = data.map(item => item.time);
diaryOption.xAxis[0].data = x;
diaryOption.series[0].data = y;
timeChart.setOption(option);
</script>
