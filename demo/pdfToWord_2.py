import sys
from os import system
from time import sleep
from pathlib import Path
from pdf2docx import Converter
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import bk


class SThread(QThread):
    progress_signal = pyqtSignal(int)
    output_pad_signal = pyqtSignal(str)

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def run(self):
        try:
            cv = Converter(self.file_name)
            docx_file = self.file_name.replace('.pdf', '.docx')
            self.progress_signal.emit(12)
            sleep(0.5)
            self.output_pad_signal.emit(f"\n- - - - - - - - - -开始转换- - - - - - - - - -\n")
            self.output_pad_signal.emit(f"\n{self.file_name}\n")
            self.progress_signal.emit(90)
            cv.convert(docx_file, start=0, end=None)
            cv.close()
            self.progress_signal.emit(100)
            self.output_pad_signal.emit("\n- - - - - - - - - -转换成功- - - - - - - - - -\n")
            self.output_pad_signal.emit(f"\n{docx_file}\n")
            system(docx_file)
        except Exception as e:
            print(e)
            self.progress_signal.emit(-1)
            self.output_pad_signal.emit('')

class DThread(QThread):
    progress_signal_d = pyqtSignal(int)
    output_pad_signal_d = pyqtSignal(str)

    def __init__(self, dir):
        super().__init__()
        self.dir = dir
        self.path_dir = Path(self.dir)
        self.i = 1
        self.j = 0
        self.files_count = len(list(self.path_dir.glob("*.pdf")))
        self.new_path = self.path_dir / '__rest__'
        if not self.new_path.exists():
            self.new_path.mkdir()

    def run(self):

        for pdf in self.path_dir.glob("*.pdf"):
            docx_file = str(self.new_path) + '\\' + str(pdf.stem) + '.docx'
            print(docx_file)
            pdf = str(pdf)

            try:
                cv = Converter(pdf)
                self.output_pad_signal_d.emit(f"\n- - - - - - - - - -开始转换- - - - - - - - - -\n")
                self.output_pad_signal_d.emit(f"\n{self.i}: {pdf}\n")
                cv.convert(docx_file, start=0, end=None)
                cv.close()
                self.progress_signal_d.emit(int((self.i*100)//self.files_count))
                self.output_pad_signal_d.emit("\n- - - - - - - - - -转换成功- - - - - - - - - -\n")
                self.output_pad_signal_d.emit(f"\n{self.i}: {docx_file}\n")
            except Exception as e:
                print(e)
                self.output_pad_signal_d.emit(f"\n{self.i}: {pdf}\n转换失败！")
                self.j += 1
            self.i += 1

        self.output_pad_signal_d.emit(f'\n转换完成！总计{self.i-1} 成功{self.i -1 -self.j} 失败{self.j}\n')
        self.progress_signal_d.emit(100)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(r'./pdf_to_world.ui')
        self.ui.setWindowIcon(QIcon(r'./matplotlib.png'))
        self.get_widget()
        # 设置禁止改变窗体大小模式
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        # 定义控件
        self.msgbox = QMessageBox(QMessageBox.Information, 'Information','请选择路径!')
        self.msgbox_dir = QMessageBox(QMessageBox.Information, 'Information', '请选择正确的文件夹路径!')
        self.msgbox_file = QMessageBox(QMessageBox.Information, 'Information', '请选择正确的文件路径!')
        # self.msgbox_finished = QMessageBox(QMessageBox.Information, 'Information', '转换完成!')
        #self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    def get_widget(self):
        # 获取控件
        self.file_edit = self.ui.file_show
        self.output_pad = self.ui.output_pad
        self.progress_bar = self.ui.progressBar
        self.progress_bar.setVisible(False)
        self.select_btn = self.ui.select_btn
        self.start_btn = self.ui.start
        self.quit_btn = self.ui.quit_btn
        self.single_file = self.ui.single_file
        self.all_file = self.ui.all_file
        self.cleae_pad = self.ui.clear
        self.save_pad = self.ui.save_data
        self.save_pad.setVisible(False)
        print(self.ui.__dict__)
        #绑定槽函数
        self.select_btn.clicked.connect(self.select_file)
        self.start_btn.clicked.connect(self.start_change)
        self.cleae_pad.clicked.connect(self.pad_clear)
        self.save_pad.clicked.connect(self.push_save)
    def select_file(self):
        self.progress_bar.setVisible(False)
        # 选择单个文件转换
        if self.single_file.isChecked():
            self.file_name, file_type = QFileDialog.getOpenFileName(self, "选择PDF文件", './', "PDF Files (*.pdf)")
            self.file_edit.setText(self.file_name)
        # 选择文件夹
        else:
            self.dir = QFileDialog.getExistingDirectory(self, '选择文件夹', './')
            self.file_edit.setText(self.dir)

    def quit_app(self):
        pass

    def start_change(self):
        # 选择单个文件时
        if self.single_file.isChecked():
            if self.file_edit.text():
                if '.pdf' in self.file_edit.text() and Path(self.file_edit.text()).exists():
                    self.progress_bar.setVisible(True)
                    # 创建子进程
                    self.thread_change = SThread(self.file_name)
                    #连接信号槽
                    self.thread_change.progress_signal.connect(self.thread_finished)
                    self.thread_change.output_pad_signal.connect(self.pad_out)
                    #运行子线程
                    self.thread_change.start()
                else:
                    self.msgbox_file.exec()
            else:
                self.msgbox.exec_()
        # 选择文件夹时
        else:
            if self.file_edit.text():
                if '.pdf' not in self.file_edit.text() and Path(self.file_edit.text()).exists():
                    self.progress_bar.setVisible(True)
                    # 创建子进程
                    self.thread_change_dir = DThread(self.dir)
                    #连接信号槽
                    self.thread_change_dir.progress_signal_d.connect(self.thread_finished)
                    self.thread_change_dir.output_pad_signal_d.connect(self.pad_out)
                    #运行子线程
                    self.thread_change_dir.start()
                else:
                    self.msgbox_dir.exec_()
            else:
                self.msgbox.exec_()
    def thread_finished(self,value):
        if value == -1:
            self.progress_bar.setVisible(False)
        else:
            self.progress_bar.setValue(value)

        # if value == 100:
        #     self.msgbox_finished.exec()
    def pad_out(self,string):
        self.output_pad.append(string)

    def pad_clear(self):
        self.output_pad.setText('')

    def push_save(self):

        with open(r'./转换记录.txt', 'w', encoding='utf-8') as f:
            print(self.output_pad.toPlainText())
            f.write(self.output_pad.toPlainText())
        system(r'转换记录.txt')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.ui.show()
    sys.exit(app.exec())