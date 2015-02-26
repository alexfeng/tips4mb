## 查看下载历史记录


历史记录位于数据库

` ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* `

### 使用软件打开


~~~objectivec
> open -a MesaSQLite  ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* 
~~~


### 使用命令行打开

~~~objectivec
sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* 'select LSQuarantineDataURLString from LSQuarantineEvent'
~~~


### 删除所有下载历史记录

~~~objectivec
> sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* 'delete from LSQuarantineEvent'
~~~

---


> 注意
> 
> > `>`为命令提示符,命令中的引号为英文单引号.
> > 


## 参考资料

- http://www.xitongzhijia.net/xtjc/20150204/37106.html
- http://www.macx.cn/thread-2054947-1-1.html