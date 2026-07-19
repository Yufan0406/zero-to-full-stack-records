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

## 现代前端开发入门

### 开发痛点

- javascript的模块化是现代前端开发的迈进，但模块化后网页的预览必须需要服务器支持；同时多模块会使得浏览器发送多个请求，进程变慢
- 此外浏览器自身还有缓存，更改文件后再次刷新页面时浏览器会优先使用缓存，导致页面显示不及时。
- 矛盾三角：工程治理（强调复杂项目下的规范性）-开发效率（开发者的体验和便利性）-用户体验（用户使用时的便利性和即时性）
  
### 解决方案：构建工具(Build Tool)

- 功能1：本地跑一个服务器，且支持热更新（热加载）（即修改文件后浏览器自动刷新页面）
- 功能2：自动合并（将多个文件打包成一个文件，减少请求次数）
- 功能3：文件名指纹（即文件名中包含文件的哈希值，防止文件名重复，避免缓存问题）
推荐工具：**Vite**

### Vite入门

- Vite本身是基于JavaScript开发的命令行工具，需要配置对应的运行环境：Node.js
- npm是Node.js的包管理工具，用于安装和管理项目依赖。
  - 不同于ubuntu上apt的全局安装与管理，npm是基于项目进行安装和管理包，每个项目有自己的`package.json`文件，用于记录项目依赖。
  - 使用前通常需要初始化：`npm init -y`，该命令只产生`package.json`文件，是Node.js 项目的“配置总清单”，用于记录项目信息、管理所有依赖包、定义运行脚本，并约束环境版本，确保项目在不同环境下能一致运行。入门时主要关注：
    - `name`：项目名称，必须是唯一的，且不能包含特殊字符。
    - `version`：项目版本号，遵循Semantic Versioning（SemVer）规范，即`MAJOR.MINOR.PATCH`，其中`MAJOR`表示重大更改，`MINOR`表示新增功能，`PATCH`表示修复bug。
    - `script`：定义运行脚本，如`start`用于启动项目，`build`用于构建项目，`test`用于运行测试。
- 通过`npm install -D vite`来安装
  - `-D`表示安装为开发依赖，即只在开发环境中使用，不打包到生产环境中，即上线的网站时不会包含这些依赖包。
  - Tips：Windows上安装时可能会遇到权限问题，可以尝试使用管理员权限运行命令行工具。
- 安装后会产生`node_modules`和`package-lock.json`两个文件，`node_modules`文件中存放了所有安装的依赖包（指定安装包的依赖包也会一并安装），`package-lock.json`文件中记录了所有依赖包的版本信息，用于确保项目在不同环境下能一致运行。
- 如同一般命令一样，`node_modules`下存在一个`vite`文件夹，该文件为Vite的安装目录；其子文件夹`.bin`下同样存在一个`vite`文件，即`node_modules/.bin/vite`，该文件就是Vite的可执行文件，可以使用该地址命令直接进行**开发预览**。
- `node_modules/.bin/vite build`命令可以进行**构建项目**，即打包项目、合并并再生成生产环境所需的文件。这样即可用于解决多模块下发送多个请求的问题，减少请求次数，提高开发效率。
  - 该命令下会生成`dist`文件夹，该文件夹中存放了打包后的文件，包括HTML、CSS、JavaScript等文件，可以用于上线。其中`dist`文件夹下的文件名中包含文件的哈希值，防止文件名重复，避免缓存问题。
    - 重新构建文件时，文件名上的哈希值会自动更新，从而避免缓存问题。
  - 打包后的文件并不能在本地直接运行（实际上内部仍然存在ES模块，即HTML文件中存在`<script type="module">`标签），需要通过`node_modules/.bin/vite preview`**对打包后文件进行预览**。
  - 同时注意到，该命令打包项目时只确认一个入口文件，即`index.html`，因此如果项目中存在多个入口文件，需要在`vite.config.js`文件中进行配置。

主要代码对应流程：

```bash
./node_modules/.bin/vite  # 开发中：跑源码，热更新
./node_modules/.bin/vite build # 考虑上线：打包项目，合并文件，产出服务器所上线版本
./node_modules/.bin/vite preview # 上线前：预览打包后的文件是否正常
```

为了方便调用以上命令，我们可以通过在package.json文件中添加脚本来简化命令调用：

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

这样，我们就可以通过以下命令来调用相应的脚本，实际上对于这个项目我们都可以自定义脚本名和指定对应的命令，并通过`npm run xxx`来调用。通常而言，vite执行时首先会从.bin目录下查找对应的命令，如果找不到则会考虑系统命令。

```bash
npm run dev # dev-开发中：跑源码，热更新
npm run build # build-整合构建，考虑上线：打包项目，合并文件，产出服务器所上线版本
npm run preview # preview-上线前预览检查：预览打包后的文件是否正常
```

Tips：我们之前构建html文件时，部分功能的实现是通过从第三方库官网上拉取代码获得的。但当项目上线后，这些第三方库的代码可能会被删除，因此为了保证项目能够正常运行，我们需要将这些第三方库的代码保存下来。通常我们会将这些第三方库的代码保存在`node_modules`文件夹中，这样在项目上线后，这些第三方库的代码仍然存在，不会被删除。即通过`npm install`命令安装这些第三方库时，npm会自动将这些第三方库的代码保存到`node_modules`文件夹中。

- 此处注意区别于安装vite，这里安装时不会添加`-D`参数，因为此处这些第三方库是作为项目依赖，需要打包到生产环境中。
- 下载好后修改文件内容时，在import时将原本的网址更改为对应库即可
  - 例如：`import anime from 'https://cdn.jsdelivr.net/npm/animejs@4/lib/anime.iife.min.js';` 改为 `import anime from 'animejs';`。在没有vite的情况下，浏览器不支持后者写法，但vite会自动处理这些文件，将这些文件打包到生产环境中。

#### 关于Git的提交

- 一般而言，对于`package.json`和`package-lock.json`是需要提交的，因为这些文件记录了项目的依赖包和版本信息，对于`node_modules`以及`dist`等能够通过命令生成的文件是不需要提交的。