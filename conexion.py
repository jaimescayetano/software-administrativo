import mysql.connector  

def conectar():
    conexion = mysql.connector.connect(host='localhost',
                                            user='root',
                                            passwd='',
                                            database='tornillo_feliz')
    cursor = conexion.cursor()
    return conexion, cursor

def insertarProducto(datos):
    conexion, cursor = conectar()
    sentencia = "INSERT INTO productos(ID, Nombre, Unidad, Precio) VALUES(NULL, %s, %s, %s)"
    cursor.execute(sentencia, datos)
    conexion.commit()
    conexion.close()

def consultarDatos():
    conexion, cursor = conectar()
    sentencia = "SELECT * from productos"
    cursor.execute(sentencia)
    productos = {}
    productos['Productos'] = []
    for producto in cursor:
        productos['Productos'].append({'codigo':producto[0], 'nombre':producto[1], 'unidad':producto[2], 'precio':producto[3]})
    conexion.close()
    return productos

def insertarCliente(datos):
    conexion, cursor = conectar()
    sentencia = "INSERT INTO clientes(ID, DNI, Nombre, Telefono, Direccion, Fecha) VALUES(NULL, %s, %s, %s, %s, %s)"
    cursor.execute(sentencia, datos)
    conexion.commit()
    conexion.close()

def consultarClientes():
    conexion, cursor = conectar()
    sentencia = "SELECT DNI, Nombre, Telefono, Direccion, Fecha from clientes"
    cursor.execute(sentencia)
    clientes = {}
    clientes['Clientes'] = []
    for cliente in cursor:
        clientes['Clientes'].append({'dni':cliente[0], 'nombre':cliente[1], 'telefono':cliente[2], 'direccion':cliente[3], 'fecha':cliente[4]})
    conexion.close()
    return clientes
