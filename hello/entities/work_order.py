from django.db import connection
from ..enums.status import Status
from ..enums.action import Action


class Work_order:
    def __init__(self, id, title, description, status):
        self.id = id
        self.title = title
        self.description = description
        self.status = Status(status)

    @staticmethod
    def get_all():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, title, description, status
                FROM `work_order`
            """)
            rows = cursor.fetchall()

        return [
            Work_order(row[0], row[1], row[2], row[3])
            for row in rows
        ]

    @staticmethod
    def create(title, description):
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO `work_order` (title, description, status)
                VALUES (%s, %s, %s)
            """, [title, description, Status.PENDIENTE.value])

    @staticmethod
    def get_by_id(id):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, title, description, status
                FROM `work_order` WHERE id = %s
            """, [id])
            row = cursor.fetchone()

        if row:
            return Work_order(row[0], row[1], row[2], row[3])

        return None

    @staticmethod
    def update(id, title, description):
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE `work_order` SET title = %s, description = %s WHERE id = %s
            """, [title, description, id])

    @staticmethod
    def get_available():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, title, description, status
                FROM work_order
                WHERE status = %s AND NOT EXISTS (
                    SELECT 1 FROM work_order_history
                    WHERE id_work_order = work_order.id AND action = %s
                )
            """, [Status.PENDIENTE.value, Action.CREAR.value])
            rows = cursor.fetchall()

        return [
            Work_order(row[0], row[1], row[2], row[3])
            for row in rows
        ]

    @staticmethod
    def update_status(id, status):
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE work_order SET status = %s WHERE id = %s
            """, [status, id])
