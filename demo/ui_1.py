import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__init__ui()

    def __init__ui(self):
        #设置窗体标题
        self.setWindowTitle('python')
        #设置窗体大小
        self.resize(600, 480)

        #创建垂直布局器
        layout = QVBoxLayout()
        btn1 = QPushButton("按钮1")
        btn2 = QPushButton("按钮2")
        btn3 = QPushButton("按钮3")
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        #添加弹簧
        layout.addStretch()
        layout.addWidget(btn3)
        layout.addStretch()
        #设置布局器
        self.setLayout(layout)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Mywindow()
    window.show()

    app.exec()



'''
    #创建应用
    app = QApplication(sys.argv)
    #创建窗口
    window = QWidget()
    #设置窗口标题
    window.setWindowTitle('python')
    #创建文本框
    edit = QLineEdit(window)
    #创建按钮
    but = QPushButton("打开", window)
    #创建标签
    label = QLabel("文件", window)

    #将窗体显示在中央
    center_point = QDesktopWidget().availableGeometry().center()
    xp, yp, width, height = window.frameGeometry().getRect()
    window.move(int(center_point.x()-width/2), int(center_point.y()-height/2))

    #设置图标
    window.setWindowIcon(QIcon('sztu.ico'))
    #设置窗体大小
    window.resize(600, 480)
    #设置控件显示位置和大小
    but.setGeometry(60, 60, 30, 30)
    edit.setGeometry(100, 100, 100, 50)
'''