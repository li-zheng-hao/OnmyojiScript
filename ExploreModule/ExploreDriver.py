import logging
import time
import random

from CommonUtil import ImgPath
from CommonUtil.CommonPosition import CommonPos
from CommonUtil.GlobalProperty import GlobalProperty
from CommonUtil.RandomTimer import RandomTimer
from YuHunModule.Fighter import Fighter


class ExploreDriver(Fighter):
    def __init__(self, hwnd):
        Fighter.__init__(self, '司机', hwnd)

    def start(self):
        """
        开始战斗
        :return:
        """
        self.run.start()
        while self.run.is_running():
            # 点击继续邀请队友战斗按钮，直到按钮消失 todo 更改路径和坐标
            # todo 先检测是否在探索主界面
            # self.game_control.wait_game_img(ImgPath.get_img_file_path() + ImgPath.YOU_JIAN)
            # todo 再开始不断点击战斗按钮
            self.random_timer_level_three.sleep_random_time()
            self.click_until('继续邀请队友战斗按钮', ImgPath.get_img_file_path() + ImgPath.EXPLORE_QUE_DING,
                             *CommonPos.EXPLORE_JI_XU_YAO_QING_RECT, False)
            # 场景拖动次数 次数要能够拖完整个场景
            move_count = 4
            # 寻找经验怪和boss
            while self.run.is_running() and move_count > 0:
                result = self.fight_monster()
                if result == 1:
                    continue
                elif result == 2:
                    break
                else:
                    logging.info('未找到经验怪或boss，司机拖动至右侧场景')
                    self.next_scene()
                    move_count -= 1

            self.random_timer_level_two.sleep_random_time()

            # 打完了 退出场景
            self.game_control.find_game_img(ImgPath.get_img_file_path() + ImgPath.EXPLORE_QUIT, False)
            self.game_control.mouse_click_bg(*CommonPos.EXPLORE_QUIT_RECT)
            # self.random_timer_level_two.sleep_random_time()
            logging.info('司机第一次点击退出探索成功')

            que_ding_pos = self.game_control.wait_game_img(ImgPath.get_img_file_path() + ImgPath.EXPLORE_QUE_REN)
            self.game_control.mouse_click_bg(*CommonPos.EXPLORE_TUI_CHU_QUE_REN_RECT)
            logging.info('司机第二次点击退出探索成功')

            # self.random_timer_level_three.sleep_random_time()

    def fight_monster(self):
        """
        打经验怪
        :return: 打完普通怪返回1；打完boss返回2；未找到经验怪返回-1；未找到经验怪和boss返回-2
        """
        while self.run.is_running():
            # 查看是否进入探索界面
            self.game_control.wait_game_img(ImgPath.get_img_file_path() + ImgPath.YING_BING)
            logging.info('司机进入探索页面')
            find_boss = False
            # 寻找经验怪，未找到则寻找boss，再未找到则退出
            fight_pos = self.find_exp_moster()
            if fight_pos == -1:
                fight_pos = self.find_boss()
                if fight_pos == -1:
                    logging.info('未找到经验怪和boss')
                    return -2
                find_boss = True
            # 攻击怪
            logging.info('司机点击怪物头顶战斗标志,坐标为{}'.format(fight_pos))
            self.game_control.mouse_click_bg(fight_pos)
            if self.game_control.wait_game_img(ImgPath.get_img_file_path() + ImgPath.JIN_RU_ZHAN_DOU, 30,
                                               False) is False:
                logging.error('进入战斗失败')
                break
            logging.info('司机已进入战斗')
            self.random_timer_level_two.sleep_random_time()

            # 等待式神准备
            self.game_control.wait_game_color(((1024, 524), (1044, 544)), (138, 198, 233), 50)
            logging.info('式神准备完成')

            # 检查狗粮经验
            self.check_exp_full()
            if self.run.is_running() is False:
                return False
            # 点击准备，直到进入战斗
            pos = self.game_control.wait_game_img(ImgPath.get_img_file_path() + ImgPath.ZHUN_BEI)
            logging.info('准备按钮已出现,司机点击！')
            self.game_control.mouse_click_bg(*CommonPos.ZHUN_BEI_RECT)
            # 检查是否打完
            self.wait_fight_end()

            if self.run.is_running() is False:
                return False

            self.random_timer_level_two.sleep_random_time()
            # 点击第一次结算
            self.click_until('第一次结算', ImgPath.get_img_file_path() + ImgPath.JIN_BI,
                             *CommonPos.JIE_SUAN_FIRST_POS_RECT, appear=True)
            # logging.info('司机点击了第一次结算的位置{}'.format(CommonPosition.JIE_SUAN_FIRST_POS))
            if self.run.is_running() is False:
                return False
            self.random_timer_level_one.sleep_random_time()

            # 点击第二次结算
            self.click_until('第二次结算', ImgPath.get_img_file_path() + ImgPath.JIN_BI,
                             *CommonPos.JIE_SUAN_SECOND_POS_RECT, appear=False)
            if self.run.is_running() is False:
                return False

            # 返回结果
            if find_boss:
                return 2
            else:
                return 1

    def find_exp_moster(self):
        '''
        寻找经验怪
            return: 成功返回经验怪的攻打图标位置；失败返回-1
        '''
        # 查找经验图标
        exp_pos = self.game_control.find_color(
            ((2, 205), (1127, 545)), (140, 122, 44), 10)
        if exp_pos == -1:
            return -1
        # 查找经验怪攻打图标位置
        find_pos = self.game_control.find_game_img(
            ImgPath.get_img_file_path() + ImgPath.EXPLORE_ZHAN_DOU, True, (exp_pos[0] - 150, exp_pos[1] - 250),
            (exp_pos[0] + 150, exp_pos[1] - 50))
        if not find_pos:
            return -1

        # 返回经验怪攻打图标位置
        fight_pos = ((find_pos[0] + exp_pos[0] - 150),
                     (find_pos[1] + exp_pos[1] - 250))
        return fight_pos

    def next_scene(self):
        '''
        移动至下一个场景，每次移动600像素
        '''
        x0 = random.randint(1000, 1126)
        x1 = x0 - 800
        y0 = random.randint(110, 210)
        y1 = random.randint(110, 210)
        self.game_control.mouse_drag_bg((x0, y0), (x1, y1))

    def check_exp_full(self):
        '''
        检查狗粮经验是否满了，并自动换狗粮
        '''
        # 狗粮经验判断, gouliang1是中间狗粮，gouliang2是右边狗粮
        gou_liang1_pos = self.game_control.find_game_img(
            ImgPath.get_img_file_path() + ImgPath.EXPLORE_GOU_LIANG_MAN, True,
            *CommonPos.EXPLORE_DUAL_DRIVER_CHECK_FULL_LEFT_RECT)
        gou_liang2_pos = self.game_control.find_game_img(
            ImgPath.get_img_file_path() + ImgPath.EXPLORE_GOU_LIANG_MAN, True,
            *CommonPos.EXPLORE_DUAL_DRIVER_CHECK_FULL_RIGHT_RECT
        )
        #
        # gou_liang1_pos = self.game_control.find_color(CommonPos.EXPLORE_DUAL_DRIVER_CHECK_FULL_LEFT_RECT, (201, 121, 24), 1)
        # gou_liang2_pos = self.game_control.find_color(CommonPos.EXPLORE_DUAL_DRIVER_CHECK_FULL_RIGHT_RECT, (201, 121, 24), 1)
        # 如果都没满则退出
        if  not gou_liang1_pos  and not gou_liang2_pos:
            logging.info('司机狗粮没有满级')
            return False
        logging.info('司机开始换狗粮')
        # 开始换狗粮
        while self.run.is_running():
            # 点击狗粮位置
            self.game_control.mouse_click_bg(*CommonPos.EXPLORE_REPLACE_SHI_SHEN_CLICK_RECT)
            if self.game_control.wait_game_img(ImgPath.get_img_file_path() + ImgPath.EXPLORE_QUAN_BU, 5, False):
                break
        time.sleep(1)
        logging.info('司机点击换狗粮区域成功')
        # 点击“全部”选项
        self.game_control.mouse_click_bg(*CommonPos.EXPLORE_QUAN_BU_RECT)
        time.sleep(1)
        # 点击“N”卡
        self.game_control.mouse_click_bg(*CommonPos.EXPLORE_N_POS_RECT)
        time.sleep(1)

        # 拖动N卡
        pos_begin = CommonPos.EXPLORE_SLIDER_DEFAULT_AND_MIN_POS
        add_val_x = int(((CommonPos.EXPLORE_SLIDER_MAX_POS[0] - pos_begin[0]) * GlobalProperty.n_ka_slider_value / 100))
        pos_end = (pos_begin[0] + random.randint(add_val_x, add_val_x + 20), pos_begin[1])
        self.game_control.mouse_drag_bg(pos_begin,
                                        pos_end)
        self.random_timer_level_one.sleep_random_time()
        # 更换N卡位置中第一个和第二个狗粮
        if gou_liang1_pos:
            self.game_control.mouse_drag_bg(CommonPos.EXPLORE_N_FIRST_RECT[0],
                                            CommonPos.EXPLORE_DUAL_DRIVER_LEFT_RECT[0])
        self.random_timer_level_one.sleep_random_time()
        if gou_liang2_pos:
            self.game_control.mouse_drag_bg(CommonPos.EXPLORE_N_SECOND_RECT[0],
                                            CommonPos.EXPLORE_DUAL_DRIVER_RIGHT_RECT[0])

    def find_boss(self):
        '''
        寻找BOSS
            :return: 成功返回BOSS的攻打图标位置；失败返回-1
        '''
        # 查找BOSS攻打图标位置
        find_pos = self.game_control.find_game_img(
            ImgPath.get_img_file_path() + ImgPath.EXPLORE_BOSS, False)
        if not find_pos:
            return -1

        # 返回BOSS攻打图标位置
        fight_pos = ((find_pos[0] + 10), (find_pos[1] + 10))
        logging.info('司机找到boss')
        return fight_pos

    def stop(self):
        self.run.stop()
