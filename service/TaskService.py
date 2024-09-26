from dao.TaskDao import TaskDao


class TaskService:
    def __init__(self):
        self.dao = TaskDao()

    def selectGroup(self, db, user_id):
        group_list = self.dao.selectGroupListByUserId(db, user_id)
        if group_list is not None:
            group_ids = group_list.split(",")
            group_map = {}
            for group_id_str in group_ids:
                group_id = int(group_id_str)
                group_map[group_id] = self.dao.selectGroupNameById(db, group_id)
            return group_map
        return None