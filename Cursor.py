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
        try:
            conn = self.createConnection()
            cursor = conn.cursor()
            cursor.execute(getUserQuery)
            user = cursor.fetchone()
            if (user is None):
                return False
            if (user[2] != credentials["password"]):
                return False
            return True
        except Exception as ex:
            return False

    def addContender(self, contender):
        fName = contender["name"]
        fLastName = contender["firstLastName"]
        sLastName = contender["secondLastName"]
        name = f'{fName} {fLastName} {sLastName}'
        addContenderQuery = f'''
        INSERT INTO contenders (name, age, curp, gender, address, school, category, payment)
        VALUES (
        '{name}',
        {contender["age"]},
        '{contender["curp"]}',
        '{contender["gender"]}',
        '{contender["address"]}',
        '{contender["school"]}',
        '{contender["category"]}',
        {contender["payment"][0:4]}
        );
        '''
        try:
            conn = self.createConnection()
            cursor = conn.cursor()
            cursor.execute(addContenderQuery)
            conn.commit()
            conn.close()
            return True
        except Exception as ex:
            print(ex)
            return False

    def updateContender(self, contender, id):
        fName = contender["name"]
        fLastName = contender["firstLastName"]
        sLastName = contender["secondLastName"]
        name = f'{fName} {fLastName} {sLastName}'
        updateContenderQuery = f'''
        UPDATE contenders SET 
        name = '{name}',
        age = {contender["age"]},
        curp = '{contender["curp"]}',
        gender = '{contender["gender"]}',
        address = '{contender["address"]}',
        school = '{contender["school"]}',
        category = '{contender["category"]}',
        payment = {contender["payment"][0:4]}
        WHERE id = {id}
        '''
        try:
            conn = self.createConnection()
            cursor = conn.cursor()
            cursor.execute(updateContenderQuery)
            conn.commit()
            conn.close()
            return True
        except Exception as ex:
            print(ex)
            return False

    def getContenders(self):
        getContendersQuery = '''
        SELECT * FROM contenders
        '''

        try:
            conn = self.createConnection()
            cursor = conn.cursor()
            cursor.execute(getContendersQuery)
            return cursor.fetchall()
        except Exception as ex:
            print(ex)

    def deleteContender(self, id):
        deleteContenderQuery = f'''
        DELETE FROM contenders WHERE id = {id}
        '''
        print(id)
        try:
            conn = self.createConnection()
            cursor = conn.cursor()
            cursor.execute(deleteContenderQuery)
            conn.commit()
            conn.close()
            return True
        except Exception as ex:
            print(ex)
            return False
