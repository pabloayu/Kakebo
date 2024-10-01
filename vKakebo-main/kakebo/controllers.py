import tkinter as tk
from kakebo.vistas import FormMovimiento
from kakebo.modelos import DaoSqlite
from kakebo import PATH_DATABASE

class Controller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minikakebo")
        self.form = FormMovimiento(self, self.grabaMovimiento)
        self.form.pack()
        self.dao = DaoSqlite(PATH_DATABASE)
        
    def grabaMovimiento(self, movimiento):
        print("Por aqui pasa")
        print(movimiento)
        self.dao.grabar(movimiento)
        # leer todos los movvimientos 
        # enviar todos los movimientos al componente listaMovimientos
        