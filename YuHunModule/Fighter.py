import logging
import time

from PIL import Image

from CommonUtil import ImgPath, CommonPosition
from CommonUtil.GlobalProperty import GlobalProperty
from CommonUtil.Logger import Logger
from CommonUtil.RandomTimer import RandomTimer
from ImageProcessModule.GameControl import GameControl
from YuHunModule.State import State


class Fighter:
    def __init__(self,name,hwnd):
        """
        初始化
        :param name: 司机或者乘客
        :param hwnd: 绑定的窗体句柄
        """
        self.name=name
        self.hwnd = hwnd
        # 控制子线程退出的变量
        self.run = State()
        self.random_timer_level_one = RandomTimer(level=1)
        self.random_timer_level_two = RandomTimer(level=2)
        self.random_timer_level_three = RandomTimer(level=3)
        self.game_control = GameControl(hwnd=hwnd, run=self.run, quit_game_enable=True)


    def find_color(self, region, color, tolerance=0):
        """
        寻找颜色
            :param region: ((x1,y1),(x2,y2)) 欲搜索区域的左上角坐标和右下角坐标
            :param color: (r,g,b) 欲搜索的颜色
            :param tolerance=0: 容差值
            :return: 成功返回客户区坐标，失败返回-1
        """

        img = Image.fromarray(self.window_part_shot(
            region[0], region[1]), 'RGB')
        width, height = img.size
        r1, g1, b1 = color[:3]
        for x in range(width):
            for y in range(height):
                try:
                    pixel = img.getpixel((x, y))
                    r2, g2, b2 = pixel[:3]
                    if abs(r1-r2) <= tolerance and abs(g1-g2) <= tolerance and abs(b1-b2) <= tolerance:
                        return x+region[0][0], y+region[0][1]
                except:
                    return -1
        return -1



    def click_until(self, tag: str, img_path: str, pos: tuple, pos_end: tuple = None, appear: bool = True):
        """
        不断点击pos坐标，直到图片消失或者出现
        :param tag: 出现或消失的图像tag
        :param img_path: 图像路径
        :param pos: 左上角位置
        :param pos_end: 右下角位置
        :param appear: True为出现，False为消失
        :return:
        """
        start_time = time.time()
        while time.time() - start_time <= GlobalProperty.max_no_response_time and self.run.is_running():
            logging.info('{}开始不断点击{}'.format(self.name,tag))
            result = self.game_control.find_game_img(img_path,False)
            if not appear:
                result = not result
            if result:
                return True
            else:
                # 点击指定位置并等待下一轮
                self.game_control.mouse_click_bg(pos, pos_end)
                logging.warning('{}不断点击{},直到{}为{}'.format(self.name,pos, tag,appear))
            time.sleep(0.5)
        logging.warning('{}点击{}失败'.format(self.name,tag))

        # 提醒玩家点击失败，并在5s后退出
        self.game_control.activate_window()
        time.sleep(5)
        self.game_control.quit_game()
        return False

    def wait_fight_end(self):
        """
        等待御魂副本战斗结束
        :return:
        """
        logging.info('{}:检测是战斗是否结束'.format(self.name))
        self.game_control.wait_game_img(img_path=ImgPath.get_img_file_path() + ImgPath.JIE_SHU, max_time=GlobalProperty.max_no_response_time)
        logging.info('{}:战斗已经否结束'.format(self.name))

    def wait_enter_fight(self):
        """
        等待进入战斗
        :return:返回检测到的坐标
        """
        logging.info('{}:检测是否进入战斗'.format(self.name))
        res=self.game_control.wait_game_img(img_path=ImgPath.get_img_file_path() + ImgPath.JIN_RU_ZHAN_DOU,
                                        max_time=12)
        logging.info('{}:检测到已经进入战斗,返回位置{}'.format(self.name,res))
        return res