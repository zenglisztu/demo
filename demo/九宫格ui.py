import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        #设置窗体名称
        self.setWindowTitle('计算器')
        #设置窗体大小
        self.resize(300, 240)

        #创建总布局器
        g_layout = QVBoxLayout()
        #创建输入框
        edit = QLineEdit()
        edit.setPlaceholderText('请输入')

        #数据
        data = {
            0:['C', '<-', '%', '/'],
            1:['7', '8', '9', 'X'],
            2:['4', '5', '6', '-'],
            3:['1', '2', '3', '+'],
            4:['e', '0', '.', '=']
        }

        #创建网格布局器
        grid_layout = QGridLayout()
        #将数据写入网格布局器
        for row, data_values in data.items():
            for col, value in enumerate(data_values):
                btn = QPushButton(value)
                grid_layout.addWidget(btn,row,col)

        #将文本框和网格布局器放入总布局器
        g_layout.addWidget(edit)
        g_layout.addLayout(grid_layout)

        self.setLayout(g_layout)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    app.exec()