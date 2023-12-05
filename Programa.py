import tkinter 
from tkinter import ttk, Menu, messagebox, LabelFrame
from datetime import datetime
import conexion
from registro import Registro
from agrProducto import AgrProducto
from config import config

class Producto:
    def __init__(self, codigo, nombre, unidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.unidad = unidad
        self.precio = precio

class Programa:
    def __init__(self, productos):
        #Caracteristicas generales
        self.programa = tkinter.Tk()
        self.programa.title(config.EMPRESA)
        self.programa.geometry('814x510')
        self.programa.resizable(width=0, height=0)
        icono = tkinter.PhotoImage(file='img/logo.png')
        self.programa.iconphoto(True, icono)
        self.listaProductos = productos
        self.productos = []

        #Agregar nombres de productos en lista
        for x in self.listaProductos:
            self.productos.append(x.nombre)

        #Variables
        var_icono_1 = tkinter.PhotoImage(file='img/añadir.png')
        var_icono_2 = tkinter.PhotoImage(file='img/registro.png')
        var_icono_3 = tkinter.PhotoImage(file='img/informacion.png')
        var_icono_4 = tkinter.PhotoImage(file='img/cerrar.png')
            
        self.var_cod1 = tkinter.StringVar(value='')
        self.var_cod2 = tkinter.StringVar(value='')
        self.var_cod3 = tkinter.StringVar(value='')
        self.var_cod4 = tkinter.StringVar(value='')
        self.var_cod5 = tkinter.StringVar(value='')

        self.var_uni1 = tkinter.StringVar(value='')
        self.var_uni2 = tkinter.StringVar(value='')
        self.var_uni3 = tkinter.StringVar(value='')
        self.var_uni4 = tkinter.StringVar(value='')
        self.var_uni5 = tkinter.StringVar(value='')

        self.var_pre1 = tkinter.StringVar(value=00.0)
        self.var_pre2 = tkinter.StringVar(value=00.0)
        self.var_pre3 = tkinter.StringVar(value=00.0)
        self.var_pre4 = tkinter.StringVar(value=00.0)
        self.var_pre5 = tkinter.StringVar(value=00.0)

        self.var_res1 = tkinter.StringVar(value=00.0)
        self.var_res2 = tkinter.StringVar(value=00.0)
        self.var_res3 = tkinter.StringVar(value=00.0)
        self.var_res4 = tkinter.StringVar(value=00.0)
        self.var_res5 = tkinter.StringVar(value=00.0)

        self.var_tota = tkinter.StringVar(value=00.0)
        self.var_fact = tkinter.StringVar(value='Factura')

        #Capa 00 - Menu desplegable
        menu = Menu(self.programa)
        self.menuInsertar = Menu(menu, tearoff=0)
        self.menuInsertar.add_command(label='Agregar producto', command=self.agregarProducto, image=var_icono_1, compound=tkinter.LEFT)
        self.menuInsertar.add_command(label='Registro de clientes', command=self.mostrarRegistro, image=var_icono_2, compound=tkinter.LEFT)
        self.menuInsertar.add_command(label='Informacion', command=self.mostrarInformacion, image=var_icono_3, compound=tkinter.LEFT)
        self.menuInsertar.add_separator()
        self.menuInsertar.add_command(label='Cerrar', command=self.cerrar, image=var_icono_4, compound=tkinter.LEFT)
        menu.add_cascade(menu=self.menuInsertar, label='Menu')
        self.programa.config(menu=menu)

        #Capa 01 - Frame (Datos del comprador)
        frame_1 = LabelFrame(self.programa, text='Datos del comprador')
        frame_1.config(font=('Bahnschrift', 10))
        
        lb_tit = ttk.Label(self.programa, text=config.EMPRESA)
        lb_tit.config(font=('Bahnschrift', 30, 'bold'))
        lb_dni = ttk.Label(frame_1, text='DNI:')
        lb_dni.config(font=('Bahnschrift', 10, 'bold'))
        lb_nom = ttk.Label(frame_1, text='Nombres:')
        lb_nom.config(font=('Bahnschrift', 10, 'bold'))
        lb_ape = ttk.Label(frame_1, text='Apellidos:')
        lb_ape.config(font=('Bahnschrift', 10, 'bold'))
        lb_tel = ttk.Label(frame_1, text='Teléfono:')
        lb_tel.config(font=('Bahnschrift', 10, 'bold'))
        lb_dir = ttk.Label(frame_1, text='Dirección:')
        lb_dir.config(font=('Bahnschrift', 10, 'bold'))
        
        self.et_dni = ttk.Entry(frame_1, width=30)
        self.et_nom = ttk.Entry(frame_1, width=30)
        self.et_ape = ttk.Entry(frame_1, width=30)
        self.et_tel = ttk.Entry(frame_1, width=30)
        self.et_dir = ttk.Entry(frame_1, width=30)

        #Capa 02 - Widgets (Datos de la compra)
        lb_informacion2 = ttk.Label(self.programa, text='Seleccionar los productos:', anchor=tkinter.W)
        lb_informacion2.config(font=('Bahnschrift', 10))
        lb_cod = ttk.Label(self.programa, text='Codigo')
        lb_cod.config(font=('Bahnschrift', 10, 'bold'))
        lb_pro = ttk.Label(self.programa, text='Producto')
        lb_pro.config(font=('Bahnschrift', 10, 'bold'))
        lb_can = ttk.Label(self.programa, text='Cantidad')
        lb_can.config(font=('Bahnschrift', 10, 'bold'))
        lb_uni = ttk.Label(self.programa, text='Unidad')
        lb_uni.config(font=('Bahnschrift', 10, 'bold'))
        lb_pre = ttk.Label(self.programa, text='Precio')
        lb_pre.config(font=('Bahnschrift', 10, 'bold'))
        lb_tot = ttk.Label(self.programa, text='Total')
        lb_tot.config(font=('Bahnschrift', 10, 'bold'))
        
        self.et_cod1 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_cod1, justify=tkinter.CENTER, width=8)
        self.et_cod2 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_cod2, justify=tkinter.CENTER, width=8)
        self.et_cod3 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_cod3, justify=tkinter.CENTER, width=8)
        self.et_cod4 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_cod4, justify=tkinter.CENTER, width=8)
        self.et_cod5 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_cod5, justify=tkinter.CENTER, width=8)

        self.cb_producto1 = ttk.Combobox(self.programa, state='readonly', values=self.productos)
        self.cb_producto1.bind('<<ComboboxSelected>>', self.completarDatos1)
        self.cb_producto2 = ttk.Combobox(self.programa, state='readonly', values=self.productos)
        self.cb_producto2.bind('<<ComboboxSelected>>', self.completarDatos2)
        self.cb_producto3 = ttk.Combobox(self.programa, state='readonly', values=self.productos)
        self.cb_producto3.bind('<<ComboboxSelected>>', self.completarDatos3)
        self.cb_producto4 = ttk.Combobox(self.programa, state='readonly', values=self.productos)
        self.cb_producto4.bind('<<ComboboxSelected>>', self.completarDatos4)
        self.cb_producto5 = ttk.Combobox(self.programa, state='readonly', values=self.productos)
        self.cb_producto5.bind('<<ComboboxSelected>>', self.completarDatos5)

        self.sb_cantidad1 = ttk.Spinbox(self.programa, from_=1, to=1000, width=7, state='readonly', command=self.hallarTotal1)
        self.sb_cantidad2 = ttk.Spinbox(self.programa, from_=1, to=1000, width=7, state='readonly', command=self.hallarTotal2)
        self.sb_cantidad3 = ttk.Spinbox(self.programa, from_=1, to=1000, width=7, state='readonly', command=self.hallarTotal3)
        self.sb_cantidad4 = ttk.Spinbox(self.programa, from_=1, to=1000, width=7, state='readonly', command=self.hallarTotal4)
        self.sb_cantidad5 = ttk.Spinbox(self.programa, from_=1, to=1000, width=7, state='readonly', command=self.hallarTotal5)

        self.et_uni1 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_uni1, justify=tkinter.CENTER)
        self.et_uni2 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_uni2, justify=tkinter.CENTER)
        self.et_uni3 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_uni3, justify=tkinter.CENTER)
        self.et_uni4 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_uni4, justify=tkinter.CENTER)
        self.et_uni5 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_uni5, justify=tkinter.CENTER)

        self.et_pre1 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_pre1, justify=tkinter.CENTER, width=10)
        self.et_pre2 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_pre2, justify=tkinter.CENTER, width=10)
        self.et_pre3 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_pre3, justify=tkinter.CENTER, width=10)
        self.et_pre4 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_pre4, justify=tkinter.CENTER, width=10)
        self.et_pre5 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_pre5, justify=tkinter.CENTER, width=10)

        self.et_res1 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_res1, justify=tkinter.RIGHT)
        self.et_res2 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_res2, justify=tkinter.RIGHT)
        self.et_res3 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_res3, justify=tkinter.RIGHT)
        self.et_res4 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_res4, justify=tkinter.RIGHT)
        self.et_res5 = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_res5, justify=tkinter.RIGHT)

        self.et_resT = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_tota, justify=tkinter.CENTER)

        self.bt_calc = ttk.Button(self.programa, text='Calcular', command=self.calcularTotal)
        self.bt_fact = ttk.Button(self.programa, text='Facturar', command=self.imprimirFactura)
        self.et_fact = ttk.Entry(self.programa, state=tkinter.DISABLED, textvariable=self.var_fact, justify=tkinter.CENTER)
        
        #Grid 1 - Frame (Datos del comprador)
        lb_tit.grid(row=0, column=0, columnspan=6, pady=20)
        
        lb_dni.grid(row=0, column=0, pady=10, padx=5)
        lb_nom.grid(row=1, column=0, pady=10, padx=5)
        lb_ape.grid(row=0, column=2, pady=10, padx=5)
        lb_tel.grid(row=1, column=2, pady=10, padx=5)
        lb_dir.grid(row=0, column=4, pady=10, padx=5)
        
        self.et_dni.grid(row=0, column=1, pady=10, padx=5)
        self.et_nom.grid(row=1, column=1, pady=10, padx=5)
        self.et_ape.grid(row=0, column=3, pady=10, padx=5)
        self.et_tel.grid(row=1, column=3, pady=10, padx=5)
        self.et_dir.grid(row=0, column=5, pady=10, padx=5)

        frame_1.grid(row=1, column=0, columnspan=6, padx=5)
        
        #Grid capa 2
        lb_informacion2.grid(row=4, column=0, columnspan=6, sticky='NSWE', padx=5, pady=10)
        lb_cod.grid(row=5, column=0, pady=10)
        lb_pro.grid(row=5, column=1, pady=10)
        lb_can.grid(row=5, column=2, pady=10)
        lb_uni.grid(row=5, column=3)
        lb_pre.grid(row=5, column=4)
        lb_tot.grid(row=5, column=5, pady=10)
        
        self.et_cod1.grid(row=6, column=0, padx=5)
        self.et_cod2.grid(row=7, column=0, padx=5)
        self.et_cod3.grid(row=8, column=0, padx=5)
        self.et_cod4.grid(row=9, column=0, padx=5)
        self.et_cod5.grid(row=10, column=0, padx=5)
        
        self.cb_producto1.grid(row=6, column=1, pady=5, sticky='NSWE', padx=10)
        self.cb_producto2.grid(row=7, column=1, pady=5, sticky='NSWE', padx=10)
        self.cb_producto3.grid(row=8, column=1, pady=5, sticky='NSWE', padx=10)
        self.cb_producto4.grid(row=9, column=1, pady=5, sticky='NSWE', padx=10)
        self.cb_producto5.grid(row=10, column=1, pady=5, sticky='NSWE', padx=10)
        
        self.sb_cantidad1.grid(row=6, column=2)
        self.sb_cantidad2.grid(row=7, column=2)
        self.sb_cantidad3.grid(row=8, column=2)
        self.sb_cantidad4.grid(row=9, column=2)
        self.sb_cantidad5.grid(row=10, column=2)
        
        self.et_uni1.grid(row=6, column=3)
        self.et_uni2.grid(row=7, column=3)
        self.et_uni3.grid(row=8, column=3)
        self.et_uni4.grid(row=9, column=3)
        self.et_uni5.grid(row=10, column=3)

        self.et_pre1.grid(row=6, column=4)
        self.et_pre2.grid(row=7, column=4)
        self.et_pre3.grid(row=8, column=4)
        self.et_pre4.grid(row=9, column=4)
        self.et_pre5.grid(row=10, column=4)
        
        self.et_res1.grid(row=6, column=5)
        self.et_res2.grid(row=7, column=5)
        self.et_res3.grid(row=8, column=5)
        self.et_res4.grid(row=9, column=5)
        self.et_res5.grid(row=10, column=5)

        self.bt_calc.grid(row=11, column=4, pady=10)
        self.bt_fact.grid(row=12, column=4)
        
        self.et_resT.grid(row=11, column=5, pady=10)
        self.et_fact.grid(row=12, column=5)  

        self.programa.mainloop()

    def completarDatos1(self, event):
        self.completarDatos(1)
        self.hallarTotal1()

    def completarDatos2(self, event):
        self.completarDatos(2)
        self.hallarTotal2()

    def completarDatos3(self, event):
        self.completarDatos(3)
        self.hallarTotal3()

    def completarDatos4(self, event):
        self.completarDatos(4)
        self.hallarTotal4()

    def completarDatos5(self, event):
        self.completarDatos(5)
        self.hallarTotal5()

    def hallarTotal1(self):
        self.hallarTotal(1)

    def hallarTotal2(self):
        self.hallarTotal(2)

    def hallarTotal3(self):
        self.hallarTotal(3)

    def hallarTotal4(self):
        self.hallarTotal(4)

    def hallarTotal5(self):
        self.hallarTotal(5)

    def agregarProducto(self):
        AgrProducto()

    def mostrarRegistro(self):
        Registro()

    def mostrarInformacion(self):
        messagebox.showinfo('Información del programa', 'El programa fue diseñado por el estudiante de Ing. Jhon Jaimes Cayetano, su función es administrar a sus clientes, productos y ventas. La versión actual del programa es la 0.0.1.')

    def cerrar(self):
        self.programa.destroy()

    def calcularTotal(self):
        total = float(self.var_res1.get()) + float(self.var_res2.get()) + float(self.var_res3.get()) + float(self.var_res4.get()) + float(self.var_res5.get())
        igv = total * 0.18
        self.var_tota.set(round(total + igv, 1))

    def completarDatos(self, fila):
        if fila == 1:
            for x in self.listaProductos:
                if self.cb_producto1.get() == x.nombre:
                    self.var_cod1.set(x.codigo)
                    self.var_uni1.set(x.unidad)
                    self.var_pre1.set(x.precio)
        elif fila == 2:
            for x in self.listaProductos:
                if self.cb_producto2.get() == x.nombre:
                    self.var_cod2.set(x.codigo)
                    self.var_uni2.set(x.unidad)
                    self.var_pre2.set(x.precio)
        elif fila == 3:
            for x in self.listaProductos:
                if self.cb_producto3.get() == x.nombre:
                    self.var_cod3.set(x.codigo)
                    self.var_uni3.set(x.unidad)
                    self.var_pre3.set(x.precio)
        elif fila == 4:
            for x in self.listaProductos:
                if self.cb_producto4.get() == x.nombre:
                    self.var_cod4.set(x.codigo)
                    self.var_uni4.set(x.unidad)
                    self.var_pre4.set(x.precio)
        elif fila == 5:
            for x in self.listaProductos:
                if self.cb_producto5.get() == x.nombre:
                    self.var_cod5.set(x.codigo)
                    self.var_uni5.set(x.unidad)
                    self.var_pre5.set(x.precio)

    def hallarTotal(self, total):
        if total == 1:
            precio = float(self.var_pre1.get())
            if len(self.sb_cantidad1.get()) != 0:
                cantidad = float(self.sb_cantidad1.get())
            else:
                cantidad = 0
            self.var_res1.set(round(precio * cantidad, 1))
        elif total == 2:
            precio = float(self.var_pre2.get())
            if len(self.sb_cantidad2.get()) != 0:
                cantidad = float(self.sb_cantidad2.get())
            else:
                cantidad = 0
            self.var_res2.set(round(precio * cantidad, 1))
        elif total == 3:
            precio = float(self.var_pre3.get())
            if len(self.sb_cantidad3.get()) != 0:
                cantidad = float(self.sb_cantidad3.get())
            else:
                cantidad = 0
            self.var_res3.set(round(precio * cantidad, 1))
        elif total == 4:
            precio = float(self.var_pre4.get())
            if len(self.sb_cantidad4.get()) != 0:
                cantidad = float(self.sb_cantidad4.get())
            else:
                cantidad = 0
            self.var_res4.set(round(precio * cantidad, 1))
        elif total == 5:
            precio = float(self.var_pre5.get())
            if len(self.sb_cantidad5.get()) != 0:
                cantidad = float(self.sb_cantidad5.get())
            else:
                cantidad = 0
            self.var_res5.set(round(precio * cantidad, 1))
        
    def imprimirFactura(self):
        self.guardarCliente()
        #Algoritmo de espaciado
        espacioTotal = 30
        espacio = ''
        espacio1 = ''
        espacio2 = ''
        espacio3 = ''
        espacio4 = ''
        espacio5 = ''
        p1 = 30 - len(self.cb_producto1.get())
        p2 = 30 - len(self.cb_producto2.get())
        p3 = 30 - len(self.cb_producto3.get())
        p4 = 30 - len(self.cb_producto4.get())
        p5 = 30 - len(self.cb_producto5.get())
        listap = [p1, p2, p3, p4, p5]
        listae = [espacio1, espacio2, espacio3, espacio4, espacio5]
        contador = 0
        for p in listap:
            for x in range(p):
                espacio += ' '
            listae[contador] = espacio
            contador += 1
            espacio = ''

        ob_hora = datetime.now()

        cadena = (f'''
{config.EMPRESA.center(39, '-')}

Fecha: {ob_hora.strftime("%d/%m/%Y")}

DNI: {self.et_dni.get()}
Nombre: {self.et_nom.get()} {self.et_ape.get()}
Telefono: {self.et_tel.get()}
Dirección: {self.et_dir.get()}

---------------------------------------
         Articulo           SubTotal
---------------------------------------
{self.cb_producto1.get()}{listae[0]}{self.et_res1.get()}
{self.cb_producto2.get()}{listae[1]}{self.et_res2.get()}
{self.cb_producto3.get()}{listae[2]}{self.et_res3.get()}
{self.cb_producto4.get()}{listae[3]}{self.et_res4.get()}
{self.cb_producto5.get()}{listae[4]}{self.et_res5.get()}

---------------------------------------
                     subtotal        
                          IGV        
                        Total {self.var_tota.get()}
---------------------------------------

Contacto: {config.EMAIL_FACTURA}

---------------------------------------
''')
        try:
            #Abrimos el archivo open(ruta, modo=escritura/archivotexto)
            factura = open(config.RUTA_FACTURA + 'factura.txt', mode='wt')
            factura.write(cadena)
            factura.close()
        except Exception as err:
            print(err)

    def guardarCliente(self):
        if len(self.et_nom.get()) > 0 and len(self.et_ape.get()) > 0 and len(self.et_tel.get()) > 0:
            nombre = self.et_nom.get() + ' ' + self.et_ape.get()
            ob_hora = datetime.now()
            fecha = ob_hora.strftime("%d/%m/%Y - %I:%M %p")
            datos = (self.et_dni.get(), nombre, self.et_tel.get(), self.et_dir.get(), fecha)
            conexion.insertarCliente(datos)
        else:
            messagebox.showerror('Error', 'No se ingresaron todos los datos necesarios del comprador.')


datos = conexion.consultarDatos()
productos = []
for x in datos['Productos']:
    producto = Producto(x['codigo'], x['nombre'], x['unidad'], x['precio'])
    productos.append(producto)
Programa(productos)


