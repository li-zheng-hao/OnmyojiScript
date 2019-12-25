import logging
import random
import time

from CommonUtil import ImgPath
from CommonUtil.CommonPosition import CommonPos
from CommonUtil.GlobalProperty import GlobalProperty
from YuHunModule.Fighter import Fighter


class ExplorePassenger(Fighter):
    def __init__(self, hwnd):
        Fighter.__init__(self, '乘客', hwnd)

    def start(self):
        """
        开始战斗
        :return:
        """
        self.run.start()
        while self.run.is_running():
            # 点击继续邀请队友战斗按钮，直到按钮消失 todo 更改路径和坐标
            # todo 先检测是否在探索主界面
            self.game_control.wait_game_img(ImgPath.get_img_file_path() + ImgPath.EXPLORE_JIE_SHOU)
            logging.info('乘客在探索界面等待队友邀请按钮')
            # todo 等待队友邀请按钮
            pos = self.game_control.find_game_img(ImgPath.get_img_file_path() + ImgPath.EXPLORE_JIE_SHOU, False)
            self.game_control.mouse_click_bg(pos)
            self.random_timer_level_three.sleep_random_time()

            if self.run.is_running() is False:
                return False

            while self.run.is_running():
                # 检测是否进入战斗
                res_pos=self.wait_enter_fight()
                if res_pos is False and self.check_driver_is_quit() is True :
                    logging.info('队长退出了游戏，乘客开始退出')
                    # 10秒没有进入游戏，再判断队长是否退出了游戏 退出场景
                    self.game_control.find_game_img(ImgPath.get_img_file_path() + ImgPath.EXPLORE_QUIT, False)
                    self.game_control.mouse_click_bg(*CommonPos.EXPLORE_QUIT_RECT)
                    self.random_timer_level_three.sleep_random_time()
                    self.game_control.mouse_click_bg(*CommonPos.EXPLORE_TUI_CHU_QUE_REN_RECT)
                    # self.random_timer_level_three.sleep_random_time()
                    break
                logging.info('乘客进入了战斗')

                self.game_control.wait_game_color(((1024, 524), (1044, 544)), (138, 198, 233), 50)
                logging.info('式神准备完成')
                # 检查是否有经验没满的狗粮
                self.check_exp_full()

                if self.run.is_running() is False:
                    return False

                # 检查完开始准备
                self.game_control.wait_game_img(ImgPath.get_img_file_path() + ImgPath.ZHUN_BEI)
                self.random_timer_level_one.sleep_random_time()
                # self.game_control.mouse_click_bg(*CommonPos.ZHUN_BEI_RECT)
                self.click_until('准备',ImgPath.get_img_file_path() + ImgPath.ZHUN_BEI,*CommonPos.ZHUN_BEI_RECT,False)
                logging.info('乘客点击准备完成')
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

    def check_driver_is_quit(self):
        """
        判断司机是否退出了游戏
        :return:True 已退出，False继续在游戏
        """
        res = self.game_control.find_game_img(ImgPath.get_img_file_path() + ImgPath.EXPLORE_DUI_ZHANG_LOGO, False)
        logging.info('res:{}'.format(res))
        if res is not False:
            return False
        else:
            logging.info('队长退出了游戏')
            return True

    def check_exp_full(self):
        '''
        检查狗粮经验是否满了，并自动换狗粮
        '''
        self.random_timer_level_two.sleep_random_time()
        # 狗粮经验判断, gouliang1是中间狗粮，gouliang2是右边狗粮
        logging.info('乘客开始检查狗粮')
        gou_liang1_pos= self.game_control.find_game_img(
            ImgPath.get_img_file_path() + ImgPath.EXPLORE_GOU_LIANG_MAN, True,
            *CommonPos.EXPLORE_DUAL_PASSENGER_CHECK_FULL_MID_RECT)
        gou_liang2_pos= self.game_control.find_game_img(
            ImgPath.get_img_file_path() + ImgPath.EXPLORE_GOU_LIANG_MAN, True,
            *CommonPos.EXPLORE_DUAL_PASSENGER_CHECK_FULL_RIGHT_RECT)
        # gou_liang1_pos=self.game_control.find_color(CommonPos.EXPLORE_DUAL_PASSENGER_CHECK_FULL_MID_RECT,(201,121,24),2)
        # gou_liang2_pos=self.game_control.find_color(CommonPos.EXPLORE_DUAL_PASSENGER_CHECK_FULL_RIGHT_RECT,(201,121,24),2)
        logging.info('乘客检查完狗粮')
        # 如果都没满则退出
        if not gou_liang1_pos  and  not gou_liang2_pos:
            logging.info('乘客：狗粮都没满级 ')
            return False

        # 开始换狗粮
        while self.run.is_running():
            # 点击狗粮位置
            self.game_control.mouse_click_bg(*CommonPos.EXPLORE_REPLACE_SHI_SHEN_CLICK_RECT)
            if self.game_control.wait_game_img(ImgPath.get_img_file_path() + ImgPath.EXPLORE_QUAN_BU, 5, False):
                break
        time.sleep(1)

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
                                            CommonPos.EXPLORE_DUAL_PASSENGER_MID_RECT[0])
        if gou_liang2_pos:
            time.sleep(1)
            self.game_control.mouse_drag_bg(CommonPos.EXPLORE_N_SECOND_RECT[0],
                                            CommonPos.EXPLORE_DUAL_PASSENGER_RIGHT_RECT[0])

    def stop(self):
        self.run.stop()
