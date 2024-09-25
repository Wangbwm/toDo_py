from PyQt5 import QtSql


class DbConnection:
    def __init__(self):
        # 初始化数据库连接
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("./toDo.db")

        # 尝试打开数据库连接
        if not self.db.open():
            raise Exception(self.db.lastError().text())

    def close(self):
        # 关闭数据库连接
        self.db.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def transaction(self):
        return self.db.transaction()

    def commit(self):
        return self.db.commit()

    def rollback(self):
        return self.db.rollback()
