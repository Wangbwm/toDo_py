from PyQt5.QtCore import pyqtSignal, QObject


class Communicate(QObject):
    # 自定义信号，带有一个str类型的参数
    singleton = pyqtSignal(str)
    # 自定义信号，带有一个str类型和数组参数
    singleton_list = pyqtSignal(str, list)
