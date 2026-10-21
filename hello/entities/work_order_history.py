from django.db import connection
from ..enums.action import Action

class Work_order_history:
    def __init__(self, id_user, action, id_work_order):
        self.id_user = id_user
        self.action = Action(action)
        self.id_work_order = id_work_order

    @staticmethod
    def get_all():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id_user, action, id_work_order
                FROM `work_order_history`
            """)
            rows = cursor.fetchall()

        return [
            Work_order_history(row[0], row[1], row[2])
            for row in rows
        ]

    @staticmethod
    def create(id_user, action, id_work_order):
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO work_order_history(id_user,action,id_work_order) values(%s,%s,%s)', [id_user, action, id_work_order])