from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import PushButton, LineEdit, PasswordLineEdit, MessageBox

from Communicate import Communicate
from service.StartService import StartService


class LoginWidget(QWidget):
    def __init__(self, db, comm):
        super().__init__()
        self.setObjectName('login')
        self.db = db
        self.service = StartService()
        self.comm = comm

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
        self.label.setText('欢迎进入-待办-')
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
        self.hSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed)
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
        self.hSpacer = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.pwd_lineEdit)
        self.hSpacer = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        # 登录按钮
        self.horizontalLayout = QHBoxLayout()
        self.btn_login = PushButton('登录')
        self.btn_login.setFixedSize(150, 30)
        self.hSpacer = QtWidgets.QSpacerItem(270, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.btn_login)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.switch_register = PushButton('注册账号')
        self.switch_register.setFixedSize(100, 30)
        self.hSpacer = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.switch_register)
        self.hSpacer = QtWidgets.QSpacerItem(270, 20, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vSpacer = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        self.setLayout(self.verticalLayout)
        self.init_connections()

    def init_connections(self):
        self.btn_login.clicked.connect(self.login)
        self.pwd_lineEdit.returnPressed.connect(self.login)

    def login(self):
        ans = self.service.login(self.db, self.user_lineEdit.text(), self.pwd_lineEdit.text())
        if ans[0]:
            w = MessageBox("欢迎", ans[1], self)
            w.exec()
            self.comm.singleton.emit('ADD_TASK_WIDGET')
            user_id = self.service.selectUserID(self.db, self.user_lineEdit.text())
            self.comm.singleton_list.emit('SET_USER_INFO', [user_id, self.user_lineEdit.text()])
            self.comm.singleton.emit('BTN_HOME_CLICKED')
        else:
            w = MessageBox("错误", ans[1], self)
            w.exec()
