import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        #设置窗体大小
        #self.resize(220 ,100)
        self.setFixedSize(220, 100)#禁止改变窗体大小
        #设置窗体名称
        self.setWindowTitle('QQ')
        #设置窗体图标
        self.setWindowIcon(QIcon(r'C:\Users\曾立\Desktop\demo\img.png'))

        #创建总布局器
        g_layout = QVBoxLayout()

        #创建表单布局器
        form_layout = QFormLayout()
        #创建账号输入框
        edit_1 = QLineEdit()
        edit_1.setPlaceholderText("请输入账号")
        form_layout.addRow('账号', edit_1)
        #创建密码输入框
        edit_2 = QLineEdit()
        edit_2.setPlaceholderText("请输入密码")
        form_layout.addRow('密码', edit_2)

        #创建登录按钮
        btn = QPushButton('登录')
        #设置按钮大小
        btn.setFixedSize(60, 30)
        #将表单和按钮放入总布局器
        g_layout.addLayout(form_layout)
        #指定对齐方式
        g_layout.addWidget(btn, alignment=Qt.AlignCenter)

        #设置窗体布局器
        self.setLayout(g_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    app.exec()