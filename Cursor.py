import sqlite3


class Cursor ():
    def __init__(self):
        pass

    def createConnection(self):
        connection = sqlite3.connect("database/chess.sqlite3")
        return connection

    def logIn(self, credentials):
        getUserQuery = f'''
        SELECT * FROM users WHERE email = '{credentials["email"]}'
        '''
        conn = self.createConnection()
        cursor = conn.cursor()
        cursor.execute(getUserQuery)
        user = cursor.fetchone()

        if (user is None):
            return False
        if (user[2] != credentials["password"]):
            return False

        return True
