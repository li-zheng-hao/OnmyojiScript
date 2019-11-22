import logging
import time

from CommonUtil import ImgPath
from CommonUtil.CommonPosition import CommonPos
from CommonUtil.GlobalProperty import GlobalProperty
from CommonUtil.Logger import Logger
from CommonUtil.RandomTimer import RandomTimer
from ImageProcessModule.GameControl import GameControl
from YuHunModule.Fighter import Fighter
from YuHunModule.State import State


class YuHunDriver(Fighter):
    def __init__(self, hwnd):
        Fighter.__init__(self, '司机', hwnd)
        self.random_timer_level_one = RandomTimer(level=1)
        self.random_timer_level_two = RandomTimer(level=2)
        self.random_timer_level_three = RandomTimer(level=3)

    def start(self):
        self.run.start()

        while self.run.is_running():
            if GlobalProperty.passenger_num == 2:
                # 等待两个乘客都上车 加号消失
                self.game_control.wait_game_img(img_path=ImgPath.GetImgFilePath() + ImgPath.JIA_CHENG,
                                                max_time=GlobalProperty.max_no_response_time)
                self.random_timer_level_three.sleep_random_time()
                self.click_until('开始战斗', ImgPath.GetImgFilePath() + ImgPath.DUI_YOU_JIA_HAO,
                                 *CommonPos.KAI_SHI_ZHAN_DOU_POS, appear=False)

            elif GlobalProperty.passenger_num == 1:
                # 等待点击挑战按钮亮起点击
                pos = self.game_control.wait_game_img(img_path=ImgPath.GetImgFilePath() + ImgPath.KAI_SHI_ZHAN_DOU,
                                                      max_time=GlobalProperty.max_no_response_time)
                self.random_timer_level_two.sleep_random_time()
                self.game_control.mouse_click_bg(pos=pos, pos_end=(pos[0] + 10, pos[1] + 10))
                logging.info('司机点击开始战斗按钮成功')
            if self.run.is_running() is False:
                return False

            # 需要手动标记式神
            if GlobalProperty.need_mark_shi_shen is True:
                # 等待标记式神位置
                self.game_control.wait_game_img(ImgPath.GetImgFilePath() + ImgPath.ZI_DONG)
                # logging.info('自动图片出现')
                time.sleep(1)
                if GlobalProperty.mark_shi_shen_index == 1:
                    self.game_control.mouse_click_bg(*CommonPos.SHI_SHEN_ONE_POS)
                elif GlobalProperty.mark_shi_shen_index == 2:
                    self.game_control.mouse_click_bg(*CommonPos.SHI_SHEN_TWO_POS)
                elif GlobalProperty.mark_shi_shen_index == 3:
                    self.game_control.mouse_click_bg(*CommonPos.SHI_SHEN_THREE_POS)
                elif GlobalProperty.mark_shi_shen_index == 4:
                    self.game_control.mouse_click_bg(*CommonPos.SHI_SHEN_FOUR_POS)
                elif GlobalProperty.mark_shi_shen_index == 5:
                    self.game_control.mouse_click_bg(*CommonPos.SHI_SHEN_FIVE_POS_POS)
                else:
                    logging.error('标记式神失败，当前需要标记式神位置为{}'.format(GlobalProperty.mark_shi_shen_index))
                logging.info('成功标记式神')
            if self.run.is_running() is False:
                return False

            # 等待游戏结算
            self.wait_fight_end()

            self.random_timer_level_one.sleep_random_time()

            # 点击第一次结算
            self.click_until('第一次结算', ImgPath.GetImgFilePath() + ImgPath.JIN_BI,
                             *CommonPos.JIE_SUAN_FIRST_POS, appear=True)
            # logging.info('司机点击了第一次结算的位置{}'.format(CommonPosition.JIE_SUAN_FIRST_POS))
            if self.run.is_running() is False:
                return False
            self.random_timer_level_one.sleep_random_time()

            # 点击第二次结算
            self.click_until('第二次结算', ImgPath.GetImgFilePath() + ImgPath.JIN_BI,
                             *CommonPos.JIE_SUAN_SECOND_POS, appear=False)
            if self.run.is_running() is False:
                return False
            # 等待下一轮,顺便要检查自动邀请队友
            logging.info('司机等待下一轮')
            start_time = time.time()
            while time.time() - start_time <= GlobalProperty.max_no_response_time and self.run.is_running():
                if self.game_control.wait_game_img(img_path=ImgPath.GetImgFilePath() + ImgPath.KAI_SHI_ZHAN_DOU,
                                                   max_time=5, quit=False):
                    logging.info('司机进入房间')
                    break

                # 点击默认邀请
                if self.game_control.find_game_img(ImgPath.GetImgFilePath() + ImgPath.ZI_DONG_YAO_QING):
                    self.game_control.mouse_click_bg(CommonPos.ZI_DONG_YAO_QING_FIRST_POS)
                    time.sleep(1)
                    self.game_control.mouse_click_bg(CommonPos.ZI_DONG_YAO_QING_SECOND_POS)
                    logging.info('司机自动邀请自动邀请')

    def stop(self):
        self.run.stop()


if __name__ == '__main__':
    d = YuHunDriver(0)
    d.start()
