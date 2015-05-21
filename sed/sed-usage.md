
## 查找每行,替换第一次出现


```
zx:sed zx$ cat myfile.txt 
foo bar foo bar
foo bar foo bar
foo bar foo bar

zx:sed zx$ sed -e 's/foo/bar/' myfile.txt 
bar bar foo bar
bar bar foo bar
bar bar foo bar

```
## 查找每行,替换所有出现

```
zx:sed zx$ sed -e 's/foo/bar/g' myfile.txt 
bar bar bar bar
bar bar bar bar
bar bar bar bar
```

## 查找指定行,替换所有出现

```
zx:sed zx$ sed -e '1,2s/foo/bar/g' myfile.txt 
bar bar bar bar
bar bar bar bar
foo bar foo bar
```


## 查找指定行,替换所有出现:空格替换

```
zx:sed zx$ sed -e '1,2s/ /bar/g' myfile.txt 
foobarbarbarfoobarbar
foobarbarbarfoobarbar
foo bar foo bar
```


## 使用管道输入,替换所有出现:空格替换

```
zx:sed zx$ echo "WWDC 2014 Session 226 - What's New in Table and Collection Views - ASCIIwwdc.pdf" | sed -e 's/ /-/g'
WWDC-2014-Session-226---What's-New-in-Table-and-Collection-Views---ASCIIwwdc.p
```

```
zx:sed zx$ echo "what is this?" | sed -e 's/[ ]/-/g'
what-is-this?
```

## 使用正则表达式替换

(行开头是空行,行结尾是END)

```
zx:sed zx$ cat myfile.txt 
foo bar foo bar
foo bar foo bar
foo bar foo bar

this is line 4 END

that is line 5 END

this is line 6 END
zx:sed zx$ sed -e '/^$/,/^END/s/this/thiiss/g' myfile.txt 
foo bar foo bar
foo bar foo bar
foo bar foo bar

thiiss is line 4 END

that is line 5 END

thiiss is line 6 END
```

##  自定义分割符号

```
zx:sed zx$ cat myfile.txt 
foo bar foo bar
foo bar foo bar
foo bar foo bar

/usr/bin  /usr/local  /usr/lib /usr/share

/usr/bin  /usr/local  /usr/lib /usr/share
zx:sed zx$ sed -e 's:/usr/bin:/usr/biinn:g' myfile.txt 
foo bar foo bar
foo bar foo bar
foo bar foo bar

/usr/biinn  /usr/local  /usr/lib /usr/share

/usr/biinn  /usr/local  /usr/lib /usr/share
```

## 替换html节点 (排除字符)

```
zx:sed zx$ cat myfile.html 
<html>
	<head>
	</head>
	<body>
		<h1>
			hello world!
		</h1>
	</body>
</html>
zx:sed zx$ sed -e 's/<.*>/<node>/g' myfile.html 
<node>
	<node>
	<node>
	<node>
		<node>
			hello world!
		<node>
	<node>
<node>
```

> 有问题的替换

```
zx:sed zx$ echo "<b>This</b> is what <b>I</b> meant." | sed -e 's/<.*>//g'
 meant.
```

> 改进

```
zx:sed zx$ echo "<b>This</b> is what <b>I</b> meant." | sed -e 's/<[^>]*>//g' 
This is what I meant.
zx:sed zx$ 
```

> [^>]* 表示,不是>,匹配0次或多次


## 在匹配处周围插入字符

```
zx:sed zx$ echo "what is this?" | sed -e 's/.*/ zxSay:/'
 zxSay:
zx:sed zx$ echo "what is this?" | sed -e 's/.*/ zxSay:&/'
 zxSay:what is this?
zx:sed zx$ echo "what is this?" | sed -e 's/.*/ zx&Say:/'
 zxwhat is this?Say:
zx:sed zx$ echo "what is this?" | sed -e 's/.*/ &zxSay:/'
 what is this?zxSay:
```



```
^ 	行首定位
$	行尾定位
\<	词首定位
\> 词尾部定位
.	匹配一个字符
*	匹配0个或多个前一个字符
[]	匹配一组,例如[a-z],[0-9]
[^] 匹配不在指定范围内的字符
x\{m,n\} 匹配出现m到n个x
\	转义字符
\(...)\	创建一个标签,标签从1到9,最多9个.使用\1到\9来引用这些标签
```

```
zx:sed zx$ echo "what is this?" | sed -e 's/\(what\) /a\1b/g' 
awhatbis this?
zx:sed zx$ echo "what is this?" | sed -e 's/\(what\) /m\1n/g' 
mwhatnis this?
zx:sed zx$ echo "what is this?" | sed -e 's/\(what\) /m\1n /g' 
mwhatn is this?
zx:sed zx$ echo "what is this?" | sed -e 's/\(what\)/m\1n/g' 
mwhatn is this?
```


~~~shell
zx:sed zx$ cat abc.txt 
foo bar oni
eeny meeny miny
larry curly moe
jimmy the weasel
zx:sed zx$ sed -e 's/\(.*\) \(.*\) \(.*\)/A-and-B: \1-\2 WIN-C:\3/' abc.txt 
A-and-B: foo-bar WIN-C:oni
A-and-B: eeny-meeny WIN-C:miny
A-and-B: larry-curly WIN-C:moe
A-and-B: jimmy-the WIN-C:weasel
~~~

## 删除匹配行


> sed -ie '/LNLog/d' output.md

其中

- i表示对文件进行操作,否则不会更改源文件
- e表示命令
- LNLog表示匹配的内容
- d表示删除
- output.md表示文件名

下面是示例:

```
zx:map zx$ cat  output.md
-(void)fadeInTableView{
    LNLog(@"%s [LINE:%d]", __func__, __LINE__);
    [_activityIndicator stopAnimating];
    [UIView animateWithDuration:1.0f animations:^{
        _loadingTipsView.alpha = 1;
    } completion:^(BOOL finished) {
        _loadingTipsView.alpha = 0;
    }];
}

-(void)fadeInLoadingView{
    LNLog(@"%s [LINE:%d]", __func__, __LINE__);
    [_activityIndicator startAnimating];
    [UIView animateWithDuration:1.0f animations:^{
        _loadingTipsView.alpha = 0;
    } completion:^(BOOL finished) {
        _loadingTipsView.alpha = 1;
    }];
}zx:map zx$sed -ie '/LNLog/d' output.md 
zx:map zx$ cat output.md
-(void)fadeInTableView{
    [_activityIndicator stopAnimating];
    [UIView animateWithDuration:1.0f animations:^{
        _loadingTipsView.alpha = 1;
    } completion:^(BOOL finished) {
        _loadingTipsView.alpha = 0;
    }];
}

-(void)fadeInLoadingView{
    [_activityIndicator startAnimating];
    [UIView animateWithDuration:1.0f animations:^{
        _loadingTipsView.alpha = 0;
    } completion:^(BOOL finished) {
        _loadingTipsView.alpha = 1;
    }];
}
zx:map zx$ 
```


