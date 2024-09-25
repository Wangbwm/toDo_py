from PyQt5 import QtSql
from PyQt5.QtCore import QDateTime

from pojo.ktask import KTask


class StartDao:
    def __init__(self):
        self.db = None

    def login_dao(self, db, username, password):
        """
        在数据库中验证用户名和密码。

        参数:
        - db: 数据库连接对象。
        - username: 用户名字符串。
        - password: 密码字符串。

        返回:
        - 如果登录成功，返回True。
        - 如果查询失败或登录凭据无效，返回False。
        """
        # 初始化SQL查询对象，传入数据库连接
        query = QtSql.QSqlQuery(db)

        # 使用问号占位符，并通过bindValue绑定变量值
        # 这样做可以防止SQL注入攻击
        query.prepare("SELECT id FROM UserAccount WHERE username = ? AND password = ?;")
        query.bindValue(0, username)
        query.bindValue(1, password)

        # 执行查询
        if not query.exec_():
            # 处理查询失败的情况
            print("Query failed:", query.lastError().text())
            return False, '服务器内部错误'

        # 检查是否有结果
        if query.next():
            return True, '登录成功'  # 返回用户的ID
        else:
            return False, '用户名或密码错误'  # 如果没有找到匹配的记录，则返回None

    def register_dao(self, db, username, password):
        """
        在数据库中注册用户。

        该函数尝试在给定的数据库中插入一个新的用户账户。
        它使用参数化查询以防止SQL注入攻击，绑定用户提供的用户名和密码到SQL命令。
        如果插入操作失败，函数会打印错误信息并返回False；否则，返回True。

        参数:
        db - QSqlDatabase的实例，表示到数据库的连接。
        username - 字符串，表示要注册的用户的用户名。
        password - 字符串，表示要注册的用户的密码。

        返回值:
        布尔值，如果用户注册成功则为True，否则为False。
        """
        # 准备一个SQL查询对象，用于执行数据库查询
        query = QtSql.QSqlQuery(db)
        # 检查用户名是否已存在
        query.prepare("SELECT COUNT(*) FROM UserAccount WHERE username = ?;")
        query.bindValue(0, username)
        if not query.exec_():
            # 如果查询失败，打印错误信息并返回False
            print("Query failed:", query.lastError().text())
            return False, '服务器内部错误'
        if query.next() and query.value(0) > 0:
            # 如果用户名已存在，返回False表示注册失败
            return False, '用户名已存在'
        query.finish()
        # 准备插入语句，使用占位符避免SQL注入
        query.prepare("INSERT INTO UserAccount (username, password) VALUES (?, ?);")
        # 将用户名绑定到第一个占位符
        query.bindValue(0, username)
        # 将密码绑定到第二个占位符
        query.bindValue(1, password)
        # 执行插入操作，检查是否成功
        if not query.exec_():
            # 如果操作失败，打印错误信息
            print("Query failed:", query.lastError().text())
            # 返回False表示注册失败
            return False, '服务器内部错误'
        # 如果操作成功，返回T
        return True, '注册成功'

    def selectUserID(db, m_username):
        # 准备一个SQL查询对象，用于执行数据库查询
        query = QtSql.QSqlQuery(db)
        query.prepare("SELECT id FROM UserAccount WHERE username = ?;")
        query.bindValue(0, m_username)
        if not query.exec_():
            # 如果查询失败，打印错误信息并返回False
            print("Query failed:", query.lastError().text())
            return False
        if query.next():
            return query.value(0)
        return False

    def selectGroupListByUserName(db, username):
        # 准备一个SQL查询对象，用于执行数据库查询
        query = QtSql.QSqlQuery(db)
        query.prepare("SELECT groups_list FROM todo_user WHERE username = ?")
        query.bindValue(0, username)
        if not query.exec_():
            # 如果查询失败，打印错误信息并返回False
            print("Query failed:", query.lastError().text())
            return None
        if query.next():
            return query.value(0)

    def selectGroupNameById(db, group_id):
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

    # 定义一个函数来处理单个任务的数据
    def process_task_row(query):
        id = int(query.value('id'))
        group_id = query.value('group_id')
        groupId = -1 if group_id == '' else int(group_id)
        userId = -1
        eventName = query.value('event_name')
        isArranged = bool(query.value('is_arranged'))
        priority = 0 if query.value('priority') == '' else int(query.value('priority'))
        pdueDate = query.value('due_date')
        dueDate = QDateTime() if pdueDate is None else pdueDate
        isRepeated = bool(query.value('is_repeated'))
        premindTime = query.value('remind_time')
        remindtime = QDateTime() if premindTime is None else premindTime
        description = query.value('description')
        location = query.value('location')
        note = query.value('note')

        return KTask(id, userId, groupId, eventName, isArranged, priority, dueDate, isRepeated, remindtime, description,
                     location, note)

    def selectAllTasksGroup(self, db, group_id):
        # 准备一个SQL查询对象，用于执行数据库查询
        query = QtSql.QSqlQuery(db)
        query.prepare("SELECT * FROM todo_list WHERE group_id = ?")
        query.bindValue(0, group_id)
        taskList = []
        if not query.exec_():
            # 如果查询失败，打印错误信息并返回False
            print("Query failed:", query.lastError().text())
            return None
        while query.next():
            task = self.process_task_row(query)
            taskList.append(task)
        return taskList

    def selectAllTasks(self, db, userID):
        # 准备一个SQL查询对象，用于执行数据库查询
        query = QtSql.QSqlQuery(db)
        query.prepare("SELECT * FROM todo_list WHERE user_id = ?")
        query.bindValue(0, userID)
        taskList = []
        if not query.exec_():
            # 如果查询失败，打印错误信息并返回False
            print("Query failed:", query.lastError().text())
            return None
        while query.next():
            task = self.process_task_row(query)
            taskList.append(task)
        return taskList
