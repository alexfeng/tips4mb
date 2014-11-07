short_command use alias

```
open /Application/Mou.app file_name_here
```

use alias, we can write

```
# /etc/profile
alias mou='open /Application/Mou.app'
```

> sudo vi /etc/profile



finally:

we can use 

```
mou file_name
```
to open markdown file.

---


```
#open Mou filename
alias mou='open /Applications/Mou.app ' 

#open TextEdit filename.c 
alias te='open /Applications/TextEdit.app ' 

#take a screenshot:
# -W window mode -P preview after screenshot -S noShodow 
alias sc='screencapture -iW -P -S  ' 

```

