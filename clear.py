#-*-coding:utf-8-*-
import os
def screecls(rootdir):
    os.system('clear')
    for year in rootdir:
        print "                           %s"  %year
    content = raw_input("请选择需要处理的月份：")
    print content
