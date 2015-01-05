
从内容里使用正则表达

```
zx:grep zx$ cat content.txt  | grep [a-z]
     2	README.md
     3	browser_safari_chrome.md
     4	compress_decompress.md
     5	diff_compare_file.md
     6	disable_enable_dashborad.md
     7	filename-chmod.md
     8	find_file_on_mac_os.md
     9	grep
    10	quich_input_symbol.md
    11	recovery_min_windows.md
    12	restart.md
    13	screencapture_usage.md
    14	short_command_alias.md
    15	showHiddenFiles.md
    16	showStorageOfDiretory.md
    17	solve_command_not_found.md
    18	terminal_tab_usage.md
```





不指定文件类型

```objectivec
grep -E  "#define.*http" ./*	
```
 | sort

指定文件类型

```objectivec
find . -name "*.m" |  xargs  -n 10 grep -inrE "#define.*http"   > x.txt
```

改进(路径中如果带空格的处理)

```objectivec
find . -name "*.m"  -print0 |  xargs  -n 10 -0 grep -inrE "#define.*http"   > x.txt
```



