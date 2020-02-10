import logging
import random
import time

from CommonUtil import ImgPath, CommonPosition
from CommonUtil.CommonPosition import CommonPos
from CommonUtil.GlobalProperty import GlobalProperty
from YuHunModule.Fighter import Fighter


class ExplorePassenger(Fighter):
    def __init__(self, hwnd):
        Fighter.__init__(self, '乘客', hwnd)

    def start(self):
        """
        开始战斗
        :return:
        """
        self.run.start()
        while self.run.is_running():
            self.game_control.take_screenshot()

            # 等待游戏结算
            self.wait_fight_end()
            self.random_timer_level_two.sleep_random_time()

            # 点击第一次结算
            self.click_until('结算', ImgPath.get_img_file_path() + ImgPath.JIN_BI,
                             *CommonPos.JIE_SUAN_FIRST_POS_RECT, appear=True)

            self.random_timer_level_one.sleep_random_time()
            if self.run.is_running() is False:
                return False
            # 点击第二次结算
            self.click_until('结算', ImgPath.get_img_file_path() + ImgPath.JIN_BI,
                             *CommonPos.JIE_SUAN_SECOND_POS_RECT, appear=False)




    def stop(self):
        self.run.stop()
