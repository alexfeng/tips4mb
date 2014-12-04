# -*- coding: utf-8 -*-
# ! /usr/bin/
import os.path
import sys

path=os.getcwd()

githubStringPostion = path.find("github/");

pathLocal = path[githubStringPostion + 1 + 6 :]
# print pathLocal

projectName = pathLocal[:pathLocal.find("/")]
projectName = "https://github.com/urmyfaith" + projectName + "/tree/master"
# print projectName

pathOnGithubPart1 = pathLocal[pathLocal.find("/") + 1:]
# print pathOnGithubPart1



linkString = ""
tableContentString = ""

files = os.listdir('.')
for file in files:

	if file.startswith('.') or file.endswith('.swp') or not cmp("prepare4md.py",file):
		print "--> "+ file + " is ignored."
		continue

	linkName = '[' + file +']'

	pathList =[];
	pathList.append(projectName)
	pathList.append(pathOnGithubPart1)
	pathList.append(file)
	linkAddress = '('+'/'.join(pathList) + ')'

 	linkString  = linkName + linkAddress

	oneRowString = '''
''' + '|' + linkString + '| description |'

	tableContentString = tableContentString + oneRowString

tableStringHead ='''| 文件名 |  描述 |
| ------------- | ------------ |'''


tableString =  tableStringHead + tableContentString
print tableString


file2write = "/Users/zx/documents/github/prepare4md.md"
f =open(file2write,'w')
f.write(tableString)
f.close

os.system('open ' + file2write)



