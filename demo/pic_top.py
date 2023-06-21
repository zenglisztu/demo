"""图片处理用"""
from PIL import ImageGrab
import os

"""显示图片用"""
import wx

"""程序被激活的入口以及监控调用下一步显示"""
from pynput.keyboard import Key, Controller, Listener


class Util:
    """图片处理类"""

    @staticmethod
    def get_pic():
        img = ImageGrab.grabclipboard()
        img.save('picture.png')

    @staticmethod
    def del_pic():
        os.remove('picture.png')  # 及时清理文件


class PicFrame(wx.Frame):
    """窗体类"""

    def __init__(self):
        """生成窗体"""
        # 参数设置
        self.shrink_rate = 1.08
        self.now_rate = 1
        self.shrink_quality = wx.IMAGE_QUALITY_NORMAL
        # 从剪切板生成图片
        Util.get_pic()
        # 读取本地图片为wxImage，之后转换生成bitmap对象
        self.img = wx.Image('picture.png', wx.BITMAP_TYPE_PNG)
        self.size = self.img.GetSize()
        # 清理图片
        Util.del_pic()
        # 初始化展示图片，None表示没有父节点，style通过参数调节没有边框
        # 框架的size通过图片的尺寸来自适应，位置用center函数取屏幕中央
        super().__init__(None, style=wx.SIMPLE_BORDER |
                                     wx.STAY_ON_TOP |
                                     wx.TRANSPARENT_WINDOW, size=self.size)
        self.Center(dir=wx.BOTH)
        # 创建一个Bitmap显示组件
        self.bitmap = wx.StaticBitmap(self, bitmap=wx.Bitmap(self.img))
        # 关联事件，移动窗口
        self.bitmap.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.bitmap.Bind(wx.EVT_MOTION, self.on_drag)
        self.bitmap.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.bitmap.Bind(wx.EVT_MOUSEWHEEL, self.on_scroll)

    def on_left_down(self, event):
        """左键按下"""
        """位置解析：
        默认左上角是（0,0）
        self.GetPosition() self代表的Client相对于Screen的位置
        event.GetPosition() event相对于Client的位置
        wx.GetMousePosition() 获取鼠标位置
        self.ClientToScreen()=前面的self+event位置
        以下这一句可以验证
        print(self.GetPosition()+event.GetPosition(),self.ClientToScreen(self.delta))
        """
        self.delta = event.GetPosition()

    def on_drag(self, event):
        """鼠标拖动"""
        # 如果不加LeftIsDown，就会导致递归移动，移动事件触发移动，鼠标放下也没用
        if event.Dragging() and event.LeftIsDown():
            mouse = wx.GetMousePosition()  # 用记录的delta抵消位置偏差
            self.Move((mouse.x - self.delta[0], mouse.y - self.delta[1]))

    def on_left_up(self, event):
        """左键放开"""
        if self.HasCapture():
            self.ReleaseMouse()

    def on_scroll(self, event):
        """
        滚轮控制缩放
        图像因为连续缩放会导致模糊，所以保留最初图像，每次从最初图像计算，保真
        """
        # 更新缩放倍数
        if event.GetWheelRotation() > 0:
            self.now_rate = self.now_rate * self.shrink_rate
        else:
            self.now_rate = self.now_rate / self.shrink_rate
        # 计算临时尺寸
        temp_size = (self.size[0] * self.now_rate, self.size[1] * self.now_rate)
        # 更改窗口大小
        self.SetSize(temp_size)
        # 更改图片大小
        temp_img = self.img.Scale(*temp_size, self.shrink_quality)
        self.bitmap.SetBitmap(wx.Bitmap(temp_img))


class ScrShotShow:
    """主类"""

    def __init__(self):
        """主函数"""
        # 激活截图，使用无敌简洁的写法，完美！！！
        controller = Controller()
        with controller.pressed(Key.cmd):
            with controller.pressed(Key.shift):
                controller.press('s')
                controller.release('s')
        # 监控enter键，检查到就激活图片处理
        # 设定join类监听，阻塞程序，如果出现enter，就将监听线程停掉继续后面的操作
        with Listener(
                on_press=self.on_press, on_release=None
        ) as self.listener:
            self.listener.join()
        # 激活图片显示
        app = wx.App()  # 创建app
        PicFrame().Show()  # 生成我的窗体类
        app.MainLoop()  # 循环

    def on_press(self, key):
        """按键按下响应"""
        # 停掉监听线程，进行后面的操作，也可以通过 return False实现
        self.listener.stop()
        # return False


if __name__ == '__main__':
    ScrShotShow()