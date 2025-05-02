# Importa tkinter para crear la interfaz y la función para leer promociones
import tkinter as tk
from datos import leer_datos, PROMOS_PATH

# Clase que representa la página de promociones
class PromocionesPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#002f5e")  # Fondo azul oscuro para toda la página

        # Contenedor principal para agrupar las promociones
        self.promos_frame = tk.Frame(self, bg="#002f5e")
        self.promos_frame.pack()

        # Título de la página
        tk.Label(self, text="Promociones Actuales", font=("Arial", 24, "bold"),
                 fg="white", bg="#002f5e").pack(pady=20)

        # Frame que contiene la lista de promociones y el scrollbar
        self.lista_frame = tk.Frame(self, bg="#002f5e")
        self.lista_frame.pack(fill="both", expand=True)

        # Scrollbar vertical
        self.scrollbar = tk.Scrollbar(self.lista_frame)
        self.scrollbar.pack(side="right", fill="y")

        # Lista donde se muestran las promociones
        self.lista = tk.Listbox(
            self.lista_frame,
            width=60,
            height=15,
            yscrollcommand=self.scrollbar.set,
            bg="#002f5e",       # Mismo fondo que la página
            fg="#cce7ff",       # Texto en azul claro
            font=("Arial", 14)
        )
        self.lista.pack(side="left", fill="both", expand=True)

        # Conecta la scrollbar con la lista
        self.scrollbar.config(command=self.lista.yview)

        # Botón para regresar a la página de inicio
        tk.Button(self, text="Regresar al Inicio",
                  command=lambda: controller.mostrar_frame("InicioPage"),
                  bg="#004080", fg="white").pack(pady=10)

        # Carga las promociones desde el archivo al iniciar la página
        self.recargar_datos()

    # Esta función recarga los datos desde el archivo de promociones
    def recargar_datos(self):
        self.lista.delete(0, tk.END)  # Borra lo que ya esté en la lista
        promociones = leer_datos(PROMOS_PATH)  # Lee las promociones guardadas
        for promo in promociones:
            self.lista.insert(tk.END, promo)  # Agrega cada una a la lista visual

    # Se llama automáticamente cuando esta página se muestra en pantalla
    def tkraise(self, aboveThis=None):
        super().tkraise(aboveThis)
        self.recargar_datos()  # Asegura que se actualicen los datos al cambiar de página
