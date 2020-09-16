
from bin import FileParse
from bin import XlsxModify
import configparser
import datetime
import os
import shutil

date=datetime.datetime.now().strftime('%Y%m%d')

path=os.getcwd()
file_path=os.path.join(path,'addlist')
goal_path=os.path.join(path,r'已生成',date)

if not os.path.exists(file_path):
    print('addlist 文件夹不存在')
if not os.path.exists('IGTB交易银行JAR包配置文档.xlsx'):
    print('IGTB交易银行JAR包配置文档.xlsx 文件夹不存在')


#读取文件名、批次、任务
cf = configparser.ConfigParser(allow_no_value=True)
# cf.read(r"D:\python测试\组包\config.ini",encoding='utf-8')
cf.read(r"D:\Users\Desktop\版本\交易银行版本\config.txt",encoding='utf-8')

taskInfo=cf.get("任务", "需求简述")
mission=cf.options("批次")[0].upper()
split=cf.options("批次标识")[0]
constant=[taskInfo,mission,date]

#拷贝文件
shutil.copytree(file_path,os.path.join(goal_path,'addlist'))
xlsx_name='IGTB交易银行JAR包配置文档-'+mission+'(功能测试版).xlsx'#创建临时文件
shutil.copy('IGTB交易银行JAR包配置文档.xlsx',xlsx_name)

#操作xlsx
xlslObject = XlsxModify.xlsxModel()
xlslObject.open(os.path.join(path,xlsx_name))
xlslObject.delete()

# 循环添加jar包
for file in os.listdir(file_path):
    file_dict=FileParse.parse(file_path,file) #解析文件
    xlslObject.add(file_dict,constant)
    os.remove(os.path.join(file_path,file)) #添加完jar包后，移除文件夹内的文件，测试时注释该行

#将相同jar包的操作类型改为：升级替换
xlslObject.merge(split)
print('合并：将相同jar包的操作类型改为：升级替换！')

result=xlslObject.close()

print('jar包配置文档生成')
shutil.move(result,goal_path)


print('完成： 文件位于文件夹',goal_path)









