from dao.StartDao import StartDao


class StartService:
    def __init__(self):
        self.dao = StartDao()

    @staticmethod
    def check(username, password, re_password):
        if username == '' or password == '' or re_password == '':
            return False
        else:
            return True

    def login(self, db, username, password):
        # 判断用户名和密码是否填写，即检查是否为空
        if not self.check(username, password, password):
            return False, '账号密码不能为空！'
        else:
            return self.dao.login_dao(db, username, password)

    def register(self, db, username, password, re_password):
        if not self.check(username, password, re_password):
            return False, '账号密码不能为空！'
        elif password != re_password:
            return False, '两次密码不一致！'
        return self.dao.register_dao(db, username, password)

    def selectUserID(self, db, m_username):
        return self.dao.selectUserID(db, m_username)

    def selectGroup(self, db, username):
        group_list = self.dao.selectGroupListByUserName(db, username)
        if group_list is not None:
            group_ids = group_list.split(",")
            group_map = {}
            for group_id_str in group_ids:
                group_id = int(group_id_str)
                group_map[group_id] = self.dao.selectGroupNameById(db, group_id)
            return group_map
        return None

    def selectAllTasks(self, db, username):
        db.transaction()
        userID = self.dao.selectUserID(db, username)
        taskList = []
        groupList = self.dao.selectGroupListByUserName(db, username)
        if groupList is not None:
            group_ids = groupList.split(",")
            for group_id_str in group_ids:
                group_id = int(group_id_str)
                tasks = self.dao.selectAllTasksGroup(db, group_id)
                taskList += tasks
        if userID == -1:
            db.rollback()
            taskList.clear()
            return taskList
        taskListNew = self.dao.selectAllTasks(db, userID)
        if len(taskListNew) != 0:
            taskList += taskListNew
        db.commit()
        return taskList

    def selectGroupNameById(self, db, groupId):
        return self.dao.selectGroupNameById(db, groupId)
