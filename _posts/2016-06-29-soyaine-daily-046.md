---
layout: post
title: "所丫日报" 
date: 2016-06-29 
category: soyainedaily 
excerpt: ""
---

随手记录今天的学习内容。

查看了一下 `id` 和 `name` 的区别。下面摘抄一下《HTML&CSS》的内容：

> ID ATTRIBUTE
>
> Its value should started with **a letter or an underscore** (not a number or any other character).
>
> The id attribute is known as a **global attribute** because it can used on any element.

在 Stack Overflow 上的回答：

> Use `name` attributes for form controls (such as `<input>` and `<select>` ), as that's the identifier used in the `POST` or `GET` call that happens on form submission.
>
> Use `id` attributes whenever you need to address a particular HTML element with CSS, JavaScript or a fragment identifier. It's possible to look up elements by name, too, but it's simpler and more reliable to look them up by ID.
>
> answered by Warren Young.
>
> The `name` attribute is used when sending data in a form submission. Different controls respond differently. For example, you may have several radio buttons with different `id` attributes, but the same `name`. When submitted, there is just the one value in the response - the radio button you selected.
>
> answered by John Fisher



> ID Attribute
>
> - Valid on any element
> - Each Id should be unique
> - Can be used as anchor reference in URL
> - Is referenced in CSS or URL with # sign
> - Is referenced in JS with `getElementById()`
> - Shares same name space as name attribute
> - Is case sensitive(区分大小写)
>
> Name Attribute
>
> - Valid only on `a`, `form`, `iframe`, `img`, `map`, `input`, `select`, `textarea`
> - Name does not have to be unique
> - Can not be referenced in CSS or URL
> - Is referenced in JS with `getElementByName()` 
> - Shares same name spaces as id attribute
> - Must begin with a letter
> - Is case sensitive
> - Used on form elements to submit information
>
> from [HTML Difference Between Id and Name](http://solidlystated.com/scripting/html-difference-between-id-and-name/)

CSS 的声明顺序应当如下，其中相关的属性要归为一组。

1. Positioning: `position` `top` `right bottom left z-index`
2. Box model: `display float width height`
3. Typographic: `font line-height color text-aligh`
4. Visual: `background-color border border-radius`
5. Misc: `opacity`

class 的命名规则：

> - class  名称中只能出现小写字符和破折号（不是下划线，不是驼峰命名法）。破折号应当用于相关 class 的命名。
> - 使用有组织的或目的明确的名称，不要使用表现形式（presentational）的名称。
> - 基于最近的父 class 或基本 class 作为新的 class 的前缀。
> - 使用 `.js-*` class 来标识行为（与样式相对），并且不要将这些 class 包含到 CSS 文件中。

JSON (JavaScript Object Notation)

轻量级数据交换格式。

已经简单了解了 JSON 的语法和基础，学习如何使用。一搜竟然都是一些零零散散的文章，最后找到了阮一峰的教程。写得很详尽。http://javascript.ruanyifeng.com/stdlib/json.html