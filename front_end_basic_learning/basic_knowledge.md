# 前端基础知识

HTML、CSS 和 JavaScript 是前端开发的基础知识，它们分别用于定义网页的结构、样式和交互功能。

HTML 用于定义网页的内容和结构，CSS 用于定义网页的样式，JavaScript 用于定义网页的交互功能。HTML、CSS 和 JavaScript 三者相互配合，共同构建出一个完整的网页。

HTML格式有极强的表达能力。**同时AI训练数据中网页HTML数据是高度丰富的，相较于word、ppt这种文档格式，HTML格式更适配AI处理。**

## HTML

- HTML 是超文本标记语言，用于创建网页的基本结构。
- HTML 使用标签来定义网页的内容，如 `<html>`、`<head>`、`<body>`、`<h1>`、`<p>` 等。其中标签成对出现，标签首尾之间用斜杠 `/` 分隔。
- HTML 标签可以嵌套，形成复杂的网页结构。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>我的网页</title>
</head>
<body>
    <div class="card">
        <h1>欢迎来到我的网页</h1>
        <p id = 'msg'>这是一个简单的网页示例。</p>

        <button onclick="changeMessage()">点击我</button>
    </div>
</body>
</html>
```

- `<!DOCTYPE html>` 声明文档类型为 HTML5。
- `<html lang="zh-CN">` 定义 HTML 文档的根元素，lang 属性指定文档的语言为中文。
- `<head>` 部分包含文档的元数据，如字符编码、标题等。
  - `<meta charset="UTF-8">` 标签定义文件元数据，其中这里具体定义了文档的字符编码为 UTF-8。
  - `<title>` 标签定义网页的标题，显示在浏览器的标签页上。
- `<body>` 部分包含文档的主体内容，如文本、图像、视频等。
  - `<h1>` 和 `<p>` 是 HTML 标签，分别用于定义一级标题和段落。
    - `id` 属性用于唯一标识一个元素，`id` 值必须是唯一的。
  - `<button>` 是 HTML 标签，用于定义一个按钮元素，当用户点击按钮时，会触发 JavaScript 函数。
    - `onclick` 属性用于定义按钮的点击事件，当用户点击按钮时，会调用 `changeMessage()` 函数。
  - `<div>` 是 HTML 标签，用于定义一个块级元素，可以包含其他 HTML 元素，形成复杂的网页结构。

## CSS

- CSS 是层叠样式表，用于定义网页的样式，如颜色、字体、布局等。
- CSS 使用选择器来选择网页元素，并定义样式规则。
- CSS 有内联样式、内部样式表和外部样式表三种方式。
  - 内联样式：直接在 HTML 元素的 `style` 属性中定义样式规则。
  - 内部样式表：在 HTML 文档的 `<head>` 部分嵌入 `<style>` 标签，定义样式规则。
  - 外部样式表：将样式规则写入一个单独的 CSS 文件中，通过 `<link>` 标签引入到 HTML 文档中。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>我的网页</title>
    <style>
        body {
            background-color: lightblue;
        }
        h1 {
            color: darkblue;
        }
        p {
            font-size: 18px;
        }   
    </style>
...
```

- `<style>` 标签定义内部样式表，直接在 HTML 文档中嵌入样式规则，即修改网页的样式。
  - `body` 选择器选择网页的主体部分，定义背景颜色为浅蓝色。
  - `h1` 选择器选择一级标题，定义颜色为深蓝色。
  - `p` 选择器选择段落，定义字体大小为 18px。

## JavaScript

- JavaScript 是一种脚本语言，用于在网页中添加交互功能，如按钮点击事件、表单验证等。
- JavaScript 可以在 HTML 文档中嵌入，也可以通过外部文件引入。
- JavaScript 有事件驱动编程方式，当用户触发事件（如点击按钮）时，JavaScript 会执行相应的代码。

```javascript
<script>
    function changeMessage() {
        var messageElement = document.getElementById('message'); // 获取元素
        messageElement.textContent = '你触发了修改'; // 修改元素内容
      }
</script>
```

- `changeMessage()` 函数定义了一个 JavaScript 函数，当用户点击按钮时，会调用这个函数。
  - `document.getElementById('msg')` 选择器选择 id 为 `msg` 的元素，即段落元素。
  - `messageElement.textContent` 属性用于修改段落元素的文本内容。

### ES模块化

- ES(ECMA Script)是JS的语法标准，ES6（ECMAScript 2015）引入了模块化（module）的概念，使得代码可以更清晰地分离和组织。
- 出发点：提高代码的可维护性和可复用性。（具体问题详见[此内容中有关script标签中`src`的讲解](#结构样式以及交互分离)）
- 基本思想：将每个功能进行独立封装（文件只能访问自己本身），如需要将该文件用于其他文件的访问则需要`export`，其他模块需要通过`import`引入该模块。
- 由于有这种模块化规范，因此从第三方引入时需要注意引入的是es模块化文件而非js文件。此外，`import`本质上是发起一个http请求去加载文件，由于浏览器同源策略(CORS)的限制，当使用`file://` 协议打开文件时，浏览器会阻止跨域请求。
- 同时为了解析`import`和`export`，需要在HTML文件中引入`<script type="module">`标签，这样浏览器才会正确解析。

## 结构、样式以及交互分离

- 当HTML、CSS和JavaScript三者相互配合，共同构建出一个完整的网页时，这个项目规模往往是比较大的，它们的结构、样式和交互功能通常是分离的。
- 同时将三个模块拆分有助于我们更好地理解和维护代码，也便于团队协作和代码复用。
  - 比如对于多个内容页面但样式相同，我们只需要去维护css文件中的样式规则，而不需要在每个页面中重复编写；同样对于多个页面但交互逻辑相同，我们只需要去维护js文件中的交互逻辑，而不需要在每个页面中重复编写。
  
```html
<head>
...
  <link rel="stylesheet" href="styles.css">
...
</head>
<body>
...
  <script src="script.js"></script>
...
</body>
```

- `<link rel="stylesheet" href="styles.css">` 标签引入外部样式表，将样式规则写入一个单独的 CSS 文件中，通过 `<link>` 标签引入到 HTML 文档中。
  - `href` 属性指定 CSS 文件的路径，即 styles.css 文件。
  - `rel` 属性指定链接关系，这里设置为 `stylesheet`，表示这是一个样式表链接。

- `<script src="script.js"></script>` 标签引入外部 JavaScript 文件，将交互功能写入一个单独的 JavaScript 文件中，通过 `<script>` 标签引入到 HTML 文档中。
  - `src` 属性指定 JavaScript 文件的路径，即 script.js 文件。
    - `src`属性同样可以指定网址，例如 `src="https://cdn.jsdelivr.net/npm/animejs@4/lib/anime.iife.min.js"` 引入 anime 第三方库。此方式被称为**CDN(cross-domain network)引入**，即通过网络从远程服务器加载第三方资源，而不是将资源下载到本地。但实际上也可以将这个文件下载到本地，然后通过 `<script src="xxxx.js"></script>` 标签引入到 HTML 文档中，效果相同。
      - 运行的过程理解为：浏览器首先会创建一个window，然后第三方库以及本地js文件都会被加载到这个window中，此时整个页面中涉及的板块都可以访问到这些资源。
        - 这些资源在window上都是全局变量，因此在任何地方都可以访问到这些资源。但正因此，同一个页面中不应该出现两个同名的资源，否则会导致资源覆盖，从而导致代码错误（全局污染），在大型项目中容易出现。
      - 由于代码读取是从上往下，因此对于存在依赖关系的两个资源在编写上就必须要注意排序，否则可能会导致资源加载失败。因而在大型项目构建中就很容易顺序出错（难以完全记录依赖关系以及顺序）。
  