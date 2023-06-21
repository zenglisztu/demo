import sys
import json
from time import sleep

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from PyQt5.Qt import QThread
import requests


class LoginThread(QThread):
    start_login_signal = pyqtSignal(str)

    def __init__(self, signal):
        super().__init__()
        self.signal_status = signal

    def login_requests(self,user_password_json):
        user_password_data = json.loads(user_password_json)
        user_name = user_password_data.get('user_name')
        password = user_password_data.get('password')
        #对云函数发起get请求
        res = requests.get('https://service-reompve0-1318330569.gz.apigw.tencentcs.com/release/qt_login', json={'user_name':user_name, 'password':password})
        #将云函数返回的内容解析后打印在pad上
        res_value = res.json()
        print(res_value)

        self.signal_status.emit(json.dumps(res_value))

    def run(self):

        while True:

            print("正在运行登录子线程........")
            sleep(10)


class MyWindow(QWidget):
    login_status_signal = pyqtSignal(str)

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
        self.login = self.ui.pushButton
        self.forget = self.ui.pushButton_2
        self.pad = self.ui.textBrowser
        #设置提示信息
        self.user_name.setPlaceholderText("请输入用户名")
        self.password.setPlaceholderText("请输入密码")
        #设置密码显示格式
        self.password.setEchoMode(QLineEdit.Password)
        #绑定登录按钮
        self.login.clicked.connect(self.push_login)
        #创建登录进程
        self.login_status_signal.connect(self.print_status)
        self.login_thread = LoginThread(self.login_status_signal)
        self.login_thread.start_login_signal.connect(self.login_thread.login_requests)
        self.login_thread.start()


    def push_login(self):
        #获取用户输入的用户名和密码
        user = self.user_name.text()
        password = self.password.text()
        self.login_thread.start_login_signal.emit(json.dumps({'user_name':user, 'password':password}))
    def print_status(self, status):
        json_data = json.loads(status)
        self.pad.setText(json_data.get('errmsg'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.ui.show()
    app.exec()