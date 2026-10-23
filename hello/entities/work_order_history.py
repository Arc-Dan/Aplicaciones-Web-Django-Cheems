from django.db import connection
from ..enums.action import Action


class Work_order_history:
    def __init__(self, id, date, id_user, action, id_work_order, user_name, order_title):
        self.id = id
        self.date = date
        self.id_user = id_user
        self.action = Action(action)
        self.id_work_order = id_work_order
        self.user_name = user_name
        self.order_title = order_title

    @staticmethod
    def get_all():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT h.id, h.date, h.id_user, h.action, h.id_work_order,
                       u.name, w.title
                FROM work_order_history h
                LEFT JOIN user u ON h.id_user = u.id
                LEFT JOIN work_order w ON h.id_work_order = w.id
                ORDER BY h.id DESC
            """)
            rows = cursor.fetchall()

        return [
            Work_order_history(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            for row in rows
        ]

    @staticmethod
    def get_by_id(id):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT h.id, h.date, h.id_user, h.action, h.id_work_order,
                       u.name, w.title
                FROM work_order_history h
                LEFT JOIN user u ON h.id_user = u.id
                LEFT JOIN work_order w ON h.id_work_order = w.id
                WHERE h.id = %s
            """, [id])
            row = cursor.fetchone()

        if row:
            return Work_order_history(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

        return None

    @staticmethod
    def create(id_user, action, id_work_order):
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO work_order_history (date, id_user, action, id_work_order)
                VALUES (CURRENT_TIMESTAMP, %s, %s, %s)
            """, [id_user, action, id_work_order])
