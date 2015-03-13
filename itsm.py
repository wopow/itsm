#coding=utf8
import xlrd
import sys
import os
import dirname
#解决编码问题
reload(sys)
sys.setdefaultencoding( "utf-8" )
#建立空字典
txtkey={  }
#print输出改为蓝色
def inblue( s ):
    return"%s[1;36;2m%s%s[0m"%(chr(27), s, chr(27))

rootdir=os.listdir(sys.argv[1])
filename=dirname.getdir(rootdir)




xlsfile=[]
for i in filename:
    j=i[i.rfind('.'):]
    if j == '.xls':
         xlsfile.append(i)
sum=0
for x in xlsfile:
	#读取命令行中的路径，并打开文件
	data=xlrd.open_workbook(sys.argv[1]+ "/" + x)
	#选择工作簿
	table=data.sheets()[0]
	#选择数据列
	txt=table.col_values(2)

	#遍历数据，并加入字典，统计key出现的次数
	for i in txt:
	    if txtkey.has_key(i):
		txtkey[i]=txtkey.get(i)+1
	    else:
		txtkey.setdefault(i,1)
#打开日志文件，并写入
file=open('itsm.log',"w")
for j in txtkey:
    sum=txtkey[j]+sum
    print u"<%s>服务请求建单数为：%s" %(inblue(j),inblue(txtkey[j]))
    itsm=u"<%s>服务请求建单数为：%s\r\n" %(j,txtkey[j])
    file.write(itsm)
file.write("共合计："+str(sum)+"笔")
file.close()
