import pymysql

class Data:

    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            db="prueba"
        )

        self.cursor = self.conn.cursor()

    def insertItems(self, element):
        sql = "insert into persona(Nombre, Edad, Carrera) values('{}', '{}', '{}')".format(element[0], element[1], element[2])
        self.cursor.execute(sql)
        self.conn.commit()

    def ReturnOneItem(self, ref):
        sql = "select * from persona where Nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def ReturnForCarreer(self, ref):
        sql = "select * from persona where Carrera = '{}'".format(ref)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def returnAllElements(self):
        sql = "select * from persona"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def Delete(self, ref):
        sql = "delete from persona where Nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conn.commit()

    def UpdateItem(self, element, ref):

        sql = "update persona set Nombre = '{}',Edad = '{}', Carrera='{}' where Nombre = '{}'".format(element[0],
                                                                                                      element[1],
                                                                                                      element[2], ref)

        self.cursor.execute(sql)
        self.conn.commit()
