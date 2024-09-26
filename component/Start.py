from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from component.Login import LoginWidget
from component.Register import RegisterWidget


class StartWidget(QWidget):
    def __init__(self, db, comm):
        super().__init__()
        self.db = db
        self.comm = comm
        self.setObjectName('Start')
        # 设置字体
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        # 创建水平布局
        self.hBoxLayout = QHBoxLayout(self)

        # 创建堆叠窗口
        self.stackWidget = QtWidgets.QStackedWidget()
        self.stackWidget.setObjectName("stackWidget")

        # 创建子界面
        self.loginWidget = LoginWidget(self.db, self.comm)
        self.registerWidget = RegisterWidget(self.db)


        # 将子界面添加到堆叠窗口
        self.stackWidget.addWidget(self.loginWidget)
        self.stackWidget.addWidget(self.registerWidget)
        # 背景设置为白色和圆角
        self.setStyleSheet("background-color: rgb(255, 255, 255);\
        border:2px solid rgb(255, 255, 255);\
        border-radius:30px;")
        # 将堆叠窗口添加到主布局
        self.hBoxLayout.addWidget(self.stackWidget)

        self.hBoxLayout.setContentsMargins(220, 60, 220, 60)
        # 设置主窗口布局
        self.setLayout(self.hBoxLayout)
        self.init_connections()

    def init_connections(self):
        self.loginWidget.switch_register.clicked.connect(self.switch_register_clicked)
        self.registerWidget.switch_login.clicked.connect(self.switch_login_clicked)

    def switch_register_clicked(self):
        self.stackWidget.setCurrentIndex(1)

    def switch_login_clicked(self):
        self.stackWidget.setCurrentIndex(0)
