
OS X向多个文件插入多行数据的使用：

~~~bash
find . -d 1 -name "*.txt"  | while read file; do sed -i '' -e '1i \
line_AAA \
line_BBB ' $file; done
~~~

