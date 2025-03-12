import time
import win32con
from Bkgnd import Bkgnd


class MyObject:
    """name：任务名，num：任务次数"""

    def __init__(
        self,
        app,
        name,
        num=1,
        is_over=False,
    ):
        self.app = app
        self.name = name
        self.num = num
        self.Done_unm = 0
        self.is_over = is_over

    def waiting(self):
        i = 0
        while not self.is_home() and not self.app.find_image("./imgs/back.bmp"):

            self.app.send_key(win32con.VK_UP)
            if i >= 6:
                i = 0
            else:
                i = i + 1
            print("\033[2K", end="\r")  # 清空当前行
            print("." * i, end="\r")  # 打印新的内容
            time.sleep(3)

    def is_home(self):
        self.app.click((0, 1))
        return self.app.find_image("./imgs/cd.bmp", 0.9998)

    def go_home(self):
        for i in range(5):
            self.app.send_key(win32con.VK_ESCAPE)  # esc
        P = self.app.find_image("./imgs/back.bmp")
        while P:
            self.app.click(P)
            P = self.app.find_image("./imgs/back.bmp")
        for i in range(5):
            self.app.send_key(win32con.VK_ESCAPE)  # esc
        for i in range(5):
            self.app.send_key(win32con.VK_BACK)  # back
        for i in range(5):
            self.app.send_key(win32con.VK_ESCAPE)  # esc
        self.app.click((0, 1))
        self.app.click_for_img("./imgs/x.bmp")

    def fn(self):
        # print(f"Function called for {self.name}")

        if self.name == "边境":
            bianjing(self)
        elif self.name == "蛇蛇大作战":
            sheshedazuozhan(self)
        elif self.name == "双人冲锋战":
            shuangrenchongfengzhan(self)
        elif self.name == "宠物天梯对战":
            chongwutianti(self)
        elif self.name == "车队任务":
            cheduirenwu(self)
        elif self.name == "精灵任务":
            jinglingrenwu(self)
        elif self.name == "领取奖励":
            lingqujiangli(self)


def bianjing(self):  # 边境
    while not self.is_over:
        while not self.is_home():
            print("前往主菜单")
            self.go_home()
            time.sleep(5)
        self.app.click_for_img("./imgs/cd.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/dryx.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/bjzz.bmp")
        time.sleep(3.5)
        self.app.click_for_img("./imgs/ksjr.bmp")
        print("开始匹配，等待进入对局")
        title1 = self.app.get_window_title()
        time.sleep(61)
        title2 = self.app.get_window_title()
        if self.app.find_image("./imgs/km_h.bmp") or title1 != title2:
            # 对局开始，等待完成
            print("对局开始，等待完成")
            self.waiting()
            # 完成一次对局
            print("完成一次对局")
            self.Done_unm = self.Done_unm + 1
            if self.Done_unm >= self.num:
                self.is_over = True
        else:
            print("未找到对局")
            self.app.click_for_img("./imgs/ok.bmp")


def sheshedazuozhan(self):  # 蛇蛇大作战
    while not self.is_over:
        while not self.is_home():
            print("前往主菜单")
            self.go_home()
            time.sleep(5)
        self.app.click_for_img("./imgs/cd.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/dryx.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ssdzz.bmp")
        time.sleep(3.5)
        self.app.click_for_img("./imgs/ljpp.bmp")
        time.sleep(61)
        self.waiting()
        self.Done_unm = self.Done_unm + 1
        if self.Done_unm >= self.num:
            self.is_over = True


def shuangrenchongfengzhan(self):  # 双人冲锋战
    while not self.is_over:
        while not self.is_home():
            print("前往主菜单")
            self.go_home()
            time.sleep(5)
        self.app.click_for_img("./imgs/cd.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/dryx.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/srcfz.bmp")
        time.sleep(3.5)
        self.app.click_for_img("./imgs/srcfz_ljpp.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/srcfz_qw.bmp")
        time.sleep(3.5)
        self.app.click_for_img("./imgs/srcfz_ok.bmp")
        time.sleep(61)
        self.waiting()
        self.Done_unm = self.Done_unm + 1
        if self.Done_unm >= self.num:
            self.is_over = True


def chongwutianti(self):  # 宠物天梯对战
    while not self.is_over:
        while not self.is_home():
            print("前往主菜单")
            self.go_home()
            time.sleep(5)
        self.app.click_for_img("./imgs/cd.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/wdj.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/wdj_wdcw.bmp")
        time.sleep(1.5)
        self.app.click_for_img("./imgs/wdj_wdcw_dz.bmp")
        time.sleep(3.5)
        self.app.click_for_img("./imgs/wdj_wdcw_dz_ttdz.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/wdj_wdcw_dz_ttdz_kspp.bmp")
        time.sleep(31)
        self.waiting()
        self.Done_unm = self.Done_unm + 1
        if self.Done_unm >= self.num:
            self.is_over = True


def cheduirenwu(self):  # 车队任务
    while not self.is_over:
        while not self.is_home():
            print("前往主菜单")
            self.go_home()
            time.sleep(5)
        self.app.click_for_img("./imgs/cd.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/sj.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/sj_cdxt.bmp")
        time.sleep(1.5)
        self.app.click_for_img("./imgs/sj_cdxt_fl.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/sj_cdxt_fl_djlq.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ok.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/sj_cdxt_cdhb.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/sj_cdxt_cdhb_lqfd.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ok.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/sj_cdxt_cdhb_fhb.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/sj_cdxt_cdhb_fhb_fhb.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ok.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/sj_cdxt_cdhb_qhb.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/sj_cdxt_cdhb_qhb_qhb.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ok.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/x.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/sj_cdxt_cdrw.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/sj_cdxt_cdrw_yjlq.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ok.bmp")
        self.Done_unm = self.Done_unm + 1
        if self.Done_unm >= self.num:
            self.is_over = True


def jinglingrenwu(self):  # 精灵任务
    while not self.is_home():
        print("前往主菜单")
        self.go_home()
        time.sleep(5)
    self.app.click_for_img("./imgs/cd.bmp")
    time.sleep(0.5)
    self.app.click_for_img("./imgs/wdj.bmp")
    time.sleep(0.5)
    self.app.click_for_img("./imgs/wdj_wdjl.bmp")
    time.sleep(3.5)
    # 许愿树
    self.app.click((260, 477))
    time.sleep(1.5)
    for i in range(3):
        self.app.click_for_img("./imgs/wdj_wdjl_xys_qf.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ok.bmp")
        time.sleep(0.5)
    for j in range(2):
        for i in range(9):
            self.app.click_for_img("./imgs/wdj_wdjl_xys_bf.bmp", 0, 40 * i)
            time.sleep(3.5)
            self.app.click_for_img("./imgs/wdj_wdjl_xys_bf_js.bmp")
            time.sleep(0.5)
            self.app.click_for_img("./imgs/ok.bmp")
            time.sleep(0.5)
        self.app.click_for_img("./imgs/wdj_wdjl_xys_qtwj.bmp")
    self.app.click_for_img("./imgs/wdj_wdjl_jygn.bmp", -100, 0)
    time.sleep(3.5)
    # 打工
    self.app.click_for_img("./imgs/wdj_wdjl_jygn.bmp")
    time.sleep(0.5)
    self.app.click_for_img("./imgs/wdj_wdjl_jygn_jlgf.bmp")
    time.sleep(0.5)
    for i in range(11):
        print(f"开始地{i+1}次工作")
        self.app.click_for_img("./imgs/j.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ht.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ht1.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ok.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/lkks.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ok.bmp")
        print("等待20分钟...")
        time.sleep(20 * 60 + 3)
        self.app.click_for_img("./imgs/lqjl.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/ok.bmp")
        self.Done_unm = i + 1
    self.is_over = True


def lingqujiangli(self):  # 领取奖励
    while not self.is_home():
        print("前往主菜单")
        self.go_home()
        time.sleep(5)
    self.app.click_for_img("./imgs/cd.bmp")
    time.sleep(0.5)
    self.app.click_for_img("./imgs/rw.bmp")
    time.sleep(1.5)
    if self.app.find_image("./imgs/hyzx.bmp"):
        self.app.click_for_img("./imgs/djlq.bmp")
        time.sleep(0.5)
        self.app.click_for_img("./imgs/wzdl.bmp")
    self.app.click_for_img("./imgs/rw_yjlq.bmp")
    time.sleep(0.5)
    self.app.click_for_img("./imgs/ok.bmp")
    time.sleep(0.5)

    # 买金箩筐
    # while not self.is_home():
    #     print("前往主菜单")
    #     self.go_home()
    #     time.sleep(5)
    # self.app.click_for_img("./imgs/cd.bmp")
    # time.sleep(0.5)
    # self.app.click_for_img("./imgs/sc.bmp")
    # time.sleep(5)
    # self.app.click_for_img("./imgs/sousuo.bmp", -50, 0)

    self.is_over = True


def creatTasks(app):
    return [
        MyObject(app, "边境", 3),
        MyObject(app, "蛇蛇大作战"),
        MyObject(app, "双人冲锋战"),
        MyObject(app, "宠物天梯对战"),
        MyObject(app, "车队任务"),
        MyObject(app, "精灵任务"),
        MyObject(app, "领取奖励"),
    ]


if __name__ == "__main__":
    # 创建一个包含对象的列表
    list = [
        MyObject("边境"),
        MyObject("蛇蛇大作战"),
        MyObject("双人冲锋战"),
        MyObject("宠物天梯对战"),
        MyObject("车队任务"),
        MyObject("精灵任务"),
        MyObject("领取奖励"),
    ]

    while any(not obj.is_over for obj in list):
        # 调用对象的属性和方法
        for obj in list:
            if obj.is_over:
                continue

            print(
                f"任务名: {obj.name}, {'已完成' if obj.is_over else '剩余'+str(obj.num-obj.Done_unm)}"
            )
            obj.fn()
    print("所有任务已完成")
