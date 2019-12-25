import ctypes
import logging
import sys
import threading

from PyQt5.QtWidgets import QMainWindow, QApplication

from CommonUtil.CommonPosition import CommonPos
from CommonUtil.GlobalProperty import GlobalProperty
from CommonUtil.Logger import QTextEditLogger
from ExploreModule.ExploreTwoPerson import ExploreTwoPerson
from ImageProcessModule.GameWindow import GameWindow
from YuHunModule.State import State
from YuHunModule.YuHunDriver import YuHunDriver
from YuHunModule.YuHunPassenger import YuHunPassenger
from YuHunModule.YuHunThreePerson import YuHunThreePerson
from YuHunModule.YuHunTwoPerson import YuHunTwoPerson

sys.path.append('..')

from GuiModule.MainWindow import Ui_MainWindow
from CommonUtil.IsAdmin import is_admin


class AppStart(QMainWindow):
    def __init__(self, parent=None):
        super(AppStart, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        logger = QTextEditLogger(self, logger_ui=self.ui.textBrowser)
        # logger.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.setFormatter(logging.Formatter("%(asctime)s - %(message)s", "%H:%M:%S"))
        logging.getLogger().addHandler(logger)
        logging.getLogger().setLevel(logging.DEBUG)
        logging.info('程序启动')
        # 信号槽连接
        self.ui.start_btn.clicked.connect(self.start)
        self.ui.end_btn.clicked.connect(self.stop)
        self.ui.quit_btn.clicked.connect(self.quit)
        self.state = State()

    def init_property(self):
        """
        初始化一些游戏参数
        :return:
        """
        GlobalProperty.need_mark_shi_shen = self.ui.need_mark_shi_shen.isChecked()
        GlobalProperty.mark_shi_shen_index = self.ui.mark_shi_shen_pos_index.value()
        GlobalProperty.n_ka_slider_value=self.ui.n_ka_slider.value()
        if self.ui.system_resize_resolution.currentIndex() == 0:
            logging.info('当前系统缩放比例为{}'.format(self.ui.system_resize_resolution.itemText(0)))
            GlobalProperty.window_resize_resolution = 1.25
        else:
            logging.info('当前系统缩放比例为{}'.format(self.ui.system_resize_resolution.itemText(1)))
            GlobalProperty.window_resize_resolution = 1

    def start(self):
        """
        开始运行脚本
        :return:
        """
        if self.state.is_running():
            logging.info('脚本已启动')
            return False
        logging.info('启动脚本')
        self.init_property()
        CommonPos.InitCommonPosWithSystemResolution()
        # 判断当前选项
        if self.ui.page.currentIndex() == 0:
            # 御魂
            if self.ui.yuhun_single.isChecked():
                # todo
                logging.info('暂不支持单刷')
                pass
            elif self.ui.yuhun_driver.isChecked():
                hwndlist = GameWindow.get_game_hwnd()
                if len(hwndlist) != 1:
                    logging.error('窗体数量异常')
                    return False
                self.fighter = YuHunDriver(hwndlist[0])
                is_running = True
                task1 = threading.Thread(target=self.fighter.start)
                task1.start()
            elif self.ui.yuhun_passenger.isChecked():
                hwndlist = GameWindow.get_game_hwnd()
                if len(hwndlist) != 1:
                    logging.error('窗体数量异常')
                    return False
                self.fighter = YuHunPassenger(hwndlist[0])
                is_running = True
                task1 = threading.Thread(target=self.fighter.start)
                task1.start()
            elif self.ui.yuhun_two.isChecked():
                GlobalProperty.passenger_num = 1
                self.fighter = YuHunTwoPerson()
                is_running = self.fighter.start()

            elif self.ui.yuhun_three.isChecked():
                GlobalProperty.passenger_num = 2
                self.fighter = YuHunThreePerson()
                is_running = self.fighter.start()
        elif self.ui.page.currentIndex() == 1:
            # 探索界面
            self.fighter = ExploreTwoPerson()
            self.fighter.start()
            is_running=True

        if is_running:
            self.state.start()
        else:
            self.state.stop()

    def stop(self):
        """
        停止运行脚本
        :return:
        """
        if self.state.is_running() is False:
            logging.info('脚本未运行')
            return False
        logging.info('停止脚本')
        self.state.stop()
        self.fighter.stop()

    def quit(self):
        """
        退出脚本
        :return:
        """
        logging.info('退出脚本')
        sys.exit(0)


if __name__ == "__main__":
    try:
        # 检测管理员权限
        if is_admin():
            app = QApplication(sys.argv)
            myWin = AppStart()
            myWin.show()
            sys.exit(app.exec_())
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    except Exception as e:
        raise e
