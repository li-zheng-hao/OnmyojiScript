import logging
import threading

import cv2

from CommonUtil import ImgPath
from ExploreModule.ExploreDriver import ExploreDriver
from ExploreModule.ExplorePassenger import ExplorePassenger
from ImageProcessModule.GameControl import GameControl
from ImageProcessModule.GameWindow import GameWindow
from YuHunModule.State import State


class ExploreTwoPerson():
    def __init__(self):
        """
        初始化
        """
        # 初始化窗口信息
        self.hwndlist = GameWindow.get_game_hwnd()

        # 检测窗口信息是否正确
        num = len(self.hwndlist)
        if num == 2:
            logging.info('检测到两个窗口，窗口信息正常')
        else:
            logging.warning('检测到' + str(num) + '个窗口，窗口信息异常！')

        find_driver = False
        # 初始化司机和打手
        for hwnd in self.hwndlist:

            yys = GameControl(hwnd, State())
            logging.info('开始寻找司机')
            # img=cv2.imread(ImgPath.GetImgFilePath()+ImgPath.KAI_SHI_ZHAN_DOU)
            # if img is None:
            #     logging.error('图片路径有问题：{}'.format(ImgPath.GetImgFilePath()+ImgPath.KAI_SHI_ZHAN_DOU))
            # 是否有继续邀请队友战斗
            # todo 探索 更换双开司机窗口的继续邀请战斗按钮路径图片
            if yys.find_game_img(ImgPath.get_img_file_path() + ImgPath.EXPLORE_QUE_DING, False):
                self.driver = ExploreDriver(hwnd=hwnd)
                find_driver = True
                logging.info('发现司机,司机的窗体句柄为{}'.format(hwnd))
                self.hwndlist.remove(hwnd)
        if find_driver is False:
            logging.error('未找到司机，停止脚本')
            self.init_state = False
            return None
        self.passenger = ExplorePassenger(hwnd=self.hwndlist[0])
        logging.info('发现乘客,乘客窗体句柄为{}'.format(self.hwndlist[0]))
        self.init_state = True

    def start(self):
        if self.init_state is False:
            return False
        task1 = threading.Thread(target=self.driver.start)
        task2 = threading.Thread(target=self.passenger.start)
        task1.start()
        task2.start()
        # task1.join()
        # task2.join()

    def stop(self):
        """
        停止脚本
        :return:
        """
        self.driver.stop()
        self.passenger.stop()
