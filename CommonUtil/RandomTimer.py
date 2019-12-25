import time
import random


class RandomTimer:
    """
    随机时间延迟类，一共三个级别
    level=1：短延迟
    level=2：中等延迟
    level=3：高延迟

    """
    # 范围[x,x+y] 单位秒
    level_one_random = (0.5, 0.5)
    level_two_random = (1.5, 0.5)
    level_three_random = (2.5, 1)

    def __init__(self, level: int = 1):
        """
        初始化延迟级别
        :param level:
        """
        self.level = level

    def sleep_random_time(self):
        """
        随机延迟当前level的时间
        :return:
        """
        if self.level == 1:
            time.sleep(random.uniform(RandomTimer.level_one_random[0], RandomTimer.level_one_random[1]))
        elif self.level ==2:
            time.sleep(random.uniform(RandomTimer.level_two_random[0], RandomTimer.level_two_random[1]))
        elif self.level ==3:
            time.sleep(random.uniform(RandomTimer.level_three_random[0], RandomTimer.level_three_random[1]))

