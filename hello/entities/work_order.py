from django.db import connection
from ..enums.status import Status


class Work_order:
    def __init__(self, id, title, description, status, id_user):
        self.id = id
        self.title = title
        self.description = description
        self.status = Status(status)
        self.id_user = id_user

    @staticmethod
    def get_all():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, title, description, status, id_user
                FROM `work_order`
            """)
            rows = cursor.fetchall()

        return [
            Work_order(row[0], row[1], row[2], row[3], row[4])
            for row in rows
        ]

    @staticmethod
    def create(title, description, id_user):
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO `work_order` (title, description, status, id_user)
                VALUES (%s, %s, %s, %s)
            """, [title, description, Status.PENDIENTE.value, id_user])
