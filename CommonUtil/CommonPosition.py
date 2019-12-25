# 常量坐标
import logging

from CommonUtil.GlobalProperty import GlobalProperty


class CommonPos:
    # ---------------公共部分--------------------------
    # 拒绝悬赏 点击坐标
    REJECT_BOUNTY_POS = (757, 460)
    # 战斗准备
    ZHUN_BEI_RECT = (1070, 570), (1075, 575)
    # 第一次点击结算位置
    JIE_SUAN_FIRST_POS_RECT = (1000, 100), (1111, 452)

    # 第二次点击结算位置
    JIE_SUAN_SECOND_POS_RECT = (1000, 100), (1111, 452)

    # ---------------御魂部分--------------------------

    # 御魂自动邀请第一次点击位置(小勾)
    ZI_DONG_YAO_QING_FIRST_POS = (497, 319)

    # 御魂自动邀请第二次点击位置(确定)
    ZI_DONG_YAO_QING_SECOND_POS = (674, 384)

    # 御魂开始战斗按钮位置
    KAI_SHI_ZHAN_DOU_POS_RECT = (1085, 566),(1088, 570)

    # 御魂标记第一个式神位置
    SHI_SHEN_ONE_POS_RECT = (125, 360), (145, 380)
    # 御魂标记第二个式神位置
    SHI_SHEN_TWO_POS_RECT = (310, 380), (320, 390)
    # 御魂标记第三个式神位置
    SHI_SHEN_THREE_POS_RECT = (533, 463), (535, 465)
    # 御魂标记第四个式神位置
    SHI_SHEN_FOUR_POS_RECT = (715, 385), (730, 415)
    # 御魂标记第五个式神位置
    SHI_SHEN_FIVE_POS_RECT = (941, 420), (945, 425)

    # 御魂自动邀请接受
    YU_HUN_ZI_DONG_JIE_SHOU_YAO_QING = (200, 220), (210, 230)
    # 御魂邀请接受
    YU_HUN_JIE_SHOU_YAO_QING = (120, 220), (130, 230)

    # ---------------探索部分--------------------------
    # 更换式神的时候的区域
    EXPLORE_DUAL_DRIVER_LEFT_RECT = (830, 288), (833, 290)
    EXPLORE_DUAL_DRIVER_RIGHT_RECT = (292, 307), (294, 309)
    # 检测经验满的时候的区域
    EXPLORE_DUAL_DRIVER_CHECK_FULL_LEFT_RECT = (0, 0), (200, 475)
    EXPLORE_DUAL_DRIVER_CHECK_FULL_RIGHT_RECT = (400, 400), (600, 570)

    EXPLORE_DUAL_PASSENGER_CHECK_FULL_MID_RECT = (400, 260), (530, 447)
    EXPLORE_DUAL_PASSENGER_CHECK_FULL_RIGHT_RECT = (580, 310), (770, 500)
    # 左侧狗粮队长固定
    EXPLORE_DUAL_PASSENGER_MID_RECT = (545, 240), (590, 270)
    EXPLORE_DUAL_PASSENGER_RIGHT_RECT = (166, 259), (207, 300)

    # 更换式神要点击的区域
    EXPLORE_REPLACE_SHI_SHEN_CLICK_RECT = (340, 523), (340, 526)
    # 更换狗粮的全部按钮
    EXPLORE_QUAN_BU_RECT = (45, 575), (80, 605)
    # N卡位置按钮
    EXPLORE_N_POS_RECT = (140, 285), (170, 320)
    # 第一个N卡的点击区域
    EXPLORE_N_FIRST_RECT = (173, 480), (220, 550)
    # 第二个N卡的点击区域
    EXPLORE_N_SECOND_RECT = (290, 480), (330, 550)

    # 退出探索
    EXPLORE_QUIT_RECT = (40, 45), (50, 70)
    # 继续邀请队友
    EXPLORE_JI_XU_YAO_QING_RECT = (672, 389), (680, 395)

    # 退出探索确认
    EXPLORE_TUI_CHU_QUE_REN_RECT = (684, 357), (688, 360)

    # 换狗粮滑动条最低值也就是默认值
    EXPLORE_SLIDER_DEFAULT_AND_MIN_POS = (165, 610)
    # 换狗粮滑动条最大值
    EXPLORE_SLIDER_MAX_POS = (780, 610)

    @staticmethod
    def InitCommonPosWithSystemResolution():
        """
        根据系统分辨率缩放比例来调整所有的常量坐标
        :return:
        """
        logging.info('当前设置的系统分辨率为{}'.format(GlobalProperty.window_resize_resolution))
        CommonPos.REJECT_BOUNTY_POS = (round(CommonPos.REJECT_BOUNTY_POS[0] * GlobalProperty.window_resize_resolution),
                                       round(CommonPos.REJECT_BOUNTY_POS[1] * GlobalProperty.window_resize_resolution))
        CommonPos.JIE_SUAN_FIRST_POS_RECT = (round(
            CommonPos.JIE_SUAN_FIRST_POS_RECT[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.JIE_SUAN_FIRST_POS_RECT[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.JIE_SUAN_FIRST_POS_RECT[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.JIE_SUAN_FIRST_POS_RECT[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.JIE_SUAN_SECOND_POS_RECT = (round(
            CommonPos.JIE_SUAN_SECOND_POS_RECT[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.JIE_SUAN_SECOND_POS_RECT[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.JIE_SUAN_SECOND_POS_RECT[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.JIE_SUAN_SECOND_POS_RECT[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.ZI_DONG_YAO_QING_FIRST_POS = (
            round(CommonPos.ZI_DONG_YAO_QING_FIRST_POS[0] * GlobalProperty.window_resize_resolution),
            round(CommonPos.ZI_DONG_YAO_QING_FIRST_POS[1] * GlobalProperty.window_resize_resolution))

        CommonPos.ZI_DONG_YAO_QING_SECOND_POS = (
            round(CommonPos.ZI_DONG_YAO_QING_SECOND_POS[0] * GlobalProperty.window_resize_resolution),
            round(CommonPos.ZI_DONG_YAO_QING_SECOND_POS[1] * GlobalProperty.window_resize_resolution))

        CommonPos.KAI_SHI_ZHAN_DOU_POS_RECT = (round(
            CommonPos.KAI_SHI_ZHAN_DOU_POS_RECT[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.KAI_SHI_ZHAN_DOU_POS_RECT[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.KAI_SHI_ZHAN_DOU_POS_RECT[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.KAI_SHI_ZHAN_DOU_POS_RECT[1][1] * GlobalProperty.window_resize_resolution))
        # logging.info('御魂开始战斗按钮区域{}'.format(CommonPos.KAI_SHI_ZHAN_DOU_POS_RECT))
        CommonPos.SHI_SHEN_ONE_POS_RECT = (round(
            CommonPos.SHI_SHEN_ONE_POS_RECT[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_ONE_POS_RECT[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.SHI_SHEN_ONE_POS_RECT[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_ONE_POS_RECT[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.SHI_SHEN_TWO_POS_RECT = (round(
            CommonPos.SHI_SHEN_TWO_POS_RECT[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_TWO_POS_RECT[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.SHI_SHEN_TWO_POS_RECT[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_TWO_POS_RECT[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.SHI_SHEN_THREE_POS_RECT = (round(
            CommonPos.SHI_SHEN_THREE_POS_RECT[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_THREE_POS_RECT[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.SHI_SHEN_THREE_POS_RECT[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_THREE_POS_RECT[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.SHI_SHEN_FOUR_POS_RECT = (round(
            CommonPos.SHI_SHEN_FOUR_POS_RECT[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_FOUR_POS_RECT[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.SHI_SHEN_FOUR_POS_RECT[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_FOUR_POS_RECT[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.SHI_SHEN_FIVE_POS_RECT = (round(
            CommonPos.SHI_SHEN_FIVE_POS_RECT[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_FIVE_POS_RECT[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.SHI_SHEN_FIVE_POS_RECT[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_FIVE_POS_RECT[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.YU_HUN_ZI_DONG_JIE_SHOU_YAO_QING = (round(
            CommonPos.YU_HUN_ZI_DONG_JIE_SHOU_YAO_QING[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.YU_HUN_ZI_DONG_JIE_SHOU_YAO_QING[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.YU_HUN_ZI_DONG_JIE_SHOU_YAO_QING[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.YU_HUN_ZI_DONG_JIE_SHOU_YAO_QING[1][1] * GlobalProperty.window_resize_resolution))
        CommonPos.YU_HUN_JIE_SHOU_YAO_QING = (round(
            CommonPos.YU_HUN_JIE_SHOU_YAO_QING[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.YU_HUN_JIE_SHOU_YAO_QING[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.YU_HUN_JIE_SHOU_YAO_QING[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.YU_HUN_JIE_SHOU_YAO_QING[1][1] * GlobalProperty.window_resize_resolution))

# CommonPos.InitCommonPosWithSystemResolution()
# print(CommonPos.JIE_SUAN_FIRST_POS)
