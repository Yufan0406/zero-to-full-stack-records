# 了解你的终端

## Windows 终端操作基本命令

- `cd new_dir`：更改目录至new_dir
  - 支持相对位置描述：`..`表示上一级目录，`./`表示当前目录，`~`表示用户目录，`/`表示根目录
- `ls`：列出当前目录下的文件和子目录
  - `-Force`：显示隐藏文件和目录
- `pwd`：显示当前目录的绝对路径
- `mkdir new_dir`：创建目录new_dir
- `rmdir new_dir`：删除目录new_dir
- `ni/new-item file`：创建文件file
- `rm/del/Remove-Item file`：删除文件file
  - `-Recurse`：递归删除目录及其内部内容
  - `-Force`：强制删除，不提示确认
- `ren old_file new_file`：重命名文件old_file为new_file
- `copy file1 dir`：复制文件file1到dir
- `move file1 dir`：移动文件file1到dir
- `dir`：显示当前目录下的文件和子目录
- `type file`：显示文件file的内容
  - powershell中支持`cat file`命令来查看文件
- `start file`：打开文件file

Tips：Windows上可以安装最新推出的Coreutils，便可以使用unix风格命令（粗暴点说就是与MacOS上一致的命令）

## Vim的基本操作

- `i`：进入插入模式
- `Esc`：退出插入模式
- `:`：进入命令模式
  - `w`：写入文件并保存
  - `q`：退出
  - `q!`：强制退出，不保存
  - `p`：粘贴
