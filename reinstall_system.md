
不丢失已有磁盘的数据重装系统.

(不丢失的数据大概有:已安装的应用,完整的User目录)

# 整个过程


1. 首先command+r 进入恢复系统,

2. 命令重置密码 restpassword

3. 重启,看是否成功.

4. 不能启动的话,继续.

5. command+r 进入恢复系统,在线下载恢复系统.

6. 网速太慢? 从其他地方快速下载系统.

## 制作U盘启动盘.(6G就够了.)

1)使用磁盘工具, 格式化U盘,(可分区可不分区)

2)插上U盘,

3)从下载的系统包内容里找到createinstallmedia命令工具

4)将系统写入U盘

5)执行命令

```
/Users/[os_user_name]/Desktop/createinstallmedia --volume /Volumes/[u_disk_name] --applicationpath /Applications/"Install OS X Yosemite.app" [--force]
```

其中

-  [os_user_name] 本机名称

- [u_disk_name]U盘的名称

- [Install OS X Yosemite.app] 系统名称


7) 恢复系统:

a. 重启电脑

b.按住option

c.选择U盘启动

d.等待30分钟.(会自动重启一次)

8).完成.



=====

## 备份数据方法

 - command + r 进入恢复系统.

- 使用终端可以cp复制文件.

```
cp -v source_dir_file dst_dir

```

- 删除文件

```
rm -rfv source_dir_file
```


备份数据也可以使用磁盘工具>文件>镜像文件来备份.选择合适的位置就好了.







