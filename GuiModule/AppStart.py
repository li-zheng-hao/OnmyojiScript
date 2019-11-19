import ctypes
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from MainWindow import Ui_MainWindow
sys.path.append('..')
from CommonUtil.IsAdmin import is_admin


class AppStart(QMainWindow):
    def __init__(self, parent=None):
        super(AppStart, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


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
