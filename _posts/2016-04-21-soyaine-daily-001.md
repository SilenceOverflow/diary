---
layout: post
title: "所丫日报"
date: 2016-04-21
category: soyainedaily
excerpt: "关于日报，读书札记《把时间当做朋友》，关于技能 CSS，其他内容 小狼毫/鼠须管"
---

## 关于日报

操作流程试验成功，基本环境已配置完成。使用Typora可以关联本地.md文档，界面很简洁易用，GitHub桌面版Sync也可成功同步，所以今后可以直接在本地离线编辑，找一个时间（如周末）统一上传，这样就不用花费太多的时间在等待网络连接和同步之上。

先后试了几个Markdown的编辑器（又是外延=_=）：

- Markdown.UWP - 第一个试用，有基本功能，不过界面不如Typora舒心简洁。
- cmd Markdown - 需要导出生成.md文档到本地，可在网页端编辑，有云同步及分享功能，对我来说有点功能过剩了，非我想要。
- Typora - 界面极其简洁美观优雅，我所需功能不多，够用。所见即所得，这个功能很棒。

刚才发现另外关于读书札记也可以每天在手机便签上记录，然后统一时间整理出来。还有GitHub的Contributions可能也可以激励我把每天的都点绿，这就需要每天都push一些更新，可以是每天把前一天已经完成的日报内容上传。

我需要学习的是使用简洁的语言去记录（而不是像上面一样……废话好多）。还有吐槽一下现在我使用的GitHub Page主题好丑，引用只是缩进显示，中文的行间距太小，我得学一下怎么换模板，或者把现在的模板修改得顺眼一点。

## 读书札记
《把时间当做朋友》

没有随着之前的进度看，翻到后面希望能翻到些对目前的状态有帮助的经验。

> 坚持不懈是什么？是策略加上重复，把抽象的目标赋予其实际的意义，从而感受到更多的动力。

我不必所有目标都幻化成money的形状，但可以转化成其他令自己有成就感的东西，想起了之前看到关于『如何写满一个笔记本』的建议：想象自己写到最后一页的时候的情景，这样潜意识里也会朝着那个想象而行动了。

不过这好像是两件事情，但都是把目标变得清晰可见、对自己有吸引力，从而实现补充动力的效果。对于我来说，可以想象自己运用技能做出漂亮作品的感觉、年末翻看一整年的日报时体会到成长的感觉、身材令自己很满意的感觉…等等等等。对我来说，可能这样的情景模拟更有力，试试。

另外一个收获，记录尴尬的好处，避免人具有的不同程度的遗忘痛苦的能力，用来提醒自己之后不要犯同样的错误，并能看到过去的成长。面对尴尬，一是记录，二是提醒自己不要被大脑的直接情绪（痛苦）反应给左右。

## 关于技能

想要把博客的样式修改得顺眼一些，为了顺便学习一下CSS 就自己手动修改了，用jekyll serve 可以在本地实时查看修改的效果，免去了上传到GitHub 的麻烦。

主要操作方法是：Git Bash 中进入 xxx.github.io 文件夹，运行 jekyll serve 命令即可启动，然后在浏览器访问 http://localhost:4000 即可。

### 排版

在 [jekyllcn的贡献翻译页面](https://github.com/xcatliu/jekyllcn#如何贡献翻译) （这个可以去贡献一点翻译）看到了 [写给大家看的中文排版指南](http://zhuanlan.zhihu.com/p/20506092) ，学到一点，**中西文混合排版时，中英文之间要加空格，中文与数字、链接之间也要加空格。**

### CSS 中文字体对应名称

参考 [CSS 中文字体表达方式](http://www.css3-html5.com/DivCSS/20110718741.html) ，在Windows平台下：

- 微软雅黑 - Microsoft YaHei
- 楷体_GB2312 - KaiTi_GB2312
- 楷体 - KaiTi

### CSS 选择器

|                   选择器                    |  例子   |            例子描述             | CSS  |
| :--------------------------------------: | :---: | :-------------------------: | :--: |
| [*element*,*element*](http://www.w3school.com.cn/cssref/selector_element_comma.asp) | div,p |  选择所有 <div> 元素和所有 <p> 元素。   |  1   |
| [*element* *element*](http://www.w3school.com.cn/cssref/selector_element_element.asp) | div p |  选择 <div> 元素内部的所有 <p> 元素。   |  1   |
| [*element*>*element*](http://www.w3school.com.cn/cssref/selector_element_gt.asp) | div>p | 选择父元素为 <div> 元素的所有 <p> 元素。  |  2   |
| [*element*+*element*](http://www.w3school.com.cn/cssref/selector_element_plus.asp) | div+p | 选择紧接在 <div> 元素之后的所有 <p> 元素。 |  2   |

摘自 [CSS 选择器参考手册](http://www.w3school.com.cn/cssref/css_selectors.asp) ，之前我一直以为空格表示同时选择多个选择器，这是与逗号相混淆了。

### Jekyll里的CSS修改

引用的样式 -  HTML 里引用标签叫做 <blockquote> ，实现引用样式的基本原理就是：

```css
blockquote {
    font-size: small;
	background:#f9f9f9;
	border-left:0.4em dotted #ccc;
	margin:.1em;
	padding:.3em;
	quotes:"\201C""\201D""\2018""\2019";
}
blockquote p {
    font-family: "Microsoft YaHei UI Light";
}
```

基本思路是：设置背景颜色以及左边框颜色及宽度，从而形成区分，其中 dotted 指点状边框，还可以选用其他样式（参考 MDN [border-style](https://developer.mozilla.org/en-US/docs/Web/CSS/border-style) ），如

- dashed 虚线
- double 双线
- groove 内嵌式 3D
- ridge 外凸式 3D
- solid 实心线

由于生成 HTML 时实际的 <blockquote> 之中还会添加 <p> 标签，所以使用 CSS 选择器中 blockquote p {} 的形式，只选中引用块内部的 <p> 。

参考以上就可以定义自己喜欢的引用样式了。

### 其他

我发现 code 段在 jekyll 会自动匹配  highlighter-rouge 样式，但是目前可能还未配置好，没有高亮显示。并且缩进和空格显示的长度会有区别，另外 CSS 中的 quotes 语法我不是很明白，大概的意思是设定其内容的引用符号，如单引号、双引号之类的，看到的例子多数是下面这样：

```css
<style>
q:lang(en){quotes:'[' ']' "<" ">";}
q:lang(zh-cn){quotes:"«" "»" '"' '"';}
</style>
```

```HTML
<p lang="en"><q>Quote me <q>Quote me</q> Quote me!</q></p>
<p lang="zh-cn"><q>Quote me <q>Quote me</q> Quote me!</q></p>
```

##其他内容

### 小狼毫/鼠须管

利器推荐了一个新的输入法：小狼毫，据说配置有些麻烦，但是隐私保护比较好，我便下载了试一试，在此记录一下，有时间仔细的配置一下。现在能用上基本的小鹤双拼，具体细致的修改我还不知道。附上教程：[致第一次安装RIME的你](https://www.zybuluo.com/eternity/note/81763) 。已收入印象笔记。 [GitHub 文档](https://github.com/rime/home/wiki/Introduction) 。

问题：在 Typora 可以很好的切换输入法，但是在浏览器中 Ctrl + C 就不起作用了。