from PyQt5.QtCore import QDateTime

from dao.TaskDao import TaskDao


class TaskService:
    def __init__(self):
        self.dao = TaskDao()
        self.m_unscheduledTasks = []
        self.m_HaveFinishedTasks = []
        self.m_next7DaysTasks = []
        self.m_afterNextWeekTasks = []

    def selectGroup(self, db, user_id):
        group_list = self.dao.selectGroupListByUserId(db, user_id)
        if group_list is not None:
            group_map = {}
            for group_id in group_list:
                group_map[group_id] = self.dao.selectGroupNameById(db, group_id)
            return group_map
        return None

    def init_task_list(self, db, user_id):
        db.transaction()
        all_task_list = []
        group_list = self.dao.selectGroupListByUserId(db, user_id)
        if group_list is not None:
            for group_id in group_list:
                tasks = self.dao.selectAllTasksGroup(db, group_id)
                all_task_list += tasks
        if user_id == -1:
            db.rollback()
            all_task_list.clear()
        else:
            taskListNew = self.dao.selectAllTaskByUserId(db, user_id)
            if len(taskListNew) != 0:
                all_task_list += taskListNew
            db.commit()

        self.m_unscheduledTasks.clear()
        self.m_HaveFinishedTasks.clear()
        self.m_next7DaysTasks.clear()
        self.m_afterNextWeekTasks.clear()
        if len(all_task_list) != 0:
            for task in all_task_list:
                if not task.arranged:
                    self.m_unscheduledTasks.append(task)
                elif task.dueDate < QDateTime.currentDateTime():
                    self.m_HaveFinishedTasks.append(task)
                elif QDateTime.currentDateTime() <= task.dueDate < \
                        QDateTime.currentDateTime().addDays(7):
                    self.m_next7DaysTasks.append(task)
                else:
                    self.m_afterNextWeekTasks.append(task)
        # 返回数组
        return all_task_list, self.m_unscheduledTasks, self.m_HaveFinishedTasks, self.m_next7DaysTasks, self.m_afterNextWeekTasks

    def selectGroupNameById(self, db, group_id):
        return self.dao.selectGroupNameById(db, group_id)



