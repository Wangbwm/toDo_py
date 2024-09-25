from PyQt5.QtCore import QDateTime


class KTask:
    def __init__(self, eventId=None, userId=None, groupId=None,
                 eventName='', isArranged=False, priority=0,
                 dueDate=None, isRepeated=False, remindTime=None,
                 description='', location='', note=''):

        # 如果提供了所有参数，则使用这些参数初始化对象
        if eventId is not None and userId is not None and dueDate is not None and remindTime is not None:
            self.m_id = eventId
            self.userId = userId
            self.groupId = groupId
            self.eventName = eventName
            self.arranged = isArranged
            self.priority = priority
            self.dueDate = dueDate
            self.m_repeated = isRepeated
            self.remindTime = remindTime
            self.description = description
            self.location = location
            self.note = note
        else:
            # 否则使用默认值初始化对象
            self.m_id = -1
            self.userId = -1
            self.groupId = -1
            self.eventName = ''
            self.arranged = False
            self.priority = 0
            self.dueDate = QDateTime()
            self.m_repeated = False
            self.remindTime = QDateTime()
            self.description = ''
            self.location = ''
            self.note = ''
