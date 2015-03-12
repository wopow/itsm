#-*-coding:utf-8-*-
import os
import os.path
import re

def getdir(rootdir):
#    rootdir = "/home/wopow/python/itsm/xls"                                   # 指明被遍历的文件夹
    dirtree=[]
    print rootdir
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

        for dirname in  dirnames:                       #输出文件夹信息
            if len(dirname) == 6:
                dirmatch=re.match('\d{6}',dirname)
                if dirmatch != None:
                    print dirname
                    dirtree.append(dirname)
        for filename in filenames:                        #输出文件信息
            print "parent is: " + parent
            print "filename is: " + filename
            print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
    return dirtree

if __name__ == "__main__":
   print getdir('/home/wopow/python/itsm/xls')


