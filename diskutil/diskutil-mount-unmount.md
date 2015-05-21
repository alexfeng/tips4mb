## 命令来加载和弹出部分硬盘

~~~shell
x:~ zx$ diskutil mount HFS
Volume HFS on HFS mounted
zx:~ zx$ diskutil mount NTFS
Volume NTFS on NTFS mounted

zx:~ zx$ diskutil unmount NTFS
Volume NTFS on disk2s2 unmounted
zx:~ zx$ diskutil unmount HFS
Volume HFS on disk2s1 unmounted

~~~


## 加载整块硬盘,或者弹出整块硬盘

~~~shell
zx:~ zx$ diskutil mountDisk HFS
Volume(s) mounted successfully
zx:~ zx$ diskutil unmountDisk HFS
Unmount of all volumes on disk2 was successful
~~~

> 其中,HFS,NTFS是我自己的给某个磁盘命的名.


## 使用文件名(IDENTIFIER)来弹出整块硬盘

> 首先列表,然后弹出文件`/dev/disk2`(弹出成功),拔掉,再次弹出(弹出失败).

~~~shell
zx:~ zx$ diskutil list
/dev/disk0
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *121.3 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:          Apple_CoreStorage                         120.5 GB   disk0s2
   3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3
/dev/disk1
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                  Apple_HFS disk                   *120.1 GB   disk1
                                 Logical Volume on disk0s2
                                 12AC174C-A63E-474C-85EF-1A6C9F2870CC
                                 Unencrypted
/dev/disk2
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *1.0 TB     disk2
   1:                  Apple_HFS HFS                     680.1 GB   disk2s1
   2:                 DOS_FAT_32 NTFS                    320.1 GB   disk2s2

   
zx:~ zx$ diskutil eject /dev/disk2
Disk /dev/disk2 ejected


zx:~ zx$ diskutil eject /dev/disk2
Unable to find disk for /dev/disk2


zx:~ zx$ diskutil mount disk2s1
Volume HFS on disk2s1 mounted


zx:~ zx$ diskutil mount /dev/disk2s2
Volume NTFS on /dev/disk2s2 mounted
~~~

