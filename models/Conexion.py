#pip install mysql-connector-python
import mysql.connector # Importa la librería mysql.connector para manejar conexiones MySQL
class Conexion:
    def __init__(self):
        #crear la conexión a la base de datos
        self.__conn = mysql.connector.connect(
            #cadena de conexión
            host="localhost", #nombre del host
            user="sistemas", #nombre del usuario
            password="sisT2025", #contraseña del usuario
            database="tienda" #nombre de la base de datos
        )

    def probar_conexion(self):
        cursor = self.__conn.cursor()
        cursor.execute("SHOW TABLES")
        for table in cursor:
            print(table)
        
    # Sirve para INSERT, UPDATE, DELETE
    def ejecutar(self, sql:str, datos=None):
        cursor = self.__conn.cursor() # Crea objeto tipo cursor
        cursor.execute(sql, datos)
        self.__conn.commit() # confirma cambios
        if cursor.rowcount > 0:
            return True
        return False
    
    def listar(self, sql:str):
        cursor = self.__conn.cursor(dictionary=True)
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscar(self, sql:str, datos):
        cursor = self.__conn.cursor(dictionary=True)
        cursor.execute(sql, datos)
        return cursor.fetchone()
    