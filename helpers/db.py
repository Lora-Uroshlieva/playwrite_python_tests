import sqlite3


class DataBase:
    def __init__(self, path: str):
        self.connection = sqlite3.connect(path)

    def list_testcases(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM tcm_testcase')
        return cursor.fetchall()

    def delete_testcase_by_name(self, name: str):
        cursor = self.connection.cursor()
        cursor.execute(f'DELETE  FROM tcm_testcase WHERE name=?', (name,))
        self.connection.commit()

    def close(self):
        self.connection.close()
