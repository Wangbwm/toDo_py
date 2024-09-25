from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from component.WidgetLeft import WidgetLeft
from component.WidgetMid import WidgetMid
from component.WidgetRight import WidgetRight


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('MainWindow')
        # 创建水平布局
        self.hBoxLayout = QHBoxLayout(self)
        self.widget_left = WidgetLeft()
        self.widget_mid = WidgetMid()
        self.widget_right = WidgetRight()
        self.resize(1200, 700)

        self.initLayout()

    def initLayout(self):
        self.hBoxLayout.addWidget(self.widget_left)
        self.hBoxLayout.addWidget(self.widget_mid)
        self.hBoxLayout.addWidget(self.widget_right)
        self.setLayout(self.hBoxLayout)

