import logging
from enum import Enum

STATE_RUNNING = 'RUNNING'
STATE_STOP = 'STOP'


class State:
    # 运行状态
    state = STATE_STOP

    @staticmethod
    def stop():
        State.state = STATE_STOP


    @staticmethod
    def start():
        """
        切换运行状态
        :return:
        """
        State.state = STATE_RUNNING

    @staticmethod
    def is_running():
        """
        判断当前脚本运行状态
        :return:False为停止，True为正在运行
        """
        return State.state == STATE_RUNNING
