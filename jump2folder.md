#jump2folder

	从terminal跳转到Finder中的目录。


正确的方法是：
1.在applescripteb编辑器里复制：

```
try
	tell application "Finder"
		set this_folder to (folder of the front window) as alias
	end tell
on error
	set the this_folder to path to desktop folder as alias
end try

set full_path to POSIX path of this_folder
```
 

2.保存文件为
```
GetCurrentFinderFolder.scpt
```

> 直接touch的scpt文件和用编辑器新建的文件是不同的。

3.修改
.bash_profile
.bashrc
/etc/profile
三个文件之中的一个都可以。

4.添加

```
alias cwd="cd \`osascript $HOME/Documents/scripts/GetCurrentFinderFolder.scpt\`"

```