# Importamos Tkinter y las funciones que manejan los datos
import tkinter as tk
from datos import agregar_funcion, leer_datos, editar_funcion, eliminar_funcion, agregar_promocion, FUNCIONES_PATH, PROMOS_PATH

# Esta clase representa la página de administración para gestionar funciones y promociones
class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#002f5e")
        self.controller = controller  # Sirve para cambiar entre pantallas

        # Creamos un canvas con scroll para poder movernos si hay mucho contenido
        canvas = tk.Canvas(self, bg="#002f5e", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg="#002f5e")

        # Hace que el scroll se ajuste al contenido automáticamente
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Insertamos el contenido dentro del canvas
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Mostramos el canvas y el scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Título de la sección
        tk.Label(self.scrollable_frame, text="Administrar Funciones", font=("Arial", 24, "bold"),
                 fg="white", bg="#002f5e").pack(pady=10)

        # Campos de entrada para agregar o editar funciones
        self.entries = {}
        for field in ["Película", "Horario", "Sala"]:
            tk.Label(self.scrollable_frame, text=field, font=("Arial", 12), fg="white", bg="#002f5e").pack()
            entry = tk.Entry(self.scrollable_frame)
            entry.pack()
            self.entries[field.lower()] = entry  # Guardamos las entradas con claves en minúscula

        # Botones para acciones sobre las funciones
        tk.Button(self.scrollable_frame, text="Agregar Función", command=self.guardar_funcion,
                  bg="#004080", fg="white").pack(pady=5)
        tk.Button(self.scrollable_frame, text="Editar Función Seleccionada", command=self.editar_funcion,
                  bg="#004080", fg="white").pack(pady=5)
        tk.Button(self.scrollable_frame, text="Eliminar Función Seleccionada", command=self.eliminar_funcion,
                  bg="#004080", fg="white").pack(pady=5)

        # Lista para mostrar todas las funciones existentes
        self.lista_funciones = tk.Listbox(self.scrollable_frame, width=80)
        self.lista_funciones.pack(pady=10)

        # Sección para agregar promociones
        tk.Label(self.scrollable_frame, text="Nueva Promoción", font=("Arial", 14, "bold"),
                 fg="white", bg="#002f5e").pack(pady=10)
        self.promo_entry = tk.Entry(self.scrollable_frame, width=50)
        self.promo_entry.pack()
        tk.Button(self.scrollable_frame, text="Agregar Promoción", command=self.guardar_promocion,
                  bg="#004080", fg="white").pack(pady=5)

        # Botón para regresar a la pantalla principal
        tk.Button(self.scrollable_frame, text="Regresar al Inicio",
                  command=lambda: controller.mostrar_frame("InicioPage"),
                  bg="#004080", fg="white").pack(pady=5)

        # Al cargar esta página, se muestran los datos actuales
        self.recargar_datos()

    # Guarda una nueva función en el sistema
    def guardar_funcion(self):
        pelicula = self.entries["película"].get()
        horario = self.entries["horario"].get()
        sala = self.entries["sala"].get()
        if pelicula and horario and sala:
            agregar_funcion(pelicula, horario, sala)
            self.recargar_datos()

    # Edita los datos de la función seleccionada en la lista
    def editar_funcion(self):
        sel = self.lista_funciones.curselection()
        if sel:
            index = sel[0]
            pelicula = self.entries["película"].get()
            horario = self.entries["horario"].get()
            sala = self.entries["sala"].get()
            editar_funcion(index, {"pelicula": pelicula, "horario": horario, "sala": sala})
            self.recargar_datos()

    # Elimina la función seleccionada de la lista
    def eliminar_funcion(self):
        sel = self.lista_funciones.curselection()
        if sel:
            eliminar_funcion(sel[0])
            self.recargar_datos()

    # Guarda el texto que el usuario escribió como promoción
    def guardar_promocion(self):
        texto = self.promo_entry.get()
        if texto:
            agregar_promocion(texto)
            self.promo_entry.delete(0, tk.END)

    # Carga todas las funciones desde el archivo y las muestra en la lista
    def recargar_datos(self):
        self.lista_funciones.delete(0, tk.END)
        for f in leer_datos(FUNCIONES_PATH):
            self.lista_funciones.insert(tk.END, f"{f['pelicula']} - {f['horario']} - Sala {f['sala']}")
