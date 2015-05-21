# -*- coding: utf-8 -*-


import os
import sys
import time

dirNames=os.listdir(os.getcwd())

for dir in dirNames:
    if  dir.endswith('.md') :
        cmd="'sed -i '' -e '1i \
            new line.' "+ dir.replace('.md','')
#       os.system(cmd)
        print cmd