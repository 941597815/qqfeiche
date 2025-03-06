import win32gui
import win32ui
import win32con
import win32api
import numpy as np
import cv2
import time


class Bkgnd:
    def __init__(self, class_name, title_pattern):
        self.class_name = class_name
        self.title_pattern = title_pattern
        self.hwnd = self.find_window()

    def find_window(self):
      hwnd = win32gui.FindWindow(self.class_name, None)
      while hwnd:
          title = win32gui.GetWindowText(hwnd)
          if title and self.class_name in win32gui.GetClassName(hwnd) and self.title_pattern in title:
              return hwnd
      raise Exception("Window not found")
    def get_window_title(self):
        return win32gui.GetWindowText(self.hwnd)
    def screenshot(self):
            left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
            width = right - left
            height = bottom - top

            hwndDC = win32gui.GetWindowDC(self.hwnd)
            mfcDC = win32ui.CreateDCFromHandle(hwndDC)
            saveDC = mfcDC.CreateCompatibleDC()

            saveBitMap = win32ui.CreateBitmap()
            saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
            saveDC.SelectObject(saveBitMap)
            saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

            bmpinfo = saveBitMap.GetInfo()
            bmpstr = saveBitMap.GetBitmapBits(True)

            img = np.frombuffer(bmpstr, dtype=np.uint8)
            img = img.reshape((height, width, 4))
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

            win32gui.DeleteObject(saveBitMap.GetHandle())
            saveDC.DeleteDC()
            mfcDC.DeleteDC()
            win32gui.ReleaseDC(self.hwnd, hwndDC)

            return img

    def find_image(self, template_path):
        template = cv2.imread(template_path)
        h, w = template.shape[:2]
        res = cv2.matchTemplate(self.screenshot(), template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            center_x = pt[0] + w // 2
            center_y = pt[1] + h // 2
            return center_x-8, center_y-31#减去窗口边框8，31
        # print(f'未找到图片:{template_path.split("/")[-1]}')
        return None

    def click(self, xy):
        if not xy:return False
        x = int(xy[0])
        y = int(xy[1])
        # print(x,y)
        # 发送鼠标移动消息
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, 0, (x ) | ((y) << 16))
        time.sleep(0.1)
        # 发送鼠标左键按下消息
        win32api.PostMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, (x) | ((y) << 16))
        time.sleep(0.05)
        # 发送鼠标左键松开消息
        win32api.PostMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, (x) | ((y) << 16))
        time.sleep(0.1)
        return True
    
    def click_for_img(self, img, x=0, y=0):#x,y偏移量
        xy=self.find_image(img)
        if(xy):
            self.click((xy[0]+x,xy[1]+y))

    def send_key(self, key):
        # 发送按键消息
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, key, 0)
        time.sleep(0.05)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, key, 0)
        time.sleep(0.1)

if __name__ == "__main__":
    app = Bkgnd("GAMEAPP", "QQ飞车2.0")
    # print(app.find_image("./imgs/cd.bmp"))
    app.click_for_img("./imgs/cd.bmp")
    