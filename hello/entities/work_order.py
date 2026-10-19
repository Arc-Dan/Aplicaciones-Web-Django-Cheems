from django.db import connection
from ..enums.status import Status

class Work_order:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = Status(status)

    @staticmethod
    def get_all():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT title, description, status
                FROM `work_order`
            """)
            rows = cursor.fetchall()

        return [
            Work_order(row[0], row[1], row[2])
            for row in rows
        ]