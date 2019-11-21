# 存储所有图片的名称,函数调用时手动添加相对路径
import os

XUAN_SHANG = 'XUAN-SHANG.png'
KAI_SHI_ZHAN_DOU = 'KAI-SHI-ZHAN-DOU.png'
JIN_BI = 'JIN-BI.png'
JIE_SHU = 'JIE-SHU.png'
JIA_CHENG = 'JIA-CHENG.png'
DUI_YOU_JIA_HAO = 'DUI-YOU-JIA-HAO.png'
ZI_DONG_YAO_QING = 'ZI-DONG-YAO-QING.png'
XIE_ZHAN_DUI_WU = 'XIE-ZHAN-DUI-WU.png'
ZI_DONG_JIE_SHOU = 'ZI-DONG-JIE-SHOU.png'
YU_HUN = 'YU-HUN.png'
JIE_SHOU='JIE-SHOU.png'


def GetImgFilePath():
    root_dir = os.path.dirname(os.path.abspath('.')) + r'CommonUtil/'
    return root_dir

# print(GetImgFilePath())
