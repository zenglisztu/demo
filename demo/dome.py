import pandas as pd
import os
from pathlib import Path
import xlwings as xw


path = Path(__file__).parent
try :
    
    file = input('请输入文件名：')
    org = pd.read_excel(f'{path}//机械31班花名册（学号排序）.xlsx',header=1)
    sample = pd.read_excel(f'{path}//{file}.xlsx')

    mask = org['姓名'].isin(sample['姓名'])
    nmask = []
    for x in mask :
        nmask.append(not x)

    result = org[nmask][['姓名','宿舍号','床位']]

    result.to_excel(f'{path}//result.xlsx')
    print('未提交：')
    for i in result['姓名'] :
        print(i)
        
    app = xw.App()
    wb = app.books.open(f'{path}//result.xlsx')
    os.system('pause')
    
except Exception as err :
    print('未知错误，文件名错误或数据为空！')
    
    if 'wb' in dir():
        wb.close()
        
    os.system('pause')
    
