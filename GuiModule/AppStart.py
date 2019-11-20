import ctypes
import logging
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from CommonUtil.Logger import QTextEditLogger

sys.path.append('..')

from GuiModule.MainWindow import Ui_MainWindow
from CommonUtil.IsAdmin import is_admin


class AppStart(QMainWindow):
    def __init__(self, parent=None):
        super(AppStart, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        logger = QTextEditLogger(self, logger_ui=self.ui.textBrowser)
        logging.getLogger().addHandler(logger)
        logging.getLogger().setLevel(logging.DEBUG)


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
