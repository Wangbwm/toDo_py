from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import PushButton, ToolButton, TitleLabel
from qfluentwidgets import FluentIcon as FIF


class WidgetLeft(QWidget):
    def __init__(self, comm):
        super().__init__()
        self.comm = comm
        # 创建垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 创建水平子布局
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_home = PushButton(FIF.HOME_FILL, "我的首页", self)
        self.btn_home.setObjectName("btn_home")
        self.btn_home.setIconSize(QtCore.QSize(16, 16))
        self.verticalLayout.addWidget(self.btn_home)

        self.btn_todo = PushButton(FIF.BOOK_SHELF, "我的待办", self)
        self.btn_todo.setObjectName("btn_todo")
        self.btn_todo.setIconSize(QtCore.QSize(16, 16))
        self.verticalLayout.addWidget(self.btn_todo)

        self.btn_group = PushButton(FIF.PEOPLE, "添加分组", self)
        self.btn_group.setObjectName("btn_group")
        self.btn_group.setIconSize(QtCore.QSize(16, 16))
        self.verticalLayout.addWidget(self.btn_group)

        # 创建树形控件
        self.tree_widget_left = QtWidgets.QTreeWidget()
        self.tree_widget_left.setObjectName("tree_widget_left")
        self.tree_widget_left.setStyleSheet('border-radius:0px;\
border:none;\
font: 25 10pt "等线";')
        self.verticalLayout.addWidget(self.tree_widget_left)

        self.user_head = ToolButton(FIF.ROBOT)
        self.user_head.setObjectName("user_head")
        self.user_head.setIconSize(QtCore.QSize(60, 60))
        self.user_head.setDisabled(False)
        self.user_head.setStyleSheet('border: none;')
        self.hSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.user_head)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.label_user = TitleLabel('UserName')
        self.label_user.setStyleSheet('border: none;\
font: 25 13pt "等线";')
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.label_user)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.label_wel = TitleLabel('Welcome!')
        self.label_wel.setStyleSheet('border: none;\
        font: 25 13pt "等线";')
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.label_wel)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.setLayout(self.verticalLayout)

        self.init_connections()

    def init_connections(self):
        self.btn_home.clicked.connect(lambda: self.comm.singleton.emit('BTN_HOME_CLICKED'))
        self.btn_todo.clicked.connect(lambda: self.comm.singleton.emit('BTN_TODO_CLICKED'))
        self.btn_group.clicked.connect(lambda: self.comm.singleton.emit('BTN_GROUP_CLICKED'))


