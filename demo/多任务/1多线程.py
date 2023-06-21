import threading
from time import sleep
from ctypes import *

main_ = cdll.LoadLibrary(r'./libf.so')


class MyTask(threading.Thread):
    def __init__(self,time):
        super().__init__()
        self.time = time

    def run(self):
        for i in range(self.time):
            print(i,'4')
            sleep(0.5)


def sing():
    for i in range(3):
        print(f"singing...  {i}")
        sleep(1)


def dance():
    for i in range(3):
        print(f'dancing...  {i}')
        sleep(1)


if __name__ == '__main__':

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t3 = threading.Thread(target=main_.main)
    t4 = MyTask(10)
    t4.start()
    t1.start()
    t2.start()
    t3.start()