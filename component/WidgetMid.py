from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from component.MidGroup import MidGroupWidget
from component.MidHome import MidHomeWidget


class WidgetMid(QWidget):
    def __init__(self):
        super().__init__()
        # 创建水平布局
        self.hBoxLayout = QHBoxLayout(self)
        self.stackWidget = QtWidgets.QStackedWidget(self)
        self.home_widget = MidHomeWidget()
        self.group_widget = MidGroupWidget()
        self.stackWidget.setStyleSheet('background-color: rgb(255, 255, 255);\
                                       border-radius:30px;')
        self.initLayout()

    def initLayout(self):
        self.stackWidget.addWidget(self.home_widget)
        self.stackWidget.addWidget(self.group_widget)
        # self.stackWidget.setCurrentIndex(1)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.setLayout(self.hBoxLayout)


