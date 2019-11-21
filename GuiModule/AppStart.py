import ctypes
import logging
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from CommonUtil.GlobalProperty import GlobalProperty
from CommonUtil.Logger import QTextEditLogger
from YuHunModule.State import State
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
        logger.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logger)
        logging.getLogger().setLevel(logging.DEBUG)
        logging.info('------------程序启动-------------')
        self.init_property()
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
        if self.ui.system_resize_resolution.currentIndex() == 0:
            GlobalProperty.window_resize_resolution = 1.25
        else:
            GlobalProperty.window_resize_resolution = 1

    def start(self):
        """
        开始运行脚本
        :return:
        """
        # todo
        if self.state.is_running():
            logging.info('脚本已启动')
            return False
        logging.info('启动脚本')
        # 判断当前选项
        if self.ui.page.currentIndex() == 0:
            # 御魂
            if self.ui.yuhun_single.isChecked():
                # todo
                pass
            elif self.ui.yuhun_driver.isChecked():
                # todo
                pass
            elif self.ui.yuhun_passenger.isChecked():
                # todo
                pass

            elif self.ui.yuhun_two.isChecked():
                GlobalProperty.passenger_num = 1
                self.fighter = YuHunTwoPerson()
                self.fighter.start()

            elif self.ui.yuhun_three.isChecked():
                GlobalProperty.passenger_num = 2
                self.fighter = YuHunThreePerson()
                self.fighter.start()

        self.state.start()

    def stop(self):
        """
        停止运行脚本
        :return:
        """
        # todo
        pass
        if self.state.is_running() is False:
            logging.info('脚本已停止')
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
