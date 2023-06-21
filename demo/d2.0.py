from pathlib import Path
import xlwings as xw
import os
path = Path(__file__).parent

filename = input('请输入文件名：')

app = xw.App()

app.visible = False

wb_or = app.books.open(f'{path}/机械31班花名册（学号排序）.xlsx')

org_names = set(wb_or.sheets[0].range('b3:b72').value)

wb_ta = app.books.open(f'{path}/{filename}.xlsx')

tar_names = wb_ta.sheets[0].range('d2:d77').value

tar_names = set([name for name in tar_names if name])

df_names = org_names - tar_names

for n in df_names:
    print(n)

wb_ta.close()
wb_or.close()
app.quit()

os.system('pause')