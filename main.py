# Archivo que sirve como vista
import os 
import colorada # permite colorear líneas en el terminal
import time
import sys

symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']

def inicio_tienda(duration=2):
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        sys.stdout.write('\r' + symbols[i % len(symbols)] + ' ✨️ Bienvenido a la tienda ✨️')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * (len(symbols[0]) + len(' ✨️ Bienvenido a la tienda ✨️')) + '\r') # Clear the line
    sys.stdout.flush()
    print(f'{colorama.Fore.BLUE} Menu principal ⚙️')

def Salida_tienda(duration=2):
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        sys.stdout.write('\r' + symbols[i % len(symbols)] + ' Gracias por su visita...')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * (len(symbols[0]) + len(f' {colorama.Fore.BLUE} Gracias por su visita...')) + '\r') # Clear the line
    sys.stdout.flush()
    print(f'{colorama.Fore.RED} ¡Hasta luego ! 👋😊')
    

from dao.ProductoDAO import ProductoDAO
from models.Producto import Producto

def menu_principal():
    while True:
        os.system('clear') # os.system('clear')
        print(f'{colorama.Fore.BLUE} 💻 Tienda_CRUD')
        inicio_tienda() # animacion de bienvenida
        print(f'{colorama.Fore.GREEN} 1.Crear producto C 🆕')
        print(f'{colorama.Fore.YELLOW} 2.Listar productos R 📃')
        print(f'{colorama.Fore.CYAN} 3.Actualizar producto U 🔄')
        print(f'{colorama.Fore.RED} 4.Eliminar producto D 🗑️')
        print(f'{colorama.Fore.MAGENTA} 5.Buscar producto 🔍')
        print(f'{colorama.Fore.MAGENTA} 0.Salir ➜]')

        opcion = input(f'{colorama.Fore.GREEN}✅ Ingrese su opcion: ')
        os.system('clear')
        
        if opcion == '1':
            agrega_producto()
            
        elif opcion == '2':
            listar_productos()
            
        elif opcion == '3':
            actualizar_producto()
            
        elif opcion == '4':
            eliminar_producto()

        elif opcion == '5':
            buscar_producto()
            
        elif opcion == '0':
            Salida_tienda()
            break
            
        else:
            print('Debe ingresar una opcion valida...')
            
        input('Presione enter para continuar...')


def agrega_producto():
    print('Crear producto 🔨')
    codigo = input('Ingrese codigo de producto: ')
    while True:
        if codigo.strip() == '':
            print('El codigo no puede estar vacio. Intente de nuevo.')
            codigo = input('Ingrese codigo de producto: ')
        else:
            break
    nombre = input('Ingrese nombre de producto: ')
    while True:
        if nombre.strip() == '':
            print('El nombre no puede estar vacio. Intente de nuevo.')
            nombre = input('Ingrese nombre de producto: ')
        else:
            break
    precio = float(input('Ingrese precio de producto: '))

    stock = int(input('Ingrese stock de producto: '))

    # instancie un objeto de tipo producto
    producto = Producto(codigo=codigo, nombre=nombre, precio=precio, stock=stock)
    dao = ProductoDAO(producto)
    dao.insertar_producto()
    
def listar_productos():
    print('Listar productos 📝')
    dao = ProductoDAO()
    dao.listar_productos()

def actualizar_producto():
    print('Actualizar producto 🛠️')
    codigo = input('Ingrese codigo de producto a actualizar: ')
    nombre = input('Ingrese nuevo nombre de producto: ')
    precio = float(input('Ingrese nuevo precio de producto: '))
    stock = int(input('Ingrese nuevo stock de producto: '))
    # instancie un objeto de tipo producto
    producto = Producto(codigo=codigo, nombre=nombre, precio=precio, stock=stock)
    dao = ProductoDAO(producto)
    dao.actualizar_producto()

def eliminar_producto():
    print('Eliminar producto 🗑️')
    codigo = input('Ingrese codigo de producto a eliminar: ')
    while True:
        confirmacion = input(f'¿Está seguro de eliminar el producto con código {codigo}? (s/n): ').lower()
        if confirmacion in ['s', 'n']:
            if confirmacion == 's':
                break
            else:
                print('Operación de eliminación cancelada.')
                return
        else:
            print('Por favor, ingrese "s" para sí o "n" para no.')
    # instancie un objeto de tipo producto
    producto = Producto(codigo=codigo, nombre='', precio=0.0, stock=0)
    dao = ProductoDAO(producto)
    sql = 'DELETE FROM producto WHERE codigo=%s'
    datos = (producto.codigo,)
    if dao._ProductoDAO__conexion.ejecutar(sql, datos):
        print('Producto eliminado')
    else:
        print('Producto no se logro eliminar o producto no existe')

def buscar_producto():
    print('Buscar producto 🔍 por codigo')
    codigo = input('Ingrese codigo de producto a buscar: ')
    producto = Producto(codigo=codigo, nombre='', precio=0.0, stock=0)
    dao = ProductoDAO(producto)
    dao.buscar_producto()

menu_principal()
