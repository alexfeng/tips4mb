#find file on mac

due to the bug on Finder ,new a file though terminal but not appear in Finder. 

Or sometimes,delete a file by terminal , it still exist in Finder.


## restart Finder

```
killall Finder
```

## find file by **Tree**

Tree can show file in which folder.

```
tree -f | grep 'strtok.md'
```

add 'f' to show **F**ullfilepath

use grep to find which file you want to search.

## find file  by erverything(in PD)

1. remove the share folder
2. add the shrenare folder 
3. click "*apply*"
4. wait for a minute and then search what you want.
