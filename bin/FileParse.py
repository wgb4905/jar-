#####################################################################################################
##    解析文件名    文件格式：  工程名.操作List
#####################################################################################################
import os
def parse(filePath: str,fileName:str):
    
    #定义变量
    program_name = '' #工程名
    operation='' #操作
    jars=[] #jar包名
    file_content={} #返回结果

    tempName=str(fileName)
    file_name=tempName.split('.')#分隔文件名

    #获取操作类型、工程名
    program_name=file_name[0]
    if file_name[1].startswith('add'):
        operation='新增'
    elif file_name[1].startswith('delete'):
        operation='删除'
    else:
        operation='其他'

    #读取文件内容
    file=open(os.path.join(filePath,fileName))
    for line in file.readlines():
        jar=line[4:]
        jars.append(jar)

    file_content['program_name']=program_name
    file_content['operation']=operation
    file_content['jars']=jars

    return file_content
        



