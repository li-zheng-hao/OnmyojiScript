# 存储所有图片的名称,函数调用时手动添加相对路径
import logging
import os
from .Logger import Logger

# ---------------公共部分--------------------------
from CommonUtil.GlobalProperty import GlobalProperty
import glob
XUAN_SHANG = 'XUAN-SHANG.png'
JIN_BI = 'JIN-BI.png'
JIE_SHU = 'JIE-SHU.png'
JIA_CHENG = 'JIA-CHENG.png'
ZI_DONG = 'ZI-DONG.png'
# 右上角邮件图像
YOU_JIAN = 'MESSAGE.png'
# 战斗开始时候的准备按钮
ZHUN_BEI='ZHUN-BEI.png'
# ---------------御魂部分--------------------------

KAI_SHI_ZHAN_DOU = 'KAI-SHI-ZHAN-DOU.png'
DUI_YOU_JIA_HAO = 'DUI-YOU-JIA-HAO.png'
ZI_DONG_YAO_QING = 'ZI-DONG-YAO-QING.png'
XIE_ZHAN_DUI_WU = 'XIE-ZHAN-DUI-WU.png'
ZI_DONG_JIE_SHOU = 'ZI-DONG-JIE-SHOU.png'
YU_HUN = 'YU-HUN.png'
JIE_SHOU = 'JIE-SHOU.png'

# ---------------探索部分--------------------------
# 继续邀请队友战斗 确定按钮
EXPLORE_QUE_DING='QUE-DING.png'
# 退出探索时候的确认
EXPLORE_QUE_REN='TUI-CHU-TAN-SUO-QUE-REN.png'

# 樱饼
YING_BING = 'YING-BING.png'
# 经验怪身边的buff图像
JING_YAN = 'JING-YAN.png'
# 经验怪头上的战斗按钮
EXPLORE_ZHAN_DOU = 'FIGHT.png'
# 探索中的boss头像上的按钮
EXPLORE_BOSS='BOSS.png'
# 探索中狗粮头像上的'满'字图像
EXPLORE_GOU_LIANG_MAN='GOU-LIANG-MAN.png'
# 探索换狗粮时的全部按钮
EXPLORE_QUAN_BU='QUAN-BU.png'
# 探索中队长的标志
EXPLORE_DUI_ZHANG_LOGO='DUI-ZHANG.png'
# 探索界面中的退出按钮
EXPLORE_QUIT='QUIT.png'
# 探索乘客接受邀请的图片
EXPLORE_JIE_SHOU='TAN-SUO-JIE-SHOU.png'

JIN_RU_ZHAN_DOU='JIN-RU-ZHAN-DOU.png'


def get_img_file_path():
    root_dir = os.path.dirname(os.path.abspath('.')) + '\\Img\\'
    return root_dir

def check_img_path_correct():
    """
    检查图片路径是否正确
    :return:
    """
    logging.info('启动前检查图片路径,检查路径为{}'.format(get_img_file_path()+r'*.png'))
    img_list=glob.glob(get_img_file_path()+'*.png')
    if img_list is None or len(img_list) == 0:
        logging.error('img文件夹路径错误,应与exe文件同路径')
        return False
    else:
        logging.info('img文件夹下图片数量为{}'.format(len(img_list)))
        return True
# print(GetImgFilePath())
