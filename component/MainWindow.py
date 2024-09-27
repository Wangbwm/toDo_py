from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from component.WidgetLeft import WidgetLeft
from component.WidgetMid import WidgetMid
from component.WidgetRight import WidgetRight
from service.TaskService import TaskService


class MainWindow(QWidget):
    def __init__(self, db, comm):
        super().__init__()
        self.db = db
        self.comm = comm
        self.service = TaskService()
        self.setObjectName('MainWindow')
        # 创建水平布局
        self.hBoxLayout = QHBoxLayout(self)
        self.widget_left = WidgetLeft(self.db, self.service, self.comm)
        self.widget_mid = WidgetMid(self.comm)
        self.widget_right = WidgetRight(self.comm)

        self.initLayout()
        self.init_connections()

    def initLayout(self):
        self.hBoxLayout.addWidget(self.widget_left)
        self.hBoxLayout.addWidget(self.widget_mid)
        self.hBoxLayout.addWidget(self.widget_right)
        self.setLayout(self.hBoxLayout)

    def init_connections(self):
        self.comm.singleton.connect(self.single_methods)

    def single_methods(self, signal):
        if signal == 'SET_DISABLE_RIGHT_WIDGET':
            self.widget_right.setDisabled(True)

