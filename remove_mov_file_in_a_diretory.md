
找出指定目录下的指定后缀的文件，然后删除。

~~~objectivec
find file_path -name "*.mov" -print0 | xargs -n 10 -0 rm -rf
~~~

例如，当然目录

~~~objectivec
find . -name "*.mov" -print0 | xargs -n 10 -0 rm -rf
~~~