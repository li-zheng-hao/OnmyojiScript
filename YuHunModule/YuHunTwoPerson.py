import logging
import threading

from CommonUtil import ImgPath
from ImageProcessModule.GameControl import GameControl
from ImageProcessModule.GameWindow import GameWindow
from YuHunModule.YuHunDriver import YuHunDriver
from YuHunModule.YuHunPassenger import YuHunPassenger


class YuHunTwoPerson():
    def __init__(self):
        """
        初始化
        :param needMark: 是否需要自动标记式神
        """
        # 初始化窗口信息
        self.hwndlist = GameWindow.get_game_hwnd()

        # 检测窗口信息是否正确
        num = len(self.hwndlist)
        if num == 2:
            logging.info('检测到两个窗口，窗口信息正常')
        else:
            logging.warning('检测到' + str(num) + '个窗口，窗口信息异常！')

        find_driver=False
        # 初始化司机和打手
        for hwnd in self.hwndlist:
            yys = GameControl(hwnd)

            if yys.find_game_img(img_path=ImgPath.GetImgFilePath()+ImgPath.KAI_SHI_ZHAN_DOU):
                self.driver = YuHunDriver(hwnd=hwnd)
                find_driver=True
                logging.info('发现司机,司机的窗体句柄为{}'.format(hwnd))
                self.hwndlist.remove(hwnd)
        if find_driver is False:
            logging.info('未找到司机，停止脚本')
            return False
        self.passenger = YuHunPassenger(hwnd=self.hwndlist[0])
        logging.info('发现乘客,乘客窗体句柄为{}'.format(self.hwndlist[0]))

    def start(self):
        task1 = threading.Thread(target=self.driver.start)
        task2 = threading.Thread(target=self.passenger.start)
        task1.start()
        task2.start()
        task1.join()
        task2.join()

    def stop(self):
        """
        停止脚本
        :return:
        """
        self.driver.stop()
        self.passenger.stop()