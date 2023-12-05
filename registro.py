import conexion 
import tkinter
from tkinter import ttk

class Registro(tkinter.Toplevel):
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title('Prueba de tablas')
        self.ventana.geometry('1015x400')
        self.ventana.resizable(width=0, height=0)

        lb_tit = ttk.Label(self.ventana, text='Registro de clientes')
        lb_tit.config(font=('Bahnschrift', 30, 'bold'))

        self.tv_clientes = ttk.Treeview(self.ventana, columns=('#nombre', '#telefono', '#direccion', '#fecha'))
        bt_limp = ttk.Button(self.ventana, text='Limpiar', command=self.limpiar)
        bt_actu = ttk.Button(self.ventana, text='Actualizar', command=self.actualizar)

        lb_tit.grid(row=0, column=0, columnspan=4, pady=20)
        bt_actu.grid(row=1, column=0, pady=10, sticky='NSWE', padx=5)
        bt_limp.grid(row=1, column=1, pady=10, sticky='NSWE', padx=5)
        self.tv_clientes.grid(row=2, column=0, columnspan=4, padx=5)


        self.tv_clientes.heading('#0', text='DNI')
        self.tv_clientes.heading('#nombre', text='Nombre')
        self.tv_clientes.heading('#telefono', text='Telefono')
        self.tv_clientes.heading('#direccion', text='Dirección')
        self.tv_clientes.heading('#fecha', text='Fecha')

        self.mostrarDatos()

        self.ventana.mainloop()
            
    def mostrarDatos(self):
        self.respuesta = conexion.consultarClientes()
        for x in self.respuesta['Clientes']:
            self.tv_clientes.insert('', 0, text=x['dni'], values=(x['nombre'], x['telefono'], x['direccion'], x['fecha']))

    def actualizar(self):
        self.tv_clientes.delete(*self.tv_clientes.get_children())
        self.mostrarDatos()

    def limpiar(self):
        self.tv_clientes.delete(*self.tv_clientes.get_children())

