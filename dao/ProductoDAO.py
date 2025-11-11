# dao/ProductoDAO.py
# DAO: Data Access Object para la entidad Producto
from models.Conexion import Conexion
# Importamos la clase Producto
from models.Producto import Producto
# DAO: Data Access Object
class ProductoDAO:
    # Constructor
    def __init__(self, producto:Producto = None):
        # Instancia de clase Conexion
        self.__conexion = Conexion()
        # Atributo privado para la instancia de clase Producto
        self.__producto = producto 
        # instancia de clase producto recibida desde main.py

    # Metodo para insertar producto    
    def insertar_producto(self):
        # Sentencia SQL
        sql = 'INSERT INTO producto(codigo, nombre, precio, stock) VALUES (%s, %s, %s, %s)'
        # Datos a insertar
        datos = (self.__producto.codigo, self.__producto.nombre, self.__producto.precio, self.__producto.stock)
        # Ejecutar la sentencia
        if self.__conexion.ejecutar(sql, datos):
            print('Producto registrado 👍')
        else:
            print('Producto no se logro registrar ☹')

    # Metodo para listar productos        
    def listar_productos(self):
        sql = 'SELECT codigo, nombre, precio, stock FROM producto'
        lista = self.__conexion.listar(sql)
        for producto in lista:
            print(f'Codigo: {producto["codigo"]}')
            print(f'Nombre: {producto["nombre"]}')
            print(f'Precio: {producto["precio"]}')
            print(f'Stock: {producto["stock"]}')
            print('❯❯❯'*50)
    
    # Metodo para actualizar producto
    def actualizar_producto(self):
        sql = 'UPDATE producto SET nombre=%s, precio=%s WHERE codigo=%s'
        datos = (self.__producto.nombre, self.__producto.precio, self.__producto.codigo)
        if self.__conexion.ejecutar(sql, datos):
            print('Producto actualizado')
        else:
            print('Producto no se logro actualizar')
