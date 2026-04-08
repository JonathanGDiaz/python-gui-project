import sqlite3


class Cursor ():
    def __init__(self):
        pass

    def createConnection(self):
        connection = sqlite3.connect("database/chess.sqlite3")
        return connection

    def logIn(self, credentials):
        getUserQuery = "SELECT * FROM users WHERE email = ?"

        try:
            conn = self.createConnection()
            cursor = conn.cursor()
            cursor.execute(getUserQuery, (credentials["email"],))
            user = cursor.fetchone()
            conn.close()

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
        addContenderQuery =  """
            INSERT INTO contenders 
            (name, age, curp, gender, address, school, category, payment)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """
        try:
            conn = self.createConnection()
            cursor = conn.cursor()
            cursor.execute(addContenderQuery, (
                name,
                contender["age"],
                contender["curp"],
                contender["gender"],
                contender["address"],
                contender["school"],
                contender["category"],
                contender["payment"]
            ))
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
        updateContenderQuery = '''UPDATE contenders SET 
        name = ?,
        age = ?,
        curp = ?,
        gender = ?,
        address = ?,
        school = ?,
        category = ?,
        payment = ?
        WHERE id = ?
        '''
        try:
            conn = self.createConnection()
            cursor = conn.cursor()
            cursor.execute(updateContenderQuery, (
                name,
                contender["age"],
                contender["curp"],
                contender["gender"],
                contender["address"],
                contender["school"],
                contender["category"],
                contender["payment"],
                id
            ))
            conn.commit()
            conn.close()
            return True
        except Exception as ex:
            print(ex)
            return False

    def getContenders(self):
        getContendersQuery = "SELECT * FROM contenders"

        try:
            conn = self.createConnection()
            cursor = conn.cursor()
            cursor.execute(getContendersQuery)
            result =  cursor.fetchall()
            conn.close()
            return result
        except Exception as ex:
            print(ex)

    def deleteContender(self, id):
        deleteContenderQuery = "DELETE FROM contenders WHERE id = ?"
        try:
            conn = self.createConnection()
            cursor = conn.cursor()
            cursor.execute(deleteContenderQuery, (id,))
            conn.commit()
            conn.close()
            return True
        except Exception as ex:
            print(ex)
            return False

    def searchContender(self, query):
        searchQuery = "SELECT * FROM contenders WHERE name LIKE ? ESCAPE '\\'"
        try:
            conn = self.createConnection()
            cursor = conn.cursor()
            query = query.replace("%", r"\%").replace("_", r"\_")
            cursor.execute(searchQuery, ("%" + query + "%",))
            result = cursor.fetchall()
            conn.close()
            return result
        except Exception as ex:
            print(ex)
            return False
    
    def filterContenders(self, query, filter="Novice"):
        try:
            conn = self.createConnection()
            cursor = conn.cursor()


            if query is None:
                filterQuery = "SELECT * FROM contenders WHERE category = ?"

                cursor.execute(filterQuery, (filter,))
            else:
                filterQuery = "SELECT * FROM contenders WHERE name LIKE ? ESCAPE '\\' AND category = ?"
                query = query.replace("%", r"\%").replace("_", r"\_")
                cursor.execute(filterQuery, ("%" + query + "%", filter))
            result = cursor.fetchall()
            conn.close()
            return result
        except Exception as ex:
            print(ex)
            return False