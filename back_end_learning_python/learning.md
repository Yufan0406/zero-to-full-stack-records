# 后端入门

相对于前端，后端是软件开发中的一个重要组成部分，负责处理用户请求、数据存储、业务逻辑等。后端开发需要掌握多种编程语言和工具，包括但不限于Python、Java、C++、JavaScript等。

要想将后端的运算结果/所存储的数据/结果通过前端进行展示，需要使用到API（Application Programming Interface）。

前后端分离开发产品的运行流程：用户在前端交互，让前端发送请求-通过API-后端处理请求-通过API返回结果-前端展示结果

## API

引入：`curl sites/ip`能够向对应网站发送请求，获取响应信息。

- 在较低版本的windows PowerShell中，`curl`实际是`Invoke-WebRequest`命令的别名，在较新的版本中，`curl`则直接指代原生`curl`命令。因此在调用原生`curl`命令时，通常需要安装并调用`curl.exe`。

API的意义：API是应用程序编程接口，用于定义软件应用程序之间的交互方式。每个程序通过API这样一个入口，持续对外提供自身软件功能。只要遵循这个接口标准，就可以实现不同底层代码的软件间的交互。

- 基本调用标准：URL + HTTP Method + Request Body
  - HTTP Method：GET、POST、PUT、DELETE、PATCH、HEAD、OPTIONS等调用方式
  - Request Body：请求体是HTTP请求中包含的数据，用于传递请求参数、文件等信息。常见的请求体格式有JSON、XML、form-data等。
  
AI Agent：AI Agent是人工智能助手，能够帮助用户完成各种任务。底层上，当涉及联网工作内容，实际上就是调用网络API，获取相应数据。对于本机内操作，实际上就是调用本地包的固定接口，使用这些包/工具的现成能力。

### HTTP协议以及API创建

调用方发出请求、被调用方响应，所传输的内容都必须遵循HTTP协议规范，包括请求方法、请求头、请求体、响应状态码、响应头、响应体等。

- HTTPS实际上就是在HTTP协议的基础上，使用SSL/TLS加密协议，确保数据传输的安全性。HTTPS下的requests和response仍要遵循HTTP协议规范。
- 一般而言，调用方能够通过调用工具帮助发送规范的requests。而被调用方相对而言需要做好对应的响应规范。
- 服务方每当受到请求时，服务器都能够获取请求信息，并会做好日志记录，以便后续分析和调试。
  - 但实际上用户方可以通过修改请求头，来“欺骗”服务端。

#### 基本格式

request/请求：

- 请求行（**必须要读取**）：方法 + 路径 + 协议版本，例如`GET /api/users HTTP/2`
  - 通常使用`curl`默认会自动使用GET方法，但若存在-d、-F等请求体数据参数时，就会默认使用POST方法。
  - 方法描述的是“意图”，是请求服务端如何进行操作。GET方法只是用于获取数据，而POST方法则用于提交数据交由服务端进行处理。
- 请求头：若干行附加说明，以键值对的形式表示，例如`User-Agent: Mozilla/5.0`。
- 空行：用于分隔请求头和请求体。
- 请求体：提交给响应端的内容，例如JSON格式的用户信息。该内容并非必须。

response/响应：

- 状态行（**必须要写清**）：状态码-不同代码对应的含义，例如`200 OK`、`404 Not Found`（通常是指请求方问题）、`500 Internal Server Error`（通常是服务方问题）等。
- 响应头：反馈给调用方的附加信息，最为重要的是`Content-Type`（**规范上可有可无，但实践上需要写**），用于指示响应内容的格式。
  - 如果不将这块写清楚（响应的格式、对应的字符编码等等），那么调用方可能无法正确解析响应内容，比如在浏览器中无法正常渲染出html页面。
- 空行（**必须要写，用于分离请求体和响应头**）
- 响应体（**规范上也是可有可无，但实践中必须写**）：响应正文内容，在终端和浏览器所显示的主要就是此内容。

通常使用`curl -v sites/ip`来查看请求和响应的详细信息，包括请求头、响应头、请求体和响应体等。其中`>`表示请求体，`<`表示响应体。`*`后内容则可以视为注释和旁白。

## Python及其环境管理

同一机器上允许安装多个版本的Python，使用不同版本的Python时可以通过`path/python.exe (command)`或者`python3.X (command)`来指定使用哪个版本的Python。

默认情况下，Python的第三方库会直接安装在对应版本的Python目录下，不会跟随项目需求变动。因此，为了确保项目能够正确运行，需要使用虚拟环境来管理Python的第三方库。

- 虚拟环境：虚拟环境是一种隔离的Python环境，可以独立安装和管理第三方库，不会影响系统上的其他Python环境。
- `venv`：Python自带的虚拟环境模块，可以方便地创建和管理虚拟环境。其能够在每个项目中创建一个`.venv`目录，用于存储虚拟环境的依赖包。在进入到对应项目根目录后，我们使用以下命令来创建和激活、退出虚拟环境。
  - `python -m venv .venv`：创建一个名称为`.venv`的虚拟环境，并将其安装在当前目录下。命名可以修改，但`.venv`是约定俗成的命名方式。
    - 为了避免混淆，可以通过`python -m venv --prompt = myenv .venv`来添加`myenv`的提示符，便于区分不同的虚拟环境。
  - `source .venv/bin/activate`：激活虚拟环境，使得当前命令行使用虚拟环境中的Python和第三方库。
    - windows：使用`.\venv\Scripts\Activate.ps1`。
  - `deactivate`：退出虚拟环境，恢复到系统默认的Python环境。
  - 对应的Python版本取决于创建环境时所调用的版本。
  - 由于venv所创的虚拟环境是跟随项目的，因此在Vibe Coding时代会更方便让AI读取项目信息并进行操作。
- `conda`：conda是Anaconda提供的包管理器，可以方便地创建和管理虚拟环境。能够在项目中直接设定所需的conda环境以及对应的解释器，无需手动创建虚拟环境。
  - 安装Anaconda后会默认开启conda环境，可以直接使用conda命令来创建和管理虚拟环境。
  - `conda create -n myenv python=3.8`：创建一个名称为`myenv`的conda环境，并指定Python版本为3.8。
  - `conda activate myenv`：激活conda环境，使得当前命令行使用conda环境中的Python和第三方库。
  - `conda deactivate`：退出conda环境，恢复到系统默认的Python环境。

- `pip`：相当于`npm`在前端开发中的作用，用于安装和管理Python的第三方库。在虚拟环境中使用pip时，pip会自动将库安装在虚拟环境的site-packages目录下，不会影响系统上的其他Python环境。
  - `pip install requests`：安装requests库。
  - `pip uninstall requests`：卸载requests库。
  - `pip list`：列出当前虚拟环境中安装的所有库。
  - `pip freeze > requirements.txt`：将当前环境中安装的所有库的版本信息保存到requirements.txt文件中，便于后续安装相同版本的库。
  - `pip install -r requirements.txt`：从requirements.txt文件中安装所有库。
  - `pip show requests`：查看requests库的详细信息。
  - `pip search requests`：搜索requests库的相关信息。
  - `pip install requests==2.25.1`：安装特定版本的requests库。
