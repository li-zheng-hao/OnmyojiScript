# 常量坐标
from CommonUtil.GlobalProperty import GlobalProperty


class CommonPos:
    # 拒绝悬赏 点击坐标
    REJECT_BOUNTY_POS = (757, 460)

    # 第一次点击结算位置
    JIE_SUAN_FIRST_POS = (1000, 100), (1111, 452)

    # 第二次点击结算位置
    JIE_SUAN_SECOND_POS = (1000, 100), (1111, 452)

    # 御魂自动邀请第一次点击位置(小勾)
    ZI_DONG_YAO_QING_FIRST_POS = (497, 319)

    # 御魂自动邀请第二次点击位置(确定)
    ZI_DONG_YAO_QING_SECOND_POS = (674, 384)

    # 御魂开始战斗按钮位置
    KAI_SHI_ZHAN_DOU_POS = (1048, 535), (1113, 604)

    # 御魂标记第一个式神位置
    SHI_SHEN_ONE_POS = (125, 360), (145, 380)
    # 御魂标记第二个式神位置
    SHI_SHEN_TWO_POS = (310, 380), (320, 390)
    # 御魂标记第三个式神位置
    SHI_SHEN_THREE_POS = (540, 388), (545, 390)
    # 御魂标记第四个式神位置
    SHI_SHEN_FOUR_POS = (715, 385), (730, 415)
    # 御魂标记第五个式神位置
    SHI_SHEN_FIVE_POS = (925, 390), (945, 410)

    @staticmethod
    def InitCommonPosWithSystemResolution():
        """
        根据系统分辨率缩放比例来调整所有的常量坐标
        :return:
        """
        CommonPos.REJECT_BOUNTY_POS = (round(CommonPos.REJECT_BOUNTY_POS[0] * GlobalProperty.window_resize_resolution),
                                       round(CommonPos.REJECT_BOUNTY_POS[1] * GlobalProperty.window_resize_resolution))
        CommonPos.JIE_SUAN_FIRST_POS = (round(
            CommonPos.JIE_SUAN_FIRST_POS[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.JIE_SUAN_FIRST_POS[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.JIE_SUAN_FIRST_POS[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.JIE_SUAN_FIRST_POS[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.JIE_SUAN_SECOND_POS = (round(
            CommonPos.JIE_SUAN_SECOND_POS[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.JIE_SUAN_SECOND_POS[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.JIE_SUAN_SECOND_POS[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.JIE_SUAN_SECOND_POS[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.ZI_DONG_YAO_QING_FIRST_POS = (
            round(CommonPos.ZI_DONG_YAO_QING_FIRST_POS[0] * GlobalProperty.window_resize_resolution),
            round(CommonPos.ZI_DONG_YAO_QING_FIRST_POS[1] * GlobalProperty.window_resize_resolution))

        CommonPos.ZI_DONG_YAO_QING_SECOND_POS = (
            round(CommonPos.ZI_DONG_YAO_QING_SECOND_POS[0] * GlobalProperty.window_resize_resolution),
            round(CommonPos.ZI_DONG_YAO_QING_SECOND_POS[1] * GlobalProperty.window_resize_resolution))

        CommonPos.KAI_SHI_ZHAN_DOU_POS = (round(
            CommonPos.KAI_SHI_ZHAN_DOU_POS[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.KAI_SHI_ZHAN_DOU_POS[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.KAI_SHI_ZHAN_DOU_POS[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.KAI_SHI_ZHAN_DOU_POS[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.SHI_SHEN_ONE_POS = (round(
            CommonPos.SHI_SHEN_ONE_POS[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_ONE_POS[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.SHI_SHEN_ONE_POS[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_ONE_POS[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.SHI_SHEN_TWO_POS = (round(
            CommonPos.SHI_SHEN_TWO_POS[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_TWO_POS[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.SHI_SHEN_TWO_POS[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_TWO_POS[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.SHI_SHEN_THREE_POS = (round(
            CommonPos.SHI_SHEN_THREE_POS[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_THREE_POS[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.SHI_SHEN_THREE_POS[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_THREE_POS[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.SHI_SHEN_FOUR_POS = (round(
            CommonPos.SHI_SHEN_FOUR_POS[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_FOUR_POS[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.SHI_SHEN_FOUR_POS[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_FOUR_POS[1][1] * GlobalProperty.window_resize_resolution))

        CommonPos.SHI_SHEN_FIVE_POS = (round(
            CommonPos.SHI_SHEN_FIVE_POS[0][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_FIVE_POS[0][1] * GlobalProperty.window_resize_resolution)), (round(
            CommonPos.SHI_SHEN_FIVE_POS[1][0] * GlobalProperty.window_resize_resolution), round(
            CommonPos.SHI_SHEN_FIVE_POS[1][1] * GlobalProperty.window_resize_resolution))




# CommonPos.InitCommonPosWithSystemResolution()
# print(CommonPos.JIE_SUAN_FIRST_POS)
