import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QFileDialog

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(600,200)
        self.btn = QPushButton('选择文件',self)
        self.edit = QLineEdit()
        layout = QHBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.edit)
        self.setLayout(layout)

        self.btn.clicked.connect(self.select_file)

    def select_file(self):
        file ,type = QFileDialog.getOpenFileName(self,"选择文件", r'./', "All Files (*);;Text Files (*.*)")
        self.edit.setText(file)
        print(file,"\n", type)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()