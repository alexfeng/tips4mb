#command not found.

for some reason,usually is when we changed the configurationfile ,the command like ls,mv can not use.


## difficulty to solove this problem

* can not show hidden files by Finder
* can not copy hidden files by UDisk 
* sudo command doesnt work
* how to open hidden file?

## Fisrt

I thought it was the only command doen't work,but the fact is that,commands like ls,mv,cp do not work.

## Second

I want to copy configuration file to 'User/[usr_name]/',but,

the configuration file is hidden file. ls command does't work.

## UDisk

can not mount  udisk!oh,my God. so funny.

diskutil can't work.

## solve the problem

1) find the command we need. eg:ls,mv,vi

to achieve this aim,we need to konw where is the command .

```
where ls
where mv 
where rm
where vim
```
thoes command can be run on the mechine that are OK.

2) go to the folder where those commands lies.

a) if the 'cd' command can work,just use it.
b) open finder,
```
command + shift + g
```
go to the folder we want.

3) in the folder in process '2)',those command should be work.

if there is no command we need?

a) ask your friend ,email you one.
b) download the command file from internet.

one word,we need ls,mv,rm,vim  work in the folder above.

4) use 

```
vim /Users/[usr_name]/.hiddenfile
```
to edit the file.

use

```
rm /Users/[usr_name]/.hiddenfile
```
to remove file.

use 
```
mv /Volume/[udisk]/[.hiddefile] /Users/[usr_name]/.hiddenfile
```
to cover the file.

------

problem solved ？