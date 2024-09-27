from PyQt5 import QtSql
from PyQt5.QtCore import QDateTime

from pojo.ktask import KTask


class TaskDao:
    def __init__(self):
        self.db = None

    # 定义一个函数来处理单个任务的数据
    @staticmethod
    def process_task_row(query):
        id = int(query.value('id'))
        group_id = query.value('group_id')
        groupId = -1 if group_id == '' else int(group_id)
        userId = -1
        eventName = query.value('event_name')
        isArranged = bool(query.value('is_arranged'))
        priority = 0 if query.value('priority') == '' else int(query.value('priority'))
        pdueDate = query.value('due_date')
        dueDate = QDateTime() if pdueDate is None else QDateTime.fromString(str(pdueDate), "yyyy-MM-dd hh:mm:ss")
        isRepeated = bool(query.value('is_repeated'))
        premindTime = query.value('remind_time')
        remindtime = QDateTime() if premindTime is None else QDateTime.fromString(str(premindTime), "yyyy-MM-dd hh:mm:ss")
        description = query.value('description')
        location = query.value('location')
        note = query.value('note')

        return KTask(id, userId, groupId, eventName, isArranged, priority, dueDate, isRepeated, remindtime, description,
                     location, note)


    def execute_task_query(self, query):
        query_list = []
        if not query.exec_():
            # 如果查询失败，打印错误信息并返回False
            print("Query failed:", query.lastError().text())
            return None
        while query.next():
            task = self.process_task_row(query)
            query_list.append(task)
        return query_list

    def selectGroupListByUserId(self, db, user_id):
        # 准备一个SQL查询对象，用于执行数据库查询
        query = QtSql.QSqlQuery(db)
        query.prepare("SELECT group_id FROM todo_user_group WHERE user_id = ?")
        query.bindValue(0, user_id)
        if not query.exec_():
            # 如果查询失败，打印错误信息并返回False
            print("Query failed:", query.lastError().text())
            return None
        group_list = []
        while query.next():
            group_list.append(query.value(0))
        return group_list

    def selectGroupNameById(self, db, group_id):
        # 准备一个SQL查询对象，用于执行数据库查询
        query = QtSql.QSqlQuery(db)
        query.prepare("SELECT group_name FROM todo_groups WHERE id = ?")
        query.bindValue(0, group_id)
        if not query.exec_():
            # 如果查询失败，打印错误信息并返回False
            print("Query failed:", query.lastError().text())
            return None
        if query.next():
            return query.value(0)
        return None

    def selectAllTaskByUserId(self, db, user_id):
        # 准备一个SQL查询对象，用于执行数据库查询
        query = QtSql.QSqlQuery(db)
        query.prepare("SELECT * FROM todo_list WHERE user_id = ?")
        query.bindValue(0, user_id)
        return self.execute_task_query(query)

    def selectAllTasksGroup(self, db, group_id):
        # 准备一个SQL查询对象，用于执行数据库查询
        query = QtSql.QSqlQuery(db)
        query.prepare("SELECT * FROM todo_list WHERE group_id = ?")
        query.bindValue(0, group_id)
        return self.execute_task_query(query)


