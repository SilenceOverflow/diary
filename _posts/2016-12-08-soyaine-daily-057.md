---
layout: background
title: "所丫日报" 
date: 2016-12-08 
category: soyainedaily 
excerpt: "something about liquid"
---

## 学习笔记

### 字符串去空格化处理

页面中的标签换行时，有可能会被解析为换行符，在把 Liquid 遍历获取链接生成的 `<a>` 标签中的文本换行时

{% raw %}
```HTML
<!--原写法-->
<a href="{{ site.baseurl }}{{ post.url }}">{{ post.date | replace: '-', '/' | replace: '/0', '/' | slice: 0, 10 | strip }}</a>

<!--出现换行-->
<a href="{{ site.baseurl }}{{ post.url }}">
   {{ post.date | replace: '-', '/' | replace: '/0', '/' | slice: 0, 10 | strip }}
</a>
```
{% endraw %}


有两种办法，一是把代码改为不换行的形式，二是获取字符串后处理，用正则替换，这个方法比较保险，可以避免出现其他的问题，在处理字符串的时候都应该检查一下是否有边际情况。其中 `\n` 匹配换行符，而其余的则是匹配空格，在没有 `String.prototype.trim` 时也可以用这种方法来向下兼容。

```javascript
str = str.replace(/^[\s\uFEFF\xA0\n]+|[\s\uFEFF\n\xA0]+$/g, '');
```

### 文章列表数据处理

最开始我是使用 HTML 标签的形式，后来突然想到能不能直接把 Liquid 混在 JS 标签里面写，写成 JSON 的格式，试了一下果真可以。

原来思路：用 Liquid 获取文章列表，放入嵌套在指定 ID 的 `<a>` 标签中，然后用 JS 获取 DOM 元素，读取其 `children` 再把数据写入对象中，后续使用。

HTML 标签部分代码：

{% raw %}

```HTML
<div id="urlList" style="display: none">
    {% for post in site.posts %}
    <!--<li>-->
    <!--{{ post.date | to_string }}-->
    <a href="{{ site.baseurl }}{{ post.url }}">{{ post.date | replace: '-', '/' | replace: '/0', '/' | slice: 0, 10 | strip }}</a>
    {{ post.excerpt }}
    <!--</li>-->
    {% endfor %}
</div>
```

{% endraw %}

JS 代码：

{% raw %}

```JavaScript
loadList: function(){
    var list = document.getElementById("urlList");
    var url = {};
    for(var li in list.children){
        var date = list.children[li].innerText;
        url[date] = list.children[li].href;
    }
    this.url = url;
}
```

{% endraw %}

改进：如果直接在 Jekyll 生成静态页面时就生成了 JSON 对象，那么则省去了上述部分，可以直接读取数据并渲染到日历中去。上面两部分所实现的目的，可以用下面这些来完成。

{% raw %}

```html+javascript
<script>
    var urlJSON = {
      {% for post in site.posts %}
        "{{ post.date | replace: '-', '/' | replace: '/0', '/' | slice: 0, 10 | strip }}": {
            url: "{{ site.baseurl }}{{ post.url }}" ,
            excerpt: "{{ post.excerpt }}"
        },
      {% endfor %}
      //循环结束，对象最末一个值木有逗号
      "end": "end"  
    };
</script>
```

{% endraw %}

### 如何在 Markdown 文档中写 Liquid 标签而不被解析

关键词：code block render interpret/process

以上面一节中最后部分的代码为例，有下面两种写法。

#### 一、`raw` 标签

在代码区域前后加入 Liquid 的 `raw` 标签，如下图所示：
![写法一截图](/diary/img/2016-12-09-how-to-write-liquid-in-markdown-1.PNG)

#### 二、使用值为 `{` 的变量

声明一个 Liquid 变量，赋值为花括号，在代码中将所有的 `{` 都替换为这个变量，使其渲染之后出现正确的字符。此方法来源于[ @neagle 的博客](http://nateeagle.com/2011/08/31/how-to-output-curly-brackets-in-jekyll/)。这里的 lcb 是指 left-curly-bracket ,花括号的英文名。

可以在 YML 文件头或者 _config.yml 文件中声明，这里需要注意的是，若是在 _config.yml 中声明，引用时使用的变量名为 `site.lcb` ，若是在 Markdown 的文件头中声明，则使用 `page.lcb` 进行引用。

![写法二截图](/diary/img/2016-12-09-how-to-write-liquid-in-markdown-2.PNG)

或者直接用变量声明，使用变量声明标签 `assign` 。下图左右对比分别为 Markdown 中写法，以及渲染后的 HTML 页面。

![写法二截图](/diary/img/2016-12-09-how-to-write-liquid-in-markdown-3.PNG)

{% assign lcb = "{" %}
```javascript
<script>
    var urlJSON = {
      {{ lcb }}% for post in site.posts %}
        "{{ lcb }}{ post.date | replace: '-', '/' | replace: '/0', '/' | slice: 0, 10 | strip }}": {
            url: "{{ lcb }}{ site.baseurl }}{{ post.url }}" ,
            excerpt: "{{ lcb }}{ post.excerpt }}"
        },
      {{ lcb }}% endfor %}
      //循环结束，对象最末一个值木有逗号
      "end": "end"  
    };
</script>
```

#### `raw` 方式下的语法高亮

对比可见以上两种方式在 Code Highlighter 上有所区别，即用 `raw` 标签时不会将其按照代码区来进行解析，此时则需要直接使用 Liquid 的高亮语法，写法及效果如下：

这里有一个坑是，Liquid 的开始和结束标签是不一样的，结束标签含有一个 `end`，最开始我写错了，jekyll serve 时一直报错，还去重装了一下 Ruby 里的一些 gem，最后发现是结束标签少写了。

![语法高亮截图](/diary/img/2016-12-09-how-to-write-liquid-in-markdown-4.PNG)

{% highlight javascript %}
{% raw %}
<script>
    var urlJSON = {
      {% for post in site.posts %}
        "{{ post.date | replace: '-', '/' | replace: '/0', '/' | slice: 0, 10 | strip }}": {
            url: "{{ site.baseurl }}{{ post.url }}" ,
            excerpt: "{{ post.excerpt }}"
        },
      {% endfor %}
      //循环结束，对象最末一个值木有逗号
      "end": "end"  
    };
</script>
{% endraw %}
{% endhighlight %}

参考：

- https://github.com/jekyll/jekyll/issues/814
- http://www.ozzieliu.com/2016/04/26/writing-liquid-template-in-markdown-with-jekyll/
- 高亮 https://sacha.me/articles/jekyll-rouge/#using-rouge-in-jekyll-3-on-github-pages
- Rouge https://github.com/jneen/rouge

### 括号的名称

- [] : Brackets
- () : Round brackets / Parentheses
- {} : Curly brackets / Braces
- <> : Angle brackets / Chevrons

## 其他发现

[Maruku](http://maruku.rubyforge.org/maruku.html) 是一个支持 TOC 的 Markdown 解释器。

想自己写一个目录生成的 JS 组件。
