---
layout: post 
title: "所丫日报"
date: 2016-05-14
category: soyainedaily
excerpt: "学习笔记 CSS布局-position float z-index，其他想法"
---

## 学习笔记

### CSS 布局

#### Position

下面是摘抄于 [Learn to Code Advanced HTML & CSS](http://learn.shayhowe.com/advanced-html-css/detailed-css-positioning/) 的讲解：

##### **How Box Offset Properties Work**

> The box offset properties, `top`, `right`, `bottom`, and `left`, specify how elements may be positioned, and in which direction. 
>
> These offset properties only work on elements with a `relative`, `absolute`, or `fixed` positioning value.
>
> For relatively positioned elements, these properties specify how an element should be moved from its default position. 
>
> For elements using `absolute` or `fixed` positioning these properties specify the distance between the element and the edges of its parent element. 

虽然对于不同的属性类型偏移量的作用规律是一样的，但是作者却分开来讲，或许是这两者的角度不同，对于 `relative` 来说，这几个值设定的是元素相对于**原位置**的偏移量，而对于 `absolute` 和 `fixed` 来说，设定的是相对距离。一个动态，一个静态，可能是其中的区别所在。

##### **Position Relative**

> These values cause the boxes to overlap one another, yet do not push each other in different directions.
>
> When an element is positioned relatively the surrounding elements will observe the relatively positioned elements default position.

被设定为 `relative` 的元素，元素的偏移量对于文档流中其他元素没有影响，其他元素的布局依照的仍然是这个元素的默认原位置。

对于同一个元素，同时声明的不同方向偏移量也存在优先级：

> In the event that the `top` and `bottom` box offset properties are both declared on a relatively positioned element, the `top` properties will take priority. 
>
> Additionally, if both the `left` and `right` box offset properties are declared on a relatively positioned element, priority is given in the direction in which the language of the page is written. 
>
> For example, English pages the `left` offset property is given priority, and for Arabic pages the `right` offset property is given priority.

`top` 优先，但左右则根据 HTML 所用语言的不同而不同。英语是左优先，中文-没连上网还没查。

##### **Position Absolute**

`absolute` 的元素不在正常的文档流中，直接根据其 relatively or absolutely positioned 的父元素来定位，不存在这样的父元素，则根据 `body` 来定位。

> Absolutely positioned elements accept box offset properties, however they are removed from the normal flow of the document.

当元素没有声明长度宽度时，根据四个偏移量来确定其大小。原话如下：

> If an element doesn’t have a specific `height` or `width` and is absolutely positioned, using a combination of the `top` and `bottom` box offset properties displays an element with a height spanning（可理解为生成） the entire specified size.
>
> ...
>
> Using all four box offset properties will display an element with a full specified height and width.

##### **Position Fixed**

不支持 IE6。

> Notice how both `left` and `right` box offset properties are declared. This allows the `footer` to span the entire width of the bottom of the page, and it does so without disrupting the box model, allowing margins, borders, and padding to be applied freely.

在未声明长度宽度时，运用 `fixed` 将上下左右的距离都设为 0 ，可以自动填满整个视窗。效果类似于吸附。可灵活应用于其他地方，如 header 、 footer 、 sidebar 等。

#### 清除浮动 Containing floats

##### 简单讲解

摘抄一些简单的讲解如下。来源 https://segmentfault.com/a/1190000004237437

浮动带来的负面影响有：

> （1）：背景不能显示 （2）：边框不能撑开 （3）：margin 设置值不能正确显示

三种清除浮动的简单方法：

1. 在父 div 中加入一个新的子元素，样式设置为 `clear: both;`

2. 把父 div 的样式定义为 `overflow: auto;`

3. 对父 div 设置  `div:after { clear: both;  content: "";  display: block;   visibility:hidden; }`

4. > 其中 `clear:both;` 指清除所有浮动；
   >
   > `display:block;` 对于 FF/chrome/opera/IE8 不能缺少，
   >
   > 其中 content 可以取值也可以为 `content: '.';`
   >
   > `visibility: hidden;` 的作用是允许浏览器渲染它，但是不显示出来，这样才能实现清除浮动。 

以上只是一些简单的方法，更深的水在 http://stackoverflow.com/questions/211383/which-method-of-clearfix-is-best ，但目前我还无法完全理解。

##### 详细版-from Learn to Code Advanced HTML & CSS

看[另一篇文章](http://learn.shayhowe.com/advanced-html-css/detailed-css-positioning/)讲浮动，记录如下。作者介绍了两种清除浮动的方法： The Overflow Technique 和 The Clearfix Technique 。

**1.The Overflow Technique**

运用 `overflow: auto;` 来清除浮动时，为避免出现滚动条则可以用 `hidden` ，但可能会出现的意想不到的错误是，当添加的效果超出父元素时，多余部分会被截掉，而这有可能会被截去有用的部分。

> For example, when adding styles or moving nested elements that span outside of the parent, like when trying to implement box shadows and dropdown menus. 

同时不同的浏览器对 overflow 的实现效果不同，我在三个不同的浏览器中查看作者给的例子。发现的区别是显示父元素的长度不同，Chrome 会多显示一部分阴影，而 Firefox 和 Edge 则会因为父元素的高而将阴影完全截去。但我不确定这是不是最主要的区别。

**2.The Clearfix Technique** 

这种方法的原理是用 `:before` `:after` 来作用与父元素，使其产生隐藏的伪元素。

> Using these pseudo-elements we can create hidden elements above and below the parent containing the floats. 

`:before` 和 `:after` 的区别是：

> The `:before` pseudo-element is used to prevent the top margin of child elements from collapsing by creating an anonymous table-cell element using the `display: table;` This also helps ensure consistency within Internet Explorer 6 and 7. 



> The `:after` pseudo-element is used to prevent the bottom margin of child elements from collapsing, as well as to clear the nested floats.

`:before` 通过以 table 的形式来 display ，以防止子元素的 top margin 被折叠（ collapse 有坍塌、折叠的意思，但用在这里好像都不太合适）

`:after`  防止子元素的 bottom margin 被折，同时清除浮动。

**Effectively Containing Floats**

作者说选择何种方式取决于内容和个人。但有种公认的用法是申明一个 group 的 class ，对需要清除浮动的元素采用这个样式，但要注意， group 应作用于需要清除浮动的**父元素**。代码如下：

> ```css
> .group:before,
> .group:after {
> content: "";
> display: table;
> }
> .group:after {
> clear: both;
> }
> .group {
> *zoom: 1; //为 IE6/7 所写
> }
> ```

目前针对单个元素 `:before`  和 `:after` 是无效的。作者原话如下：

> It is worth noting only one `:before` and one `:after` pseudo-element are allowed per element, for the time being. When trying to use the clearfix technique with other `:before` and `:after` pseudo-element content you may not achieve the desired outcome.



#### Z-Index Property

> Elements coming at the top of the DOM are positioned behind elements coming after them.
>
> The element with the highest `z-index` value will appear on the top regardless of its placement in the DOM.
>
> In order to apply the `z-index` property to an element, you must first apply a `position` value of `relative`, `absolute`, or `fixed`. Same as if you were to apply and box off set properties.

我试了一下，其中不设置 `z-index` 时，与设置 `z-index: 0;` 是一样的，而元素之间的堆叠顺序，则是比较数字的大小来确认，可以理解为默认 `z-index: 0;` ，而数字越大就叠在上面。不同的数字等级交叉之间则在实际应用时观察即可。

------

上面这些是看参考资料时记录的笔记，用时 4h 58m ，新任务是要进行居中布局，然而看完这篇教程之后，虽然期间试过一些设置，但仍然没有实现垂直居中的效果，突然有种「道理都懂，可还是过不好这一生」的同感……不过这些资料让我对 CSS 的布局有了更深的理解，至于垂直居中，想必是在这些的基础上灵活运用来实现的。另外 [Learn to Code Advanced HTML & CSS](http://learn.shayhowe.com/advanced-html-css/detailed-css-positioning/) 这是一本很棒的课程（还是应该说书？）网站上以文章的形式来写的，同时也提供纸质版本，讲得很细致易懂。

写到这里突然发现，其实在阅读的过程中有些例子是我不懂的，因为没有及时标记下来，到现在已经回想不起了，于是就以为自己全都懂了……以后记得记录。

## 其他想法

发现一个有意思的事情，情绪低落的时候，演奏欢快的曲子，能让人的心情跟着「飞舞」起来，我可以有意识地多攒点欢快的谱，不开心了拿出来吹一吹，可以调整情绪。