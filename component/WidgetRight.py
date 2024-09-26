from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from qfluentwidgets import RadioButton, LineEdit, ComboBox, PushButton, ZhDatePicker, CalendarPicker, TimePicker
from qfluentwidgets import FluentIcon as FIF

class WidgetRight(QWidget):
    def __init__(self):
        super().__init__()
        # 创建垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 创建水平子布局
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_home = RadioButton()
        self.hSpacer = QtWidgets.QSpacerItem(70, 10, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.checkBox_home)
        self.lineEdit_name = LineEdit()
        self.lineEdit_name.setFixedSize(120, 30)
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.hSpacer = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.hSpacer = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.comboBox_priority = ComboBox()
        # 添加选项
        items = ['优先级 无', '优先级 低', '优先级 中', '优先级 高']
        self.comboBox_priority.addItems(items)
        self.comboBox_priority.setObjectName("comboBox_priority")
        self.comboBox_priority.setStyleSheet('border:2px solid rgb(215,217,222);\
        color: rgb(54,66,90);\
        border-radius:0px;')
        self.comboBox_priority.setFixedSize(120, 30)
        self.hSpacer = QtWidgets.QSpacerItem(70, 10, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.comboBox_priority)
        self.hSpacer = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget_dueDate = QtWidgets.QStackedWidget(self)
        self.stackedWidget_dueDate.setObjectName("stackedWidget_dueDate")
        self.widget_dueDate_1 = QWidget()
        self.widget_dueDate_1.setObjectName("widget_dueDate_1")
        self.btn_dueDate = PushButton('设置到期')
        self.btn_dueDate.setIcon(FIF.CALENDAR)
        self.btn_dueDate.setFixedSize(283, 30)
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.btn_dueDate)
        self.widget_dueDate_1.setLayout(horizontalLayout)
        self.stackedWidget_dueDate.addWidget(self.widget_dueDate_1)

        self.widget_dueDate_2 = QWidget()
        self.widget_dueDate_2.setObjectName("widget_dueDate_2")
        self.dateTime_day_pick = CalendarPicker()
        # self.dateTime_day_pick.setFixedSize(30, 30)
        self.dateTime_hms_pick = TimePicker()
        # self.dateTime_hms_pick.setFixedSize(10, 10)

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.dateTime_day_pick)
        horizontalLayout.addWidget(self.dateTime_hms_pick)
        self.widget_dueDate_2.setLayout(horizontalLayout)
        self.stackedWidget_dueDate.addWidget(self.widget_dueDate_2)
        self.verticalLayout.addWidget(self.stackedWidget_dueDate)
        # self.stackedWidget_dueDate.setCurrentIndex(1)

        self.stackedWidget_remind = QtWidgets.QStackedWidget(self)
        self.stackedWidget_remind.setObjectName("stackedWidget_remind")
        self.widget_remind_1 = QWidget()
        self.widget_remind_1.setObjectName("widget_remind_1")
        self.btn_remind = PushButton('设置提醒')
        self.btn_remind.setIcon(FIF.RINGER)
        self.btn_remind.setFixedSize(283, 30)
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.btn_remind)
        self.widget_remind_1.setLayout(horizontalLayout)
        self.stackedWidget_remind.addWidget(self.widget_remind_1)

        self.widget_remind_2 = QWidget()
        self.widget_remind_2.setObjectName("widget_remind_2")
        self.checkBox_repeat = RadioButton()
        self.remind_day_pick = CalendarPicker()
        self.remind_hms_pick = TimePicker()
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.checkBox_repeat)
        horizontalLayout.addWidget(self.remind_day_pick)
        horizontalLayout.addWidget(self.remind_hms_pick)
        self.widget_remind_2.setLayout(horizontalLayout)
        self.stackedWidget_remind.addWidget(self.widget_remind_2)
        # self.stackedWidget_remind.setCurrentIndex(1)
        self.verticalLayout.addWidget(self.stackedWidget_remind)

        horizontalLayout = QHBoxLayout()
        self.btn_des = PushButton('添加描述')
        self.btn_des.setIcon(FIF.ALIGNMENT)
        self.btn_des.setFixedSize(283, 30)
        horizontalLayout.addWidget(self.btn_des)
        self.verticalLayout.addLayout(horizontalLayout)

        horizontalLayout = QHBoxLayout()
        self.btn_loc = PushButton('添加地点')
        self.btn_loc.setIcon(FIF.AIRPLANE)
        self.btn_loc.setFixedSize(283, 30)
        horizontalLayout.addWidget(self.btn_loc)
        self.verticalLayout.addLayout(horizontalLayout)

        horizontalLayout = QHBoxLayout()
        self.btn_note = PushButton('添加备注')
        self.btn_note.setIcon(FIF.QUICK_NOTE)
        self.btn_note.setFixedSize(283, 30)
        horizontalLayout.addWidget(self.btn_note)
        self.verticalLayout.addLayout(horizontalLayout)

        # self.vSpacer = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Preferred)
        # self.verticalLayout.addItem(self.vSpacer)

        self.stackedWidget_add = QtWidgets.QStackedWidget(self)
        self.stackedWidget_add.setObjectName("stackedWidget_add")
        self.widget_add_1 = QWidget()
        self.widget_add_1.setObjectName("widget_add_1")
        horizontalLayout = QHBoxLayout()
        self.treeWidget_add = QtWidgets.QTreeWidget(self)
        horizontalLayout.addWidget(self.treeWidget_add)
        self.widget_add_1.setLayout(horizontalLayout)
        self.stackedWidget_add.addWidget(self.widget_add_1)

        self.widget_add_2 = QWidget()
        self.widget_add_2.setObjectName("widget_add_2")
        verticalLayout = QVBoxLayout()
        self.btn_add_close = PushButton('关闭')
        verticalLayout.addWidget(self.btn_add_close)
        self.testBrowser_add_close = QtWidgets.QTextBrowser(self)
        self.testBrowser_add_close.setObjectName("testBrowser_add_close")
        self.testBrowser_add_close.setStyleSheet('border:2px solid rgb(246,111,111);\
border-radius:0px;\
font: 25 15pt "等线";')
        verticalLayout.addWidget(self.testBrowser_add_close)
        self.widget_add_2.setLayout(verticalLayout)
        self.stackedWidget_add.addWidget(self.widget_add_2)

        self.widget_add_3 = QWidget()
        self.widget_add_3.setObjectName("widget_add_3")
        verticalLayout = QVBoxLayout()
        self.btn_add_ok = PushButton('确定')
        verticalLayout.addWidget(self.btn_add_ok)
        self.testBrowser_add_ok = QtWidgets.QTextBrowser(self)
        self.testBrowser_add_ok.setObjectName("testBrowser_add_ok")
        self.testBrowser_add_ok.setStyleSheet('border:2px solid rgb(246,111,111);\
        border-radius:0px;\
        font: 25 15pt "等线";')
        verticalLayout.addWidget(self.testBrowser_add_ok)
        self.widget_add_3.setLayout(verticalLayout)
        self.stackedWidget_add.addWidget(self.widget_add_3)
        self.stackedWidget_add.setFixedSize(300, 400)
        horizontalLayout = QHBoxLayout()
        self.hSpacer = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding)
        horizontalLayout.addItem(self.hSpacer)
        horizontalLayout.addWidget(self.stackedWidget_add)
        horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(horizontalLayout)



        self.setLayout(self.verticalLayout)
