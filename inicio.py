# Importa tkinter para crear la interfaz gráfica
import tkinter as tk
# Importa PIL para manipular imágenes
from PIL import Image, ImageTk

# Clase que representa la página de inicio del sistema
class InicioPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#002f5e")  # Establece el fondo azul oscuro

        # ------------------ Barra de navegación superior ------------------
        navbar = tk.Frame(self, bg="#001f3f", height=80)
        navbar.pack(fill="x", side="top")  # Se extiende horizontalmente

        # Carga y ajusta el logo
        logo_img = Image.open("logo.jpg")
        logo_img = logo_img.resize((60, 60))
        self.logo = ImageTk.PhotoImage(logo_img)

        # Muestra el logo en la barra
        tk.Label(navbar, image=self.logo, bg="#001f3f").pack(side="left", padx=10)

        # Botones de navegación con texto y página destino
        nav_btns = [
            ("Reservar Boletos", "ReservarPage"),
            ("Administrar Funciones", "AdminPage"),
            ("Ver Promociones", "PromocionesPage")
        ]

        # Crea los botones en la barra
        for texto, destino in nav_btns:
            tk.Button(navbar, text=texto,
                      bg="#004080", fg="white",
                      font=("Arial", 10, "bold"),
                      bd=0,  # Sin borde
                      command=lambda name=destino: controller.mostrar_frame(name)
                      ).pack(side="left", padx=15)

        # ------------------ Sección principal ------------------
        centro = tk.Frame(self, bg="#002f5e")
        centro.pack(expand=True)

        # Título principal
        tk.Label(centro, text="CONSULTA DE FUNCIONES",
                 font=("Arial", 24, "bold"),
                 fg="white", bg="#002f5e").pack(pady=10)

        # Subtítulo explicativo
        tk.Label(centro, text="Selecciona una opción del menú superior para continuar",
                 font=("Arial", 14), fg="#cce7ff", bg="#002f5e").pack(pady=5)

        # Imagen decorativa central
        fondo_img = Image.open("fondo.png")
        fondo_img = fondo_img.resize((250, 250))
        self.fondo = ImageTk.PhotoImage(fondo_img)
        tk.Label(centro, image=self.fondo, bg="#002f5e").pack(pady=20)
