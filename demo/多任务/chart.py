import sys
import socket
from PyQt5 import uic
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget


class MyThread(QThread):
    def __init__(self):
        super().__init__()


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.load_ui()

    def load_ui(self):
        #加载ui
        self.ui = uic.loadUi(r'./chart.ui')

        #获取ui控件
        self.btn_push = self.ui.push
        self.ip = self.ui.ip
        self.port = self.ui.port
        self.edit = self.ui.edit
        self.info = self.ui.info
        self.ok = self.ui.ok
        print(self.ui.__dict__)



def send_msg(udp_socket):
    """获取键盘数据，并将其发送给对方"""
    # 1. 从键盘输入数据
    msg = input("\n请输入要发送的数据:")
    # 2. 输入对方的ip地址
    dest_ip = input("\n请输入对方的ip地址:")
    # 3. 输入对方的port
    dest_port = int(input("\n请输入对方的port:"))
    # 4. 发送数据
    udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据并显示"""
    # 1. 接收数据
    recv_msg = udp_socket.recvfrom(1024)
    # 2. 解码
    recv_ip = recv_msg[1]
    recv_msg = recv_msg[0].decode("utf-8")
    # 3. 显示接收到的数据
    print(">>>%s:%s" % (str(recv_ip), recv_msg))


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定本地信息
    udp_socket.bind(("", 7890))
    while True:
        # 3. 选择功能
        print("="*30)
        print("1:发送消息")
        print("2:接收消息")
        print("="*30)
        op_num = input("请输入要操作的功能序号:")

        # 4. 根据选择调用相应的函数
        if op_num == "1":
            send_msg(udp_socket)
        elif op_num == "2":
            recv_msg(udp_socket)
        else:
            print("输入有误，请重新输入...")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MyWindow()

    window.ui.show()

    app.exec()


