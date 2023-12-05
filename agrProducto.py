import tkinter 
from tkinter import ttk, messagebox
import conexion

class AgrProducto(tkinter.Toplevel):
    def __init__(self):
        self.V_agregarProducto = tkinter.Tk()
        self.V_agregarProducto.title('Agregar productos')
        self.V_agregarProducto.geometry('240x240')
        self.V_agregarProducto.resizable(width=0, height=0)
        
        lb_tit = ttk.Label(self.V_agregarProducto, text='Agregar productos')
        lb_tit.config(font=('Verdana', 16))
        lb_pro = ttk.Label(self.V_agregarProducto, text='Nombre del producto:')
        lb_uni = ttk.Label(self.V_agregarProducto, text='Unidad del producto:')
        lb_pre = ttk.Label(self.V_agregarProducto, text='Precio del producto:')
        
        self.et_pro = ttk.Entry(self.V_agregarProducto, width=30)
        self.et_uni = ttk.Entry(self.V_agregarProducto, width=30)
        self.et_pre = ttk.Entry(self.V_agregarProducto, width=30)
        bt_sub = ttk.Button(self.V_agregarProducto, text='Agregar', command=self.enviarProducto)

        lb_tit.grid(row=0, column=0, columnspan=2, pady=20, sticky='NSWE', padx=20)
        lb_pro.grid(row=1, column=0, columnspan=2, sticky='NSWE', padx=20)
        lb_uni.grid(row=3, column=0, columnspan=2, sticky='NSWE', padx=20)
        lb_pre.grid(row=5, column=0, columnspan=2, sticky='NSWE', padx=20)

        self.et_pro.grid(row=2, column=0, sticky='NSWE', padx=20)
        self.et_uni.grid(row=4, column=0, sticky='NSWE', padx=20)
        self.et_pre.grid(row=6, column=0, sticky='NSWE', padx=20)
        bt_sub.grid(row=7, column=0, padx=20, pady=10)

    def enviarProducto(self):
            try:
                precio = float(self.et_pre.get())
                if len(self.et_pro.get()) != 0 and len(self.et_uni.get()) != 0 and precio > 0:
                    datos = (self.et_pro.get(), self.et_uni.get(), self.et_pre.get())
                    conexion.insertarProducto(datos)
                    messagebox.showinfo('Información', 'El producto se guardo exitosamente en la base de datos. Se recomienda reiniciar el programa para visualizar los cambios.')
                    self.V_agregarProducto.destroy()
                else:
                    messagebox.showerror('Error', 'No se ingresaron todos los datos necesarios para el registro del producto.')
                    self.V_agregarProducto.destroy()
            except Exception as err:
                messagebox.showerror('Error', err)
                self.V_agregarProducto.destroy()

