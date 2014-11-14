# diff

-i 忽略大小写

-E 忽略tab引起的不同(有问题？)

-B  忽略空白行引起的不同

-a 对待所有文件为文本文件

-c  单独使用，类似与github的不同文件比较

-q 简单判断两个文件是否相同


-W  number   每行显示多少列，（默认为130）

diff输出格式（默认）：
n1 a n3,n4 表示在文件1的n1行后面添加n3到n4行
n1,n2 d n3 表示在n1到n2行之间删除n3行
n1,n2 c n3,n4 表示把n1,n2行用n3,n4行替换掉
字母a：表示附加（add）
字符c：表示修改（change）
字符d：表示删除（delete）
字母前的是源文件，字母后是目标文件。Nx表示行号。 
以”<”打头的行属于第一个文件，以”>”打头的行属于第二个文件。


常用的比较方式：

```
diff filename_1  filename_2

```


**并排显示，控制列数（列宽）为50列**

```
diff -y -W 50 filename_1 filename_2
```


显示不同之处的上下文(分开显示)

```
diff -c filename_1 filename_2
```

**显示不同之处的上下文（合并显示）**

```
diff -u filename_1 filename_2
```
