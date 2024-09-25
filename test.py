from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import PushButton, MessageBox


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('test')
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = PushButton('点击按钮')
        self.pushButton.setFixedSize(200, 50)
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.setLayout(self.verticalLayout)

        self.init_connections()

    def init_connections(self):
        self.pushButton.clicked.connect(self.push_btn_clicked)

    def push_btn_clicked(self):
        w = MessageBox('提示', 'hello world', self)
        w.exec_()

