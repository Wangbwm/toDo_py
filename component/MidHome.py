from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import ComboBox, ToolButton, PushButton, TreeWidget
from qfluentwidgets import FluentIcon as FIF


class MidHomeWidget(QWidget):
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
        self.label_home = QtWidgets.QLabel("我的首页")
        self.label_home.setObjectName("label_home")
        self.label_home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home.setStyleSheet('border:none;\
font: 25 12pt "等线";')
        self.horizontalLayout.addWidget(self.label_home)

        self.hSpacer = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Preferred)
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
        self.refresh_btn = PushButton('刷新')
        self.refresh_btn.setIcon(FIF.SYNC)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout.addWidget(self.refresh_btn)
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.hSpacer = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.btn_create = PushButton('+ 点击新建待办')
        self.btn_create.setObjectName("btn_create")
        self.horizontalLayout.addWidget(self.btn_create)
        self.hSpacer = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.treeWidget = TreeWidget()
        self.treeWidget.setObjectName("treeWidget")
        self.hSpacer = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.addItem(self.vSpacer)

        self.setLayout(self.verticalLayout)
