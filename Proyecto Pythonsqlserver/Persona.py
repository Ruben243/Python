import pyodbc


class Persona:
    def __init__(self):
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};''Server=DESKTOP-84SNE7A\SQLEXPRESS;'
                              'Database=Practicas;'
                              'UID=ruben;'
                              'PWD=cuelebre243')

        self.cursor = conn.cursor()

    def Obtener(self):
        self.cursor.execute("select * from Persona")

        for row in self.cursor:
            print(row)

    def Add(self, Nombre, Pais):
        consulta = 'INSERT INTO Persona(nombre,pais) Values (?,?)'
        self.cursor.execute(consulta, [Nombre, Pais])
        self.cursor.commit()

    def Edit(self, Nombre, Pais, id):
        consulta = 'UPDATE persona set nombre=?, pais=? where id=?'
        self.cursor.execute(consulta, [Nombre, Pais, id])
        self.cursor.commit()

    def Delete(self, id):
        consulta = 'DELETE from persona where id=?'
        self.cursor.execute(consulta, [id])
        self.cursor.commit()
