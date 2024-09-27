from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTreeWidgetItem
from qfluentwidgets import ComboBox, ToolButton, PushButton, TreeWidget, LineEdit
from qfluentwidgets import FluentIcon as FIF


class MidHomeWidget(QWidget):
    def __init__(self, db, service, comm):
        super().__init__()
        self.db = db
        self.service = service
        self.comm = comm

        self.m_userId = -1
        self.m_username = None
        self.m_allTasks = []
        self.m_unscheduledTasks = []
        self.m_HaveFinishedTasks = []
        self.m_next7DaysTasks = []
        self.m_afterNextWeekTasks = []

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
        self.stackedWidget_create = QtWidgets.QStackedWidget(self)
        self.stackedWidget_create.setObjectName("stackedWidget_create")
        self.widget_create_1 = QWidget()
        self.hSpacer = QtWidgets.QSpacerItem(50, 5, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.btn_create = PushButton('+ 点击新建待办')
        self.btn_create.setObjectName("btn_create")
        self.horizontalLayout.addWidget(self.btn_create)
        self.hSpacer = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.widget_create_1.setLayout(self.horizontalLayout)
        self.stackedWidget_create.addWidget(self.widget_create_1)
        self.widget_create_2 = QWidget()
        self.horizontalLayout = QHBoxLayout()
        self.hSpacer = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.hSpacer)
        self.lineEdit_create = LineEdit()
        self.lineEdit_create.setObjectName("lineEdit_create")
        self.lineEdit_create.setFixedSize(400, 30)
        self.lineEdit_create.setPlaceholderText('输入后点击回车创建待办')
        self.horizontalLayout.addWidget(self.lineEdit_create)
        self.horizontalLayout.addItem(self.hSpacer)
        self.widget_create_2.setLayout(self.horizontalLayout)
        self.horizontalLayout = QHBoxLayout()
        self.stackedWidget_create.addWidget(self.widget_create_2)
        self.stackedWidget_create.setFixedHeight(50)
        self.horizontalLayout.addWidget(self.stackedWidget_create)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(self.vSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.treeWidget = TreeWidget()
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(False)
        self.treeWidget.setStyleSheet('background-color: rgb(249, 249, 249);\
                                              font: 25 11pt "等线";\
        border-radius:0px;')
        self.hSpacer = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.hSpacer)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.horizontalLayout.addItem(self.hSpacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.addItem(self.vSpacer)

        self.setLayout(self.verticalLayout)
        self.init_connections()

    def init_connections(self):
        self.comm.singleton.connect(self.single_methods)
        self.comm.singleton_list.connect(self.single_methods_params)
        self.btn_create.clicked.connect(lambda: self.stackedWidget_create.setCurrentWidget(self.widget_create_2))
        self.lineEdit_create.returnPressed.connect(self.create_pressed)
        self.refresh_btn.clicked.connect(self.refresh_btn_clicked)
        self.sort_comboBox.currentIndexChanged.connect(self.init_treeWidget_group)
        self.treeWidget.itemPressed.connect(self.itemClicked)

    def create_pressed(self):
        self.stackedWidget_create.setCurrentWidget(self.widget_create_1)

    def single_methods(self, signal):
        if signal == 'BTN_HOME_CLICKED':
            self.comm.singleton.emit('SET_DISABLE_MID_WIDGET')
            self.init_task_list()
            self.init_treeWidget()
            self.comm.singleton.emit('SET_ABLE_MID_WIDGET')
            self.label_home.setText("我的首页")
        elif signal == 'BTN_TODO_CLICKED':
            self.init_task_list()
            self.init_treeWidget_group()
            self.comm.singleton.emit('SET_ABLE_MID_WIDGET')
            self.label_home.setText("我的待办")

    def single_methods_params(self, single, x):
        if single == 'SET_USER_INFO':
            self.m_userId = x[0]
            self.m_username = x[1]

    def init_task_list(self):
        ans = self.service.init_task_list(self.db, self.m_userId)
        self.m_allTasks = ans[0]
        self.m_unscheduledTasks = ans[1]
        self.m_HaveFinishedTasks = ans[2]
        self.m_next7DaysTasks = ans[3]
        self.m_afterNextWeekTasks = ans[4]
        self.comm.singleton_list.emit('SET_TASK_INFO', [ans])

    def init_treeWidget(self):
        self.treeWidget.clear()
        unscheduledRoot = QTreeWidgetItem(self.treeWidget)
        unscheduledRoot.setText(0, " 未安排")

        next7DaysRoot = QTreeWidgetItem(self.treeWidget)
        next7DaysRoot.setText(0, " 未来七天")

        afterNextWeekRoot = QTreeWidgetItem(self.treeWidget)
        afterNextWeekRoot.setText(0, " 以后")

        # 主逻辑
        try:
            # 处理未安排的任务
            for task in self.m_unscheduledTasks:
                self.process_task(task, unscheduledRoot)

            # 获取未来七天的任务
            for task in self.m_next7DaysTasks:
                self.process_task(task, next7DaysRoot)

            # 获取一周后任务
            for task in self.m_afterNextWeekTasks:
                self.process_task(task, afterNextWeekRoot)
        except Exception as e:
            print(f"处理任务时发生错误: {e}")

    def init_treeWidget_group(self):
        self.treeWidget.clear()
        haveFinishedRoot = QTreeWidgetItem(self.treeWidget)
        haveFinishedRoot.setText(0, " 已完成")

        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0, " 我的待办")
        root.setExpanded(True)

        if self.sort_comboBox.currentIndex() == 1:
            # 将任务按到期时间从早到晚排序
            self.m_allTasks.sort(key=lambda x: x.dueDate)

        elif self.sort_comboBox.currentIndex() == 2:
            # 将任务按创建时间从早到晚排序
            self.m_allTasks.sort(key=lambda x: x.m_id)

        elif self.sort_comboBox.currentIndex() == 3:
            # 将任务按优先级从高到低排序
            self.m_allTasks.sort(key=lambda x: x.priority, reverse=True)

        for task in self.m_allTasks:
            taskItem = QTreeWidgetItem()
            taskMes = task.eventName
            groupId = task.groupId
            groupStr = self.checkGroup(groupId)
            taskMes += " 分组:" + groupStr
            priority = task.priority
            priorityStr = self.checkPriority(priority)

            taskMes += " 优先级:" + priorityStr
            taskItem.setText(0, taskMes)
            taskItem.setData(0, QtCore.Qt.ItemDataRole.UserRole, task.m_id)
            if task.dueDate < QDateTime.currentDateTime():
                haveFinishedRoot.addChild(taskItem)
            else:
                root.addChild(taskItem)

    def process_task(self, task, root):
        taskItem = QTreeWidgetItem()
        taskMes = task.eventName
        groupId = task.groupId
        groupStr = self.checkGroup(groupId)
        taskMes += " 分组:" + groupStr
        priority = task.priority
        priorityStr = self.checkPriority(priority)
        taskMes += " 优先级:" + priorityStr
        taskItem.setText(0, taskMes)
        taskItem.setData(0, QtCore.Qt.ItemDataRole.UserRole, task.m_id)
        root.addChild(taskItem)

    def checkGroup(self, groupId):
        if groupId == -1:
            return '我的待办'
        else:
            return self.service.selectGroupNameById(self.db, groupId)

    @staticmethod
    def checkPriority(priority):
        if priority == 0:
            return '无优先级'
        elif priority == 1:
            return '低'
        elif priority == 2:
            return '中'
        else:
            return '高'

    def refresh_btn_clicked(self):
        if self.label_home.text() == "我的首页":
            self.comm.singleton.emit('BTN_HOME_CLICKED')
        elif self.label_home.text() == "我的待办":
            self.comm.singleton.emit('BTN_TODO_CLICKED')

    def itemClicked(self, item, column):
        # 获得item的id
        id_str = item.data(0, QtCore.Qt.ItemDataRole.UserRole)
        task_id = 0 if id_str is None else int(id_str)
        if task_id == 0:
            if self.treeWidget.currentItem().isExpanded():
                self.treeWidget.collapseItem(item)
            else:
                self.treeWidget.expandItem(item)
        else:
            self.comm.singleton_list.emit('SET_RIGHT_WIDGET', [task_id])

