##############################################################################
# 操作xlsx表格：
# 1.删除以前数据
# 2.循环添加数据
# 3.合并
###############################################################################

import openpyxl
import datetime
import os

class xlsxModel:
    # def __init__(self):
    #         self._name = null
    #         self._age = null

    def open(self,xlsxFile:str):
        #打开xlsx
        self._wb = openpyxl.load_workbook(xlsxFile)
        file=xlsxFile.split('.')
        self._fileName=file[0]
        self._ws = self._wb['JAR包变更历史记录']
        self._cnt =3 #行计数器,忽略前2行

    def close(self):
        #保存文件：文件名-mmdd
        fileName=self._fileName+datetime.datetime.now().strftime('%m%d')+'.xlsx'
        self._wb.save(fileName)
        self._wb.close()
        os.remove(self._fileName+'.xlsx')
        return fileName


    def add(self,file_content: dict,constant:list):

        #解析文件
        program_name=file_content['program_name']
        operation=file_content['operation']
        jars=file_content['jars']

        #添加行
        for jar in jars:
            data=[jar,'王国斌',program_name,operation,'']
            data.extend(constant)
            print('插入第{0}行数据：'.format(self._cnt-2))
            print(data)
            self._ws.append(data)
            self._cnt=self._cnt+1
    
    def delete(self):

        #删除以前数据:删除从第三行开始所有行
        self._ws.delete_rows(3,self._ws.max_row-2)

    def merge(self,split: str):

        #汇总
        jars_dict={} #jar包：所在行
        cells= self._ws['A']
        for cell in cells:
            row=str(cell.row)
            value=cell.value

            #判断是否是igtb的jar包，只操作igtb的jar包
            if value.startswith('igtb-'):
                jar=value.split(split)[0]#取jar包名
            else:
                continue

            #合并操作
            if not jar in jars_dict:
                jars_dict[jar]=row #jar包不在集合内，则将单元格行数添加至集合
            else:
                #先判断工程名，如果工程名不同，说明jar包不在同一个工程，将字典里的jar包替换；如果jar包在同一工程内，再判断操作类型
                if self._ws['C'+row].value != self._ws['C'+jars_dict[jar]].value:
                    jars_dict[jar]=row #更新row
                #判断操作类型，将操作改为：升级替换
                else:
                    #当前行操作类型为删除时：
                    if self._ws['C'+row].value == '删除':
                        self._ws['D'+jars_dict[jar]].value='升级替换'
                        self._ws['E'+jars_dict[jar]].value=value
                        self._ws.delete_rows(int(row)) #删除后面的行
                    #当前行操作类型为新增时：
                    else:
                         self._ws['E'+jars_dict[jar]].value=self._ws['A'+jars_dict[jar]].value
                         self._ws['A'+jars_dict[jar]].value=value

                    self._ws['D'+jars_dict[jar]].value='升级替换'
                    self._ws.delete_rows(int(row)) #删除后面的行




                

            



        
