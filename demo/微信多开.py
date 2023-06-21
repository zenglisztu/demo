import os

try :
    
    n = int(input('请输入需要打开微信的数量：'))

    times = ' && start 1\软件\WeChat\WeChat.exe' * n

    os.system(f'd:{times}')
    
except Exception as err:
    
    print(err)
    
    print('发生错误，可能是输入有误！')
    
    os.system('pause')


        
#chcp 65001
#d:
#start 1\软件\WeChat\WeChat.exe
