import time
import subprocess
import win32con
import win32api
import win32gui
import pyautogui
import cv2
import numpy as np


def find_image(template_path, threshold=0.8):
    # 捕获全屏截图
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # 加载目标图像
    template = cv2.imread(template_path)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 转换截图为灰度图像
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # 进行模板匹配
    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        # 计算点击位置
        template_height, template_width = template.shape
        click_x = max_loc[0] + template_width // 2
        click_y = max_loc[1] + template_height // 2
        return (click_x, click_y)

    else:
        print("未找到图像")


def click(len):
    click_x = int(len[0])
    click_y = int(len[1])
    # 移动鼠标并点击
    win32api.SetCursorPos(len)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, click_x, click_y, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, click_x, click_y, 0, 0)


def click_for_img(img, x=0, y=0):
    """x,y偏移量"""
    xy = find_image(img)
    # print(xy)
    if not xy:
        return
    click((xy[0] + x, xy[1] + y))


def click_for_img_wait(img, x=0, y=0):
    """x,y偏移量"""
    xy = find_image(img)
    # print(xy)
    while not xy:
        xy = find_image(img)
        time.sleep(1)
    click((xy[0] + x, xy[1] + y))


# 特殊符号的键值映射
special_keys = {
    ".": 190,  # 小数点
    "!": 49,  # 按下 1 键然后松开
    "@": 50,  # 按下 2 键然后松开
    "#": 51,  # 按下 3 键然后松开
    "$": 52,  # 按下 4 键然后松开
    "%": 53,  # 按下 5 键然后松开
    "^": 54,  # 按下 6 键然后松开
    "&": 55,  # 按下 7 键然后松开
    "*": 56,  # 按下 8 键然后松开
    "(": 57,  # 按下 9 键然后松开
    ")": 48,  # 按下 0 键然后松开
    "-": 189,  # 按下 - 键然后松开
    "=": 187,  # 按下 = 键然后松开
    "_": 189,  # 按下 Shift + - 键然后松开
    "+": 187,  # 按下 Shift + = 键然后松开
    "[": 219,  # 按下 [ 键然后松开
    "]": 221,  # 按下 ] 键然后松开
    "{": 219,  # 按下 Shift + [ 键然后松开
    "}": 221,  # 按下 Shift + ] 键然后松开
    "|": 220,  # 按下 \ 键然后松开
    "\\": 220,  # 按下 Shift + \ 键然后松开
    ";": 186,  # 按下 ; 键然后松开
    ":": 186,  # 按下 Shift + ; 键然后松开
    "'": 186,  # 按下 ' 键然后松开
    '"': 186,  # 按下 Shift + ' 键然后松开
    ",": 188,  # 按下 , 键然后松开
    "<": 188,  # 按下 Shift + , 键然后松开
    ".": 190,  # 按下 . 键然后松开
    ">": 190,  # 按下 Shift + . 键然后松开
    "/": 191,  # 按下 / 键然后松开
    "?": 191,  # 按下 Shift + / 键然后松开
    " ": 32,  # 空格键
}


def type_string(string):
    for char in string:
        if char.isalpha():  # 字母
            char_code = ord(char.upper())
            win32api.keybd_event(char_code, 0, 0, 0)
            win32api.keybd_event(char_code, 0, win32con.KEYEVENTF_KEYUP, 0)
        elif char.isdigit():  # 数字
            win32api.keybd_event(ord(char), 0, 0, 0)
            win32api.keybd_event(ord(char), 0, win32con.KEYEVENTF_KEYUP, 0)
        elif char in special_keys:  # 特殊符号
            key_code = special_keys[char]
            win32api.keybd_event(key_code, 0, 0, 0)
            win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)
        # 可以根据需要添加更多字符类型的支持

        time.sleep(0.1)


def is_gameing():
    # 是否已经打开游戏
    hwnd = win32gui.FindWindow(
        "GAMEAPP",
        None,
    )
    print(hwnd)
    if not hwnd:
        return False
    title = win32gui.GetWindowText(hwnd)

    if title and "QQ飞车2.0" in title:
        return True
    else:
        return False


def login(user="", pwd=""):
    if not win32gui.FindWindow(None, "QQ飞车"):

        process = subprocess.Popen(
            ["D:\WeGameApps\QQ飞车\Releasephysx27\QQSpeed_Launch.exe"]
        )

    print("尝试登录")
    hwnd = 0
    while not hwnd:
        hwnd = win32gui.FindWindow(None, "QQ飞车")
        time.sleep(5)

        # 程序继续运行，不会等待记事本关闭
    win32gui.SetActiveWindow(hwnd)
    print("正在尝试登录,请勿操作鼠标键盘")
    click_for_img_wait("./imgs/user.bmp", 100)
    type_string(user)
    time.sleep(0.5)
    win32gui.SetActiveWindow(hwnd)
    click_for_img_wait("./imgs/pwd.bmp", 100)
    type_string(pwd)
    click_for_img_wait("./imgs/login.bmp")
    # 等待游戏窗口
    while not win32gui.FindWindow("GAMEAPP", None):
        print("等待游戏窗口...")
        time.sleep(3)
    print("登录成功")
    time.sleep(10)


from pywinauto import Application


def send_key_to_window(window_title, key):
    # 连接到目标应用程序
    app = Application().connect(title=window_title)

    # 获取目标窗口
    window = app.window(title=window_title)

    # 激活窗口
    window.set_focus()

    # 发送按键
    while True:
        time.sleep(0.1)
        window.type_keys(key)


if __name__ == "__main__":
    send_key_to_window(
        "QQ飞车2.0 【联通区】【3.8-3.9 在线送A车-金钻女神+A车-圣光雪狐+12888点券+6倍开启！】 【Vision丶筱沫】【魔法学院】",
        "Z W {UP}",
    )
    print("")
