# Importamos tkinter, que nos sirve para hacer ventanas con botones, textos, etc.
import tkinter as tk

# También traemos las diferentes pantallas del sistema desde otros archivos
from inicio import InicioPage
from reservar import ReservarPage
from admin import AdminPage
from promociones import PromocionesPage

# Esta es la clase principal de nuestra app del cine
class CineApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Preparamos la ventana principal
        self.title("Sistema de Cine BUAP")  # Le ponemos un nombre a la ventana
        self.geometry("680x600")  # Le damos un tamaño fijo
        self.resizable(False, False)  # No dejamos que cambien el tamaño de la ventana

        # Aquí vamos a poner todas las pantallas de la app
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}  # Un lugar donde guardamos las pantallas que vayamos creando

        # Creamos cada pantalla (inicio, reservar, admin, promociones) y la guardamos
        for F in (InicioPage, ReservarPage, AdminPage, PromocionesPage):
            frame = F(container, self)  # Creamos la pantalla
            self.frames[F.__name__] = frame  # La guardamos con su nombre
            frame.grid(row=0, column=0, sticky="nsew")  # Todas van en el mismo lugar para poder cambiar entre ellas

        # Mostramos la pantalla de inicio cuando la app arranca
        self.mostrar_frame("InicioPage")

    # Esta función sirve para cambiar la pantalla que se está viendo
    def mostrar_frame(self, nombre):
        frame = self.frames[nombre]  # Buscamos la pantalla que queremos mostrar
        frame.tkraise()  # La traemos al frente para que se vea

# Este es el inicio del programa
if __name__ == "__main__":
    app = CineApp()  # Creamos nuestra app
    app.mainloop()   # Hacemos que la ventana se quede abierta y funcione
