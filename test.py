
from bin import FileParse
filePath=r'D:\python测试\组包\addlist'
fileName=r'igtb-auto-its.addAndModList'

file_dict=FileParse.parse(filePath,fileName)
# print(file_dict)

from bin import XlsxModify

constant=['交易银行平台（二期）项目(细化-009)-iGTB Net[第6期]','P2004','2020/9/9']

xlslObject = XlsxModify.xlsxModel()

xlslObject.open('_IGTB交易银行JAR包配置文档-P2004(功能测试版).xlsx')

xlslObject.delete()

xlslObject.add(file_dict,constant)

xlslObject.close()



