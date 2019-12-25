# import pytest
import win32gui


from ImageProcessModule.GameControl import GameControl
from YuHunModule.State import State


def test_window_full_shot():
    hwnd = 0x0004084E
    game_control=GameControl(hwnd,State())
    game_control.window_full_shot('test_img.png')



