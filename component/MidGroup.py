from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import PushButton, ComboBox, LineEdit, TreeWidget
from qfluentwidgets import FluentIcon as FIF


class MidGroupWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 创建垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 创建水平子布局
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.vSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.label_home = QtWidgets.QLabel("我的分组")
        self.label_home.setObjectName("label_home")
        self.label_home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home.setStyleSheet('border:none;\
        font: 25 12pt "等线";')
        self.horizontalLayout.addWidget(self.label_home)
        self.hSpacer = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.btn_change_name = PushButton('分组重命名')
        self.btn_change_name.setIcon(FIF.LABEL)
        self.btn_change_name.setObjectName("btn_change_name")
        self.horizontalLayout.addWidget(self.btn_change_name)
        self.btn_delete_group = PushButton('删除分组')
        self.btn_delete_group.setIcon(FIF.DELETE)
        self.btn_delete_group.setObjectName("btn_delete_group")
        self.horizontalLayout.addWidget(self.btn_delete_group)
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.sort_comboBox = ComboBox()
        # 添加选项
        items = ['默认排序', '按到期时间排序', '按创建时间排序', '按优先级排序']
        self.sort_comboBox.addItems(items)
        self.sort_comboBox.setObjectName("sort_comboBox")
        self.sort_comboBox.setStyleSheet('border:2px solid rgb(215,217,222);\
        color: rgb(54,66,90);\
        border-radius:0px;')
        self.sort_comboBox.setFixedSize(200, 30)
        self.horizontalLayout.addWidget(self.sort_comboBox)
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.refresh_btn = PushButton('刷新')
        self.refresh_btn.setIcon(FIF.SYNC)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout.addWidget(self.refresh_btn)
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.stackWidget_create_group = QtWidgets.QStackedWidget(self)
        self.stackWidget_create_group.setObjectName("stackWidget_create_group")
        self.stackWidget_create_group.setFixedHeight(50)
        self.widget_create_group_1 = QWidget()
        self.widget_create_group_1.setObjectName("widget_create_group_1")
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.btn_create_group = PushButton('+  点击新建分组')
        self.btn_create_group.setObjectName("btn_create_group")
        self.btn_create_group.setFixedSize(200, 30)
        self.horizontalLayout.addWidget(self.btn_create_group)
        self.hSpacer = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.widget_create_group_1.setLayout(self.horizontalLayout)
        self.stackWidget_create_group.addWidget(self.widget_create_group_1)

        self.widget_create_group_2 = QWidget()
        self.horizontalLayout = QHBoxLayout()
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.lineEdit_create_group = LineEdit()
        self.lineEdit_create_group.setObjectName("lineEdit_create_group")
        self.lineEdit_create_group.setPlaceholderText('输入后点击回车创建分组')
        self.lineEdit_create_group.setFixedSize(400, 30)
        self.horizontalLayout.addWidget(self.lineEdit_create_group)
        self.horizontalLayout.addItem(self.hSpacer)
        self.widget_create_group_2.setLayout(self.horizontalLayout)
        self.stackWidget_create_group.addWidget(self.widget_create_group_2)
        self.verticalLayout.addWidget(self.stackWidget_create_group)

        self.horizontalLayout = QHBoxLayout()
        self.stackWidget_invite = QtWidgets.QStackedWidget(self)
        self.stackWidget_invite.setObjectName("stackWidget_invite")
        self.stackWidget_invite.setFixedHeight(50)
        self.widget_invite_1 = QWidget()
        self.widget_invite_1.setObjectName("widget_invite_1")
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.btn_invite = PushButton('+  点击发送邀请')
        self.btn_invite.setObjectName("btn_invite")
        self.btn_invite.setFixedSize(200, 30)
        self.horizontalLayout.addWidget(self.btn_invite)
        self.hSpacer = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.widget_invite_1.setLayout(self.horizontalLayout)
        self.stackWidget_invite.addWidget(self.widget_invite_1)

        self.widget_invite_2 = QWidget()
        self.horizontalLayout = QHBoxLayout()
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.lineEdit_invite = LineEdit()
        self.lineEdit_invite.setObjectName("lineEdit_invite")
        self.lineEdit_invite.setFixedSize(400, 30)
        self.lineEdit_invite.setPlaceholderText('输入后点击回车发送邀请')
        self.horizontalLayout.addWidget(self.lineEdit_invite)
        self.horizontalLayout.addItem(self.hSpacer)
        self.widget_invite_2.setLayout(self.horizontalLayout)
        self.stackWidget_invite.addWidget(self.widget_invite_2)
        self.verticalLayout.addWidget(self.stackWidget_invite)

        self.horizontalLayout = QHBoxLayout()
        self.stackWidget_create_task = QtWidgets.QStackedWidget(self)
        self.stackWidget_create_task.setObjectName("stackWidget_create_task")
        self.stackWidget_create_task.setFixedHeight(50)
        self.widget_create_task_1 = QWidget()
        self.widget_create_task_1.setObjectName("widget_create_task_1")
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.btn_create_task = PushButton('+  点击新建待办')
        self.btn_create_task.setObjectName("btn_create_task")
        self.btn_create_task.setFixedSize(200, 30)
        self.horizontalLayout.addWidget(self.btn_create_task)
        self.hSpacer = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.widget_create_task_1.setLayout(self.horizontalLayout)
        self.stackWidget_create_task.addWidget(self.widget_create_task_1)

        self.widget_create_task_2 = QWidget()
        self.horizontalLayout = QHBoxLayout()
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.lineEdit_create_task = LineEdit()
        self.lineEdit_create_task.setObjectName("lineEdit_create_task")
        self.lineEdit_create_task.setPlaceholderText('输入后点击回车创建待办')
        self.lineEdit_create_task.setFixedSize(400, 30)
        self.horizontalLayout.addWidget(self.lineEdit_create_task)
        self.horizontalLayout.addItem(self.hSpacer)
        self.widget_create_task_2.setLayout(self.horizontalLayout)
        self.stackWidget_create_task.addWidget(self.widget_create_task_2)
        self.verticalLayout.addWidget(self.stackWidget_create_task)

        self.stackWidget_group = QtWidgets.QStackedWidget(self)
        self.stackWidget_group.setObjectName("stackWidget_group")
        self.widget_group_1 = QWidget()
        self.widget_group_1.setObjectName("widget_group_1")
        self.treeWidget_group_1 = TreeWidget()
        self.treeWidget_group_1.setObjectName("treeWidget_group_1")
        self.treeWidget_group_1.setStyleSheet('background-color: rgb(249, 249, 249);\
                                              font: 25 11pt "等线";')
        self.treeWidget_group_1.setFixedWidth(600)
        self.treeWidget_group_1.header().setVisible(False)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.addWidget(self.treeWidget_group_1)
        self.widget_group_1.setLayout(self.horizontalLayout)
        self.stackWidget_group.addWidget(self.widget_group_1)

        self.widget_group_2 = QWidget()
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet('border:2px solid rgb(16,138,220);\
font: 25 15pt "等线";')
        self.textBrowser.setFixedSize(600, 300)
        self.vSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.addWidget(self.textBrowser)
        verticalLayout.addItem(self.vSpacer)
        self.btn_accepted = PushButton('接受')
        self.btn_accepted.setIcon(FIF.ACCEPT)
        self.btn_refuse = PushButton('拒绝')
        self.btn_refuse.setIcon(FIF.CLOSE)
        verticalLayout.addWidget(self.btn_accepted)
        verticalLayout.addWidget(self.btn_refuse)
        self.widget_group_2.setLayout(verticalLayout)
        self.stackWidget_group.addWidget(self.widget_group_2)

        # self.stackWidget_group.setCurrentIndex(0)
        self.horizontalLayout = QHBoxLayout()
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.stackWidget_group)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.setLayout(self.verticalLayout)
        self.init_connections()

    def init_connections(self):
        self.btn_create_group.clicked.connect(
            lambda: self.stackWidget_create_group.setCurrentWidget(self.widget_create_group_2)
        )
        self.btn_invite.clicked.connect(
            lambda: self.stackWidget_invite.setCurrentWidget(self.widget_invite_2)
        )
        self.btn_create_task.clicked.connect(
            lambda: self.stackWidget_create_task.setCurrentWidget(self.widget_create_task_2)
        )
        self.lineEdit_create_group.returnPressed.connect(self.create_group_pressed)
        self.lineEdit_invite.returnPressed.connect(self.invite_pressed)
        self.lineEdit_create_task.returnPressed.connect(self.create_task_pressed)

    def create_group_pressed(self):
        self.stackWidget_create_group.setCurrentWidget(self.widget_create_group_1)

    def invite_pressed(self):
        self.stackWidget_invite.setCurrentWidget(self.widget_invite_1)

    def create_task_pressed(self):
        self.stackWidget_create_task.setCurrentWidget(self.widget_create_task_1)


