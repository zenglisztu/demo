import re
from os import system
from time import sleep
import PySimpleGUI as sg
from PyQt5.QtCore import QThread
from pdf2docx import Converter


class SThread(QThread):
    def __init__(self):
        super().__init__()
    
    def run():
        while True:
            print("等待转换......")
            sleep(1)

# 主题设置
sg.theme('DarkTeal7')
 
# 布局设置
layout = [
          [sg.Text('待转化的文件是：',font=("微软雅黑", 12)),sg.Text('',key='filename',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
          [sg.Text('程序操作记录',justification='center')],
          [sg.Output(size=(80, 20),font=("微软雅黑", 10))],                
          [sg.FileBrowse('选择文件',key='file',target='filename'),sg.Button('开始转化'),sg.Button('关闭程序')]
         ]      
 
# 创建窗口
window = sg.Window('pdf转word工具', layout,font=("微软雅黑", 15),default_element_size=(50,1))    
 
# 事件循环
while True:
    event, values = window.read()
    if event in (None, '关闭程序'):
        break
    if event == '开始转化':
        if values['file'] and re.findall(r'\.(\S+)',values['file'])[0]=='pdf':
            fileName = values['file']
            #pdf_to_word(fileName)
            cv = Converter(fileName)
            docx_file = fileName.replace('.pdf','.docx')
            print('\n----------开始转化----------\n')
            cv.convert(docx_file, start=0, end=None)
            cv.close()
            
            print('\n----------转化完毕----------\n')
            
            system(f'start {docx_file}')
        else:
            print('文件未选取或文件非pdf文件\n请先选择文件')
 
window.close()
