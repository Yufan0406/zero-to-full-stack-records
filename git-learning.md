# Git 入门

Git 是一个分布式版本控制系统，其主要作用是管理代码版本，以及在团队中进行代码协作。

- 版本管理本质上就是做好代码修改前后对比和存档，以便在需要时能够恢复到某个特定版本。

## Git 基本概念

Git 的基本概念与操作包括仓库(repository)、分支(branch)、提交(commit)、合并(merge)等。

- repository：代码仓库，可以理解为一个受到Git管理的文件夹，包含代码文件、提交记录、分支信息等。
  - 由于Git是分布式版本控制系统，因此每个开发者都可以在本地创建自己的仓库，同时也可以将本地仓库内容**通过互联网同步**到其他开发者仓库，因此可以将Git仓库分为本地仓库(local repository)和远程仓库(remote repository)。
- commit：对代码进行手动“存档”，会记录提交时项目中不同文件的状态，以及提交者和提交时间、提交说明等信息。

## Git 使用入门

更详细的命令学习可以参考[廖雪峰老师Git教程](https://liaoxuefeng.com/books/git/introduction/index.html)

- 首次在本地使用git时需要提前配置用户名和邮箱（方便在多人协作时查看修改提交用户信息）可以通过以下命令进行查询和配置、修改：

```bash
git config --global user.name ("Your Name")
git config --global user.email ("your email@example.com")
```

- `git init`：初始化本地仓库，创建一个空的Git仓库，可以使用以下命令：
- `git status`：查看当前仓库的状态，包括哪些文件被修改、哪些文件被暂存、哪些文件未被跟踪等。
- `git add`：将文件添加到暂存区，即选定该文件并准备提交到仓库中。
  - `.`：表示添加当前目录下的所有文件。
- `git commit -m "Your commit message"`：提交暂存区的文件到仓库，并添加提交说明。
- `git push`：将本地仓库内容推送到远程仓库。
- `git log`：查看提交历史记录，包括提交时间、提交者、提交说明等信息。
  - `--oneline`：只显示简短的提交信息。
  - `--graph`：显示提交历史的图形化表示。
  - `--author="Your Name"`：只显示指定作者的提交记录。
  - `--follow`：跟踪文件的移动和重命名。
- `git rm`：本地删除文件，同时将这个操作添加到暂存区，但保留文件在本地。
  - `git rm --cached`：将文件从git暂存区中删除，但保留文件在本地，此时文件在git中的状态将被视为未被跟踪的。
  - `git rm -rf`：删除git以及本地目录中的文件及其子目录。
    - `-r`是递归删除子目录，`-f`是强制删除，不提示确认。
- `git checkout version_id`：查看指定版本的文件内容。
  - `git checkout master(部分用main)`：查看master分支的文件内容。
  - `git checkout -- file_name`：放弃工作区中修改，查看指定文件的最新提交版本or暂存区内容。
- `git switch branch_name`：切换到指定分支；新版本下这个更推荐使用switch命令。
  - `git switch -d commit_id`：切换到指定提交版本。
- `git restore file_name`：等价于`git checkout -- file_name`，新版本更推荐。
  - `--worktree`：清空工作区的修改，但保留暂存区的修改。该参数可以不输入，`git restore`默认执行。
  - `--staged`：清空暂存区的修改，但保留工作区中的修改。
- `git reset --(mode) HEAD~(num)`：撤销前`num`次提交
  - `mode`参数用来控制如何处理工作区以及暂存区中的修改。
    - `soft`：Git中回退到前`num`次提交，但最新一次的提交将被保存在工作区和暂存区中。
    - `mixed`：Git中回退到前`num`次提交，但最新一次的提交只被保存在工作区中。`git reset HEAD~(num)`是其简化形式。
    - `hard`：Git中回退到前`num`次提交，但工作区和暂存区中的所有修改都将被丢弃。
  - `git reset HEAD <file>`：将指定文件重置到指定提交版本，暂存区的修改会回退至工作区。

- `git revert commit_id`：新建一个提交来撤销commit_id对应提交的内容，但会保留commit_id的提交历史记录。

- `git reflog`：查看提交历史记录的引用信息，包括提交ID、提交时间、提交者、提交说明等信息，参数操作类似于`git log`。
  - 如果使用`git reset --hard HEAD~{num}`后需要回退，且没有使用`git gc`清理回收时，可以通过`git reflog`查看到之前的提交ID，然后使用`git reset --hard commit_id`进行回退。
  - 只要`git reflog`中记录还存在，也可以直接通过`git reset --hard HEAD@{num}`来撤销（日志记录中会显示对应的num）

- `git branch`：查看当前仓库的所有分支，包括本地分支和远程分支。
  - `git branch branch_name`：创建新分支但停留在当前分支
    - `git switch -c branch_name`能够实现创建分支并切换的效果
- `git merge branch_name`：将指定分支的最新提交与当前分支的最新提交合并，并将合并结果最新提交到当前分支。

- 有时候部分文件可能不需要被Git跟踪，可以通过创建`.gitignore`，作为一个忽略文件列表文件，用于指定哪些文件或目录不需要被Git跟踪。但这个文件本身需要被git跟踪。
  - 但`.gitignore`只能对还未被跟踪的文件生效。

### 提示

- Git更适合管理代码、配置以及文档这类文本内容（粗浅理解为能够用vscode或者vim直接打开编辑的文件），不适合管理二进制文件（如图片、视频、音频等）。
- 删除仓库只需要删除`.git`文件夹即可，但删除仓库后，本地仓库中的所有文件和提交记录都会丢失，因此在删除仓库前最好先备份。

## 远程同步与GitHub

- 远程仓库：一个能够存放代码以及git提交历史的远程设备。可以是服务器，也可以是**代码托管平台**。
- `git push`：将本地仓库内容推送到远程仓库。
- `git pull`：将远程仓库内容拉取到本地仓库。
- `git clone`：克隆远程仓库到本地，相当于将远程仓库的内容复制到本地仓库中。

### GitHub

一个代码托管平台，提供免费的私有仓库和公共仓库服务，支持多种编程语言，提供代码审查、代码托管等服务

- 对应repo需要配置SSH或者HTTPS访问，为了方便我们使用SSH访问，因为SSH不需要输入密码，而HTTPS需要输入密码。
  - 需要创建SSH密钥对，然后将公钥添加到GitHub账户中。
  - 公钥文件通常位于`~/.ssh/id_rsa.pub`，私钥文件通常位于`~/.ssh/id_rsa`。
  - 使用以下命令生成SSH密钥对：
    - `ssh-keygen -t rsa -C "your email@example.com"`
  - 使用以下命令查询公钥，并添加到GitHub账户中：`cat ~/.ssh/id_rsa.pub`
  - 此时我们可以通过`ssh -T git@github.com`来测试SSH连接是否成功。

- 之后我们可以通过以下命令将本地仓库连接至远程仓库，并将本地仓库内容推送到远程仓库：

```bash
git remote add origin git@github.com:username/repository.git
git branch -M main
git push -u origin main
```

- `git remote add origin`：将远程仓库地址添加到本地仓库中，`origin`是默认的远程仓库名称，可以自定义。
- `git branch -M main`：将本地仓库的默认分支名称强制改为`main`，因为GitHub默认使用`main`作为默认分支名称，如果本地和远程不一致推送时将出现问题。
- `git push -u origin main`：将本地仓库内容推送到远程仓库，并建立本地`main`分支与远程分支的关联，以后push将默认推送到远程的`main`分支。

- `git clone xxxx`：克隆远程仓库到本地，相当于将远程仓库的内容复制到本地仓库中。本地仓库会自动与远程仓库建立联系，从GitHub所拉取的远程仓库本地会默认命名为`origin`，默认分支名称为`main`，如果本地和远程不一致拉取时将出现问题。
  - SSH连接拉取方式：`git clone git@github.com:username/repository.git`
  - HTTPS连接拉取方式：`git clone https://github.com/username/repository.git`，该过程会校验用户名和密码，如果校验失败则无法拉取。
  - 后续再次拉取代码仅需使用`git pull`即可。

#### GitHub的仓库可见性与连接方式

- GitHub的仓库可见性与连接方式会决定访问git远程仓库时的鉴权(Authentication)操作：验证用户是否拥有访问仓库的权限。

|连接方式/可见性|HTTPS|SSH|
|---|---|---|
|公开|不需要鉴权|需要在本机生成SSH密钥并将其加到GitHub账户中，但仅需配置一次|
|私有|每次push/pull都需要校验账号|类比公开情况|
