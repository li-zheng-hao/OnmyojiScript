import logging
import time

from CommonUtil import CommonPosition, ImgPath
from CommonUtil.GlobalProperty import GlobalProperty
from YuHunModule.Fighter import Fighter
from YuHunModule.State import State


class YuHunPassenger(Fighter):
    def __init__(self, hwnd):
        Fighter.__init__(self, '乘客', hwnd)

    def start(self):
        self.run.start()

        while self.run.is_running():
            # 等待游戏结算
            self.wait_fight_end()

            # 点击第一次结算
            self.click_until('结算', ImgPath.GetImgFilePath() + ImgPath.JIN_BI,
                             CommonPosition.JIE_SUAN_FIRST_POS, appear=True)
            # 点击第二次结算
            self.click_until('结算', ImgPath.GetImgFilePath() + ImgPath.JIN_BI,
                             CommonPosition.JIE_SUAN_SECOND_POS, appear=False)
            # 等待下一轮
            logging.info('乘客等待下一轮')
            start_time = time.time()
            while time.time() - start_time <= 20 and self.run:
                # 检测是否回到队伍中
                if (self.game_control.wait_game_img(ImgPath.GetImgFilePath() + ImgPath.XIE_ZHAN_DUI_WU, 1, False)):
                    logging.info('乘客进入队伍')
                    break

                # 检测是否有御魂邀请
                yuhun_loc = self.yys.wait_game_img(
                    ImgPath.GetImgFilePath() + ImgPath.YU_HUN, 0.1, False)
                logging.info('wait_game_img返回的坐标为:{}'.format(yuhun_loc))
                if yuhun_loc:
                    # 点击自动接受邀请
                    if self.yys.find_game_img(ImgPath.GetImgFilePath() + ImgPath.ZI_DONG_JIE_SHOU):
                        self.yys.mouse_click_bg((210, yuhun_loc[1]))
                        self.log.writeinfo('乘客自动接受邀请')

                    # 点击普通接受邀请
                    elif self.yys.find_game_img(ImgPath.GetImgFilePath() + ImgPath.JIE_SHOU):
                        self.yys.mouse_click_bg((125, yuhun_loc[1]))
                        self.log.writeinfo('乘客接受邀请')

    def stop(self):
        """
        停止脚本
        :return:
        """
        self.run.stop()

if __name__ == '__main__':
    d = YuHunPassenger(0)
    d.start()
