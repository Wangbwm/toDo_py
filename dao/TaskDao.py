from PyQt5 import QtSql


class TaskDao:
    def __init__(self):
        self.db = None

    def selectGroupListByUserId(self, db, user_id):
        # 准备一个SQL查询对象，用于执行数据库查询
        query = QtSql.QSqlQuery(db)
        query.prepare("SELECT groups_list FROM todo_user WHERE id = ?")
        query.bindValue(0, user_id)
        if not query.exec_():
            # 如果查询失败，打印错误信息并返回False
            print("Query failed:", query.lastError().text())
            return None
        if query.next():
            return query.value(0)
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

