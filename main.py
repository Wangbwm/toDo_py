# coding:utf-8
import sys
from PyQt5.QtCore import Qt, QFile, QIODevice, QTextStream
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel
from qfluentwidgets import (NavigationInterface, NavigationItemPosition, isDarkTheme)
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar

from Communicate import Communicate
from component.MainWindow import MainWindow
from component.Start import StartWidget
from dao.db import DbConnection


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class Window(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.db = DbConnection().db
        self.comm = Communicate()
        self.setTitleBar(StandardTitleBar(self))

        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self, showMenuButton=True)
        self.stackWidget = QStackedWidget(self)

        self.startWidget = StartWidget(self.db, self.comm)
        self.MainWindow = MainWindow(self.db, self.comm)
        self.stackWidget.addWidget(self.startWidget)
        self.stackWidget.addWidget(self.MainWindow)

        self.setStyleSheet("background-color: rgb(220, 220, 220);")

        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()

        self.initWindow()

        self.init_connections()

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, self.titleBar.height(), 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

    def initNavigation(self):
        self.addSubInterface(self.startWidget, FIF.HOME, 'Start')
        # self.addSubInterface(self.MainWindow, FIF.QUICK_NOTE, 'Note')
        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.stackWidget.setCurrentWidget(self.startWidget)

    def initWindow(self):
        self.resize(1200, 700)
        self.setWindowIcon(QIcon('resource/logo.png'))
        self.setWindowTitle('toDo')
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        # NOTE: set the minimum window width that allows the navigation panel to be expanded
        # self.navigationInterface.setMinimumExpandWidth(900)
        # self.navigationInterface.expand(useAni=False)

        self.setQss()

    def init_connections(self):
        self.comm.singleton.connect(self.addTaskWidget)

    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP, parent=None):
        """ add sub interface """
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text,
            parentRouteKey=parent.objectName() if parent else None
        )

    def setQss(self):
        color = 'dark' if isDarkTheme() else 'light'
        file = f':/{color}/demo.qss'
        stream = QFile(file)
        stream.open(QIODevice.ReadOnly)
        qss_style = QTextStream(stream).readAll()
        self.setStyleSheet(qss_style)

    def switchTo(self, widget):
        self.stackWidget.setCurrentWidget(widget)

    def onCurrentInterfaceChanged(self, index):
        pass

    def switchNext(self):
        pass

    def addTaskWidget(self, single):
        if single == 'ADD_TASK_WIDGET':
            self.addSubInterface(self.MainWindow, FIF.QUICK_NOTE, 'Note')
            self.switchTo(self.MainWindow)
            self.navigationInterface.removeWidget(self.startWidget.objectName())
            self.showMaximized()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
