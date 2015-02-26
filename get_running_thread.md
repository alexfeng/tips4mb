显示Linux所有正在运行的进程

ps命令
输入下面的ps命令，显示所有运行中的进程：
# ps aux | less
其中，
-A：显示所有进程
a：显示终端中包括其它用户的所有进程
x：显示无控制终端的进程
任务：查看系统中的每个进程。
# ps -A
# ps -e
任务：查看非root运行的进程
# ps -U root -u root -N
任务：查看用户vivek运行的进程
# ps -u vivek
任务：top命令
top命令提供了运行中系统的动态实时视图。在命令提示行中输入top：
# top
 
任务：显示进程的树状图。
pstree以树状显示正在运行的进程。树的根节点为pid或init。如果指定了用户名，进程树将以用户所拥有的进程作为根节点。
$ pstree
 
任务：使用ps列印进程树
# ps -ejH
# ps axjf
任务：获得线程信息
输入下列命令：
# ps -eLf
# ps axms
任务：获得安全信息
输入下列命令：
# ps -eo euser,ruser,suser,fuser,f,comm,label
# ps axZ
# ps -eM
任务：将进程快照储存到文件中
输入下列命令：
# top -b -n1 > /tmp/process.log
你也可以将结果通过邮件发给自己：
# top -b -n1 | mail -s 'Process snapshot' you@example.com
任务：查找进程
使用pgrep命令。pgrep能查找当前正在运行的进程并列出符合条件的进程ID。例如显示firefox的进程ID：
$ pgrep firefox
下面命令将显示进程名为sshd、所有者为root的进程。
$ pgrep -u root sshd
向htop和atop说hello
htop是一个类似top的交互式进程查看工具，但是可以垂直和水平滚动来查看所有进程和他们的命令行。进程的相关操作（killing，renicing）不需要输入PID。要安装htop输入命令：
# apt-get install htop
或
# yum install htop
在命令提示行中输入htop：
# htop
atop工具
atop是一个用来查看Linux系统负载的交互式监控工具。它能展现系统层级的关键硬件资源（从性能角度）的使用情况，如CPU、内存、硬盘和网络。
它也可以根据进程层级的CPU和内存负载显示哪个进程造成了特定的负载；如果已经安装内核补丁可以显示每个进程的硬盘和网络负载。输入下面的命令启动atop：
# atop