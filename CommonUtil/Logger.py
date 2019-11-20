# 日志系统
import logging

from PyQt5 import QtWidgets


class QTextEditLogger(logging.Handler):
    def __init__(self, parent,logger_ui):
        super().__init__()
        self.widget = logger_ui
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.append(msg)


class Logger:
    # 只会在第一次调用类的时候执行一次
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s  %(filename)s  [line:%(lineno)d]  %(levelname)s  %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='../log.log',
                        filemode='w')

    # 定义一个StreamHandler，将DEBUG级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    @staticmethod
    def write_info(*args, **kwargs):
        logging.info(*args, **kwargs)

    @staticmethod
    def write_warning(*args, **kwargs):
        logging.warning(*args, **kwargs)
