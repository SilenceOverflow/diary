---
layout: post 
title: "所丫日报"
date: 2016-04-22
category: soyainedaily
excerpt: "关于技能 Python抓数据"
---

## 关于技能

### 任务简介

今天帮助学长采集列车信息的数据，准确的说是从昨天晚上就拿到任务了。做的事情：给定了车次信息，在12306网站上查询出发时间、到达时间、车票价格，并填入excel表格。

最开始我打算写程序来抓取，之前配置过Python的环境，所以选择用Python，于是昨晚以及今早的时间都用来学习Python了，最终结果：在另一个网站上抓取到了所需信息。不过最后还是人工去检查核对才完成了任务。

参考：

- [python requests的安装与简单运用](http://www.zhidaow.com/post/python-requests-install-and-brief-introduction)


- [python-requests文档](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html) 

### Python 正则表达式及读取文件

获取并解析页面，运用正则表达式匹配查找出时间信息：

```
\d{2}:\d{2}
```

用正则表达式对象获取所有匹配的子串并放入数组（Use regex object to get an array of all regex matches in a string）：
```
reobj = re.compile(regex)
result = reobj.findall(subject)
```

Python读取文件：

```
list = []  
f = open("data.txt","r")  
for read in f.readlines():  
list.append(read);  
print list  
```
运行结果：

 ['1\n', '2\n', '3\n', '4\n', '5\n', '5\n', '6\n', '\n', '\n']

python 会出现\n的情况，怎么去除？


```
if colb.find("\n")>0:  
colb=colb[0:len(colb)-1]  
```

参考 [Python文件操作](http://www.programgo.com/article/13363084274/;jsessionid=0C79DAD555C2D6426A25D330BF70ECA3)


### Python小Tips

1. 反斜杠和斜杠要区分开：
   - C:\Users\test\Desktop
   - C:/Users/test/Desktop    —— Python这是正确的

2. 使用with打开文件是一个很好的习惯，因为with结束，它就会自动close file，不用手动再去flie.close()。

### 结果
我写的主要代码如下，以下是一些片段，并非完整程序：

```python
import re //导入
import requests  //导入
f = open('C:/Users/test/Desktop/info.txt', 'r') //打开存储车次信息的文件
data = f.readlines() //读取数据
print(data)

r = requests.get('http://train.tielu.org/Search/1148.html')
line = r.text
matchobj = re_tran.findall(line)
print(matchobj[0], matchobj[1])

re_tran = re.compile( r'\d{2}\:\d{2}') //编译正则表达式

f = open('C:/Users/test/Desktop/traninfo.txt', 'a+')  //打开文件，以添加数据的方式
for x in data: //读取车次数据
    if x.find("\n")>0:
        x = x[0:len(x) - 1]
        print(x)
    f.write(x)
    f.write(',')
    url = 'http://train.tielu.org/Search/'+ x +'.html'
    print(url)
    r = requests.get(url) //创建请求
    line = r.text
    matchobj = re_tran.findall(line) //正则表达式匹配
    if matchobj == []: //判断当前车次是否有相关信息
        print("未找到")
        f.write("未找到"+'\n')
        continue
    print(matchobj[0])
    f.write(matchobj[0])  //将结果输出到文件
    f.write(',')
    f.write(matchobj[1]+'\n')
    print(matchobj[1])
```

其他参考内容：[Python:获取全国旅客列车车次及其始发终点站（更新）](http://www.polarxiong.com/archives/Python-%E8%8E%B7%E5%8F%96%E5%85%A8%E5%9B%BD%E6%97%85%E5%AE%A2%E5%88%97%E8%BD%A6%E8%BD%A6%E6%AC%A1%E5%8F%8A%E5%85%B6%E5%A7%8B%E5%8F%91%E7%BB%88%E7%82%B9%E7%AB%99-%E6%9B%B4%E6%96%B0.html)

## 问题

我觉得我需要为我的 blog 做一个自动生成目录的功能。
GitHub里两个标题之间需要换行才能识别。如本文开头的两个标题。

