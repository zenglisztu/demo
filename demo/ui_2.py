import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__init__ui()

    def __init__ui(self):
        # 设置窗体名称
        self.setWindowTitle('个人信息')
        # 设置窗体大小
        self.resize(600, 480)
        # 设置窗体图标
        self.setWindowIcon(QIcon(r'./sztu.ico'))

        # 创建布局器
        g_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        # 创建容器1
        box_1 = QGroupBox("学位")
        # 创建按钮
        btn1 = QRadioButton('学士')
        btn2 = QRadioButton('硕士')
        btn3 = QRadioButton('博士')
        # 将按钮添加到布局器—v
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        # 将布局器-v添加到容器
        box_1.setLayout(v_layout)

        # 创建容器2
        box_2 = QGroupBox('学校')
        # 创建按钮
        btn4 = QRadioButton('深圳技术大学')
        btn5 = QRadioButton('深圳大学')
        # 将按钮放入布局器-h
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        # 将布局器-h放入容器2

        box_2.setLayout(h_layout)
        # 将所有容器放入总布局器
        g_layout.addWidget(box_1)
        g_layout.addWidget(box_2)
        self.setLayout(g_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    app.exec()
