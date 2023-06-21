import sys
import json
from time import sleep
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from PyQt5.Qt import QThread
import requests


class MyThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(10):
            print(f'正在登录.....{i}')
            sleep(1)
        print("登录成功！")


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.load_ui()
    def load_ui(self):
        #加载ui
        self.ui = uic.loadUi(r'C:\Users\曾立\Desktop\demo\login.ui')
        #设置ui图标
        self.ui.setWindowIcon(QIcon(r'C:\Users\曾立\Desktop\demo\img.png'))
        #获取ui控件
        self.user_name = self.ui.lineEdit
        self.password = self.ui.lineEdit_2
        self.longin = self.ui.pushButton
        self.forget = self.ui.pushButton_2
        self.pad = self.ui.textBrowser
        #设置提示信息
        self.user_name.setPlaceholderText("请输入用户名")
        self.password.setPlaceholderText("请输入密码")

        #设置密码显示格式
        self.password.setEchoMode(QLineEdit.Password)

        #绑定登录按钮
        self.longin.clicked.connect(self.push_login)
        #print(self.ui.__dict__)

    def push_login(self):
        #获取用户输入的用户名和密码
        user = self.user_name.text()
        password = self.password.text()
        #对云函数发起get请求
        res = requests.get('https://service-reompve0-1318330569.gz.apigw.tencentcs.com/release/qt_login', json={'user_name':user, 'password':password})
        #将云函数返回的内容解析后打印在pad上
        res_value = json.loads(res.content.decode('utf-8'))
        self.pad.setText(res_value['errmsg'])
        print(res_value['errmsg'])
        print(res.content.decode('utf-8'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()
    window.ui.show()
    app.exec()