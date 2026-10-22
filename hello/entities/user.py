from django.db import connection
from ..enums.profile import Profile

class User:
    def __init__(self, id, name, account, password, profile):
        self.id = id
        self.name = name
        self.account = account
        self.password = password
        self.profile = Profile(profile)

    @staticmethod
    def get_all():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, name, account, password, profile
                FROM `user`
            """)
            rows = cursor.fetchall()

        return [
            User(row[0], row[1], row[2], row[3], row[4])
            for row in rows
        ]

    @staticmethod
    def create(name, account, password, profile):
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO user(name, account, password, profile) values(%s,%s,%s,%s)', [name, account, password, profile])

    @staticmethod
    def get_by_id(id):
        with connection.cursor() as cursor:
            cursor.execute('SELECT id, name, account, password, profile FROM user WHERE id = %s', [id])
            row = cursor.fetchone()

        if row:
            return User(row[0], row[1], row[2], row[3], row[4])

        return None

    @staticmethod
    def update(id, name, account, password, profile):
        with connection.cursor() as cursor:
            cursor.execute('UPDATE user SET name=%s, account=%s, password=%s, profile=%s WHERE id = %s', [name, account, password, profile, id])