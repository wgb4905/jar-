
import openpyxl

wb=openpyxl.load_workbook('IGTB交易银行JAR包配置文档.xlsx')
ws=wb['JAR包变更历史记录']

cells= ws['A']
# print(cells)
for cell in cells:
    print (cell.value)