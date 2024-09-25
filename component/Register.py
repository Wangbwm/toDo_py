from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import LineEdit, PasswordLineEdit, PushButton, MessageBox

from service.StartService import StartService


class RegisterWidget(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setObjectName('register')
        self.db = db
        self.service = StartService()

        # 设置字体
        font = QtGui.QFont()
        font.setFamily('等线')
        font.setPointSize(15)
        font.setBold(True)
        # 创建垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 创建水平子布局
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.vSpacer = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        # 创建标题Label
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label_title")
        self.label.setText('欢迎注册')
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 用户名行
        self.horizontalLayout = QHBoxLayout()
        self.label_user = QtWidgets.QLabel(self)
        self.label_user.setObjectName("label_user")
        self.label_user.setText('用户名：')
        self.user_lineEdit = LineEdit()
        # 设置提示文本
        self.user_lineEdit.setPlaceholderText('请输入用户名')
        self.user_lineEdit.setFixedSize(300, 30)
        self.hSpacer = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.label_user)
        self.hSpacer = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.user_lineEdit)
        self.hSpacer = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        # 密码行
        self.horizontalLayout = QHBoxLayout()
        self.label_pwd = QtWidgets.QLabel(self)
        self.label_pwd.setObjectName("label_pwd")
        self.label_pwd.setText('密码：')
        self.pwd_lineEdit = PasswordLineEdit()
        self.pwd_lineEdit.setPlaceholderText('请输入密码')
        self.pwd_lineEdit.setFixedSize(300, 30)
        self.hSpacer = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.label_pwd)
        self.hSpacer = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.pwd_lineEdit)
        self.hSpacer = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        # 确认密码
        self.horizontalLayout = QHBoxLayout()
        self.label_pwd_2 = QtWidgets.QLabel(self)
        self.label_pwd_2.setObjectName("label_pwd_2")
        self.label_pwd_2.setText('重复密码：')
        self.pwd_lineEdit_2 = PasswordLineEdit()
        self.pwd_lineEdit_2.setPlaceholderText('请重复密码')
        self.pwd_lineEdit_2.setFixedSize(300, 30)
        self.hSpacer = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.label_pwd_2)
        self.hSpacer = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.pwd_lineEdit_2)
        self.hSpacer = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        # 注册按钮
        self.horizontalLayout = QHBoxLayout()
        self.btn_register = PushButton('注册')
        self.btn_register.setFixedSize(150, 30)
        self.hSpacer = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.btn_register)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.switch_login = PushButton('返回登录')
        self.switch_login.setFixedSize(100, 30)
        self.hSpacer = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.switch_login)
        self.hSpacer = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vSpacer = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        self.setLayout(self.verticalLayout)
        self.init_connections()

    def init_connections(self):
        self.btn_register.clicked.connect(self.register)
        self.pwd_lineEdit_2.returnPressed.connect(self.register)

    def register(self):
        ans = self.service.register(self.db, self.user_lineEdit.text(),
                                    self.pwd_lineEdit.text(), self.pwd_lineEdit_2.text())
        if ans[0]:
            w = MessageBox('消息提示', ans[1], self)
            w.exec()
        else:
            w = MessageBox('错误', ans[1], self)
            w.exec()



