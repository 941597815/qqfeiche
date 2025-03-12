import ctypes
from ctypes import wintypes
import win32con
import win32api
import win32gui
import pyautogui

# 定义必要的常量和结构
INPUT_KEYBOARD = 1
KEYEVENTF_KEYUP = 0x0002


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        # ("dwExtraInfo", wintypes.ULONG_PTR),
    ]


class INPUT(ctypes.Structure):
    _fields_ = [
        ("type", wintypes.DWORD),
        ("ki", KEYBDINPUT),
    ]


def send_key_to_window(hwnd, key):
    # 激活目标窗口
    win32gui.SetForegroundWindow(hwnd)

    win32api.keybd_event(key, 0, 0, 0)


# 获取目标窗口的句柄
hwnd = win32gui.FindWindow(
    "GAMEAPP",
    None,
)  # 替换为实际的窗口标题

# 按下 Z 键
send_key_to_window(hwnd, ord("Z"))

# 按下 W 键
send_key_to_window(hwnd, ord("W"))

# 按下 A 键
send_key_to_window(hwnd, ord("A"))

# 按下 S 键
send_key_to_window(hwnd, ord("S"))

# 按下 D 键
send_key_to_window(hwnd, ord("D"))

# 按下上箭头键
send_key_to_window(hwnd, win32con.VK_UP)
