#! -*- coding:utf-8 -*-
import sys
import os
from backen.app import *
from PySide2.QtCore import QFileInfo
from backen import init_gui

sys.path.append((os.path.dirname(os.path.abspath(os.path.dirname(__file__)))).replace("\\", "/"))


if __name__ == '__main__':
    root = QFileInfo(__file__).absolutePath()
    init_gui(app, port=5000, window_title="江老师的专属工作软件", icon=root + "./front/resource/icon.png")


