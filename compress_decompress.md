# compress or decompree file tar/gz/bz2/bz/tar.bz/tar.Z/zip/rar

* tar

decompress:

```
tar xvf FileName.tar 
```

pack:(*not compress*)

```
tar cvf FileName.tar DirName
```

* gz

decompress:

```
gunzip FileName.gz
gzip -d Filename.gz

```

* .tar.gz/.tgz

decompress:

```
tar zxvf FileName.tar.gz
```
compress:

```
tar zcvf FileName.tar.gz DirName
```

* bz2

decompress:

```
bzip2 -d FileName.bz2
bunzip2 FileName.bz2
```
compress:

```
bzip2 -z FileName
```

* bz

decompress:

```
bzip2 -d FileName.bz
bunzip2 FileName.bz
```

* tar.bz

decompress:

```
tar jxvf fileName.tar.bz
```

* zip

decompress:

```
unzip FileName.zip
```

compress:

```
zip filename.zip dirname
```

* rar

decompress:

```
rar x filename 
```
compress:

```
zip filename.rar dirname
```


