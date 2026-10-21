from django.db import connection
from ..enums.profile import Profile

class User:
    def __init__(self, name, account, profile):
        self.name = name
        self.account = account
        self.profile = Profile(profile)

    @staticmethod
    def get_all():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT name, account, profile
                FROM `user`
            """)
            rows = cursor.fetchall()

        return [
            User(row[0], row[1], row[2])
            for row in rows
        ]

    @staticmethod
    def create(name, account, profile):
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO user(name, account, profile) values(%s,%s,%s)', [name, account, profile])