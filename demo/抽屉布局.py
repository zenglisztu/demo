import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QStackedLayout

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('深圳技术大学', self)


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('本科', self)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.craet_slayout()
        self.init_ui()

    def craet_slayout(self):
        #创建堆叠布局器
        self.stack_layout = QStackedLayout()
        #在堆叠布局器中添加显示内容
        self.stack_layout.addWidget(Window1())
        self.stack_layout.addWidget(Window2())

    def init_ui(self):
        #设置窗体名称
        self.setWindowTitle('抽屉')
        #设置窗体大小
        self.resize(300, 300)

        #创建总布局器
        g_layout = QVBoxLayout()
        #创建按钮1， 按钮2
        btn1 = QPushButton('学历')
        btn2 = QPushButton('学校')
        #给按钮添加事件响应
        btn1.clicked.connect(self.push_btn1)
        btn2.clicked.connect(self.push_btn2)
        #在总布局器中添加内容
        g_layout.addLayout(self.stack_layout)
        g_layout.addWidget(btn1)
        g_layout.addWidget(btn2)

        #设置总布局器
        self.setLayout(g_layout)

     #按钮1响应
    def push_btn1(self):
            self.stack_layout.setCurrentIndex(1)
    #按钮2响应
    def push_btn2(self):
            self.stack_layout.setCurrentIndex(0)
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    app.exec()
