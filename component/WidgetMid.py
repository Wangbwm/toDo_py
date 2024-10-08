from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from component.MidGroup import MidGroupWidget
from component.MidHome import MidHomeWidget


class WidgetMid(QWidget):
    def __init__(self, db, service, comm):
        super().__init__()
        self.db = db
        self.service = service
        self.comm = comm
        # 创建水平布局
        self.hBoxLayout = QHBoxLayout(self)
        self.stackWidget = QtWidgets.QStackedWidget(self)
        self.home_widget = MidHomeWidget(self.db, self.service, self.comm)
        self.group_widget = MidGroupWidget(self.db, self.service, self.comm)
        self.stackWidget.setStyleSheet('background-color: rgb(255, 255, 255);\
                                       border-radius:30px;')
        self.initLayout()
        self.init_connections()

    def initLayout(self):
        self.stackWidget.addWidget(self.home_widget)
        self.stackWidget.addWidget(self.group_widget)
        # self.stackWidget.setCurrentIndex(1)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.setLayout(self.hBoxLayout)

    def init_connections(self):
        self.comm.singleton.connect(self.single_methods)

    def single_methods(self, signal):
        if signal == 'BTN_GROUP_CLICKED':
            self.stackWidget.setCurrentWidget(self.group_widget)
            self.home_widget.sort_comboBox.setCurrentIndex(0)
            self.comm.singleton.emit('SET_DISABLE_RIGHT_WIDGET')
        elif signal == 'BTN_HOME_CLICKED':
            self.stackWidget.setCurrentWidget(self.home_widget)
            self.home_widget.sort_comboBox.setVisible(False)
            self.comm.singleton.emit('SET_DISABLE_RIGHT_WIDGET')
        elif signal == 'BTN_TODO_CLICKED':
            self.stackWidget.setCurrentWidget(self.home_widget)
            self.home_widget.sort_comboBox.setVisible(True)
            self.comm.singleton.emit('SET_DISABLE_RIGHT_WIDGET')




