# Importamos lo necesario para crear la interfaz y manejar los datos
import tkinter as tk
from tkinter import messagebox
from datos import agregar_reserva, leer_datos, FUNCIONES_PATH, RESERVAS_PATH
from datetime import datetime

# Esta es la pantalla donde el usuario puede reservar boletos
class ReservarPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#002f5e")
        self.controller = controller

        # Título y subtítulo de la página
        tk.Label(self, text="Reservar Boletos", font=("Arial", 24, "bold"), fg="white", bg="#002f5e").pack(pady=20)
        tk.Label(self, text="Selecciona una película y horario disponible", font=("Arial", 14), fg="white", bg="#002f5e").pack(pady=10)

        # Aquí vamos a guardar la película y el horario que el usuario elija
        self.pelicula_var = tk.StringVar()
        self.funcion_var = tk.StringVar()

        # Menú para escoger una película
        tk.Label(self, text="Película:", font=("Arial", 12), fg="white", bg="#002f5e").pack()
        self.peliculas_menu = tk.OptionMenu(self, self.pelicula_var, "")
        self.peliculas_menu.pack()

        # Menú para escoger el horario
        tk.Label(self, text="Horario:", font=("Arial", 12), fg="white", bg="#002f5e").pack(pady=(10, 0))
        self.horarios_menu = tk.OptionMenu(self, self.funcion_var, "")
        self.horarios_menu.pack()

        # Título para los asientos
        tk.Label(self, text="Selecciona tus asientos:", font=("Arial", 12), fg="white", bg="#002f5e").pack(pady=15)
        asientos_frame = tk.Frame(self, bg="#002f5e")
        asientos_frame.pack()

        # Aquí vamos a crear los botones para los asientos (A1, A2... E5)
        self.asientos = {}
        for fila in range(5):
            for col in range(5):
                id_asiento = f"{chr(65+fila)}{col+1}"  # Nombres como A1, B3, etc.
                var = tk.IntVar()
                btn = tk.Checkbutton(
                    asientos_frame, text=id_asiento, variable=var,
                    bg="#002f5e", fg="white", selectcolor="green"
                )
                btn.grid(row=fila, column=col, padx=5, pady=5)
                self.asientos[id_asiento] = var

        # Botón para confirmar la reserva
        tk.Button(self, text="Confirmar Reserva", command=self.confirmar_reserva, bg="#00cc66", fg="white").pack(pady=20)

        # Botón para volver al menú principal
        tk.Button(self, text="Regresar al Inicio", command=lambda: controller.mostrar_frame("InicioPage"), bg="#004080", fg="white").pack(pady=10)

    # Esta función se encarga de cargar las películas, horarios y asientos cada vez que entras a esta pantalla
    def recargar_datos(self):
        funciones = leer_datos(FUNCIONES_PATH)  # Leemos las funciones disponibles

        # Sacamos los nombres de las películas y sus horarios
        peliculas = list(set(f["pelicula"] for f in funciones))
        horarios = {pelicula: [] for pelicula in peliculas}
        for funcion in funciones:
            horarios[funcion["pelicula"]].append(funcion["horario"])

        # Mostramos la primera película y horario por defecto
        self.pelicula_var.set(peliculas[0] if peliculas else "")
        self.funcion_var.set(horarios[self.pelicula_var.get()][0] if horarios.get(self.pelicula_var.get()) else "")

        # Actualizamos el menú de películas
        self.peliculas_menu['menu'].delete(0, 'end')
        for pelicula in peliculas:
            self.peliculas_menu['menu'].add_command(
                label=pelicula,
                command=lambda p=pelicula: self.actualizar_horarios(p, horarios)
            )

        # Actualizamos el menú de horarios
        self.horarios_menu['menu'].delete(0, 'end')
        for horario in horarios.get(self.pelicula_var.get(), []):
            self.horarios_menu['menu'].add_command(label=horario, command=tk._setit(self.funcion_var, horario))

        # Revisamos qué asientos ya están reservados
        self.deshabilitar_asientos_reservados()

    # Cuando se cambia la película, se actualizan los horarios correspondientes
    def actualizar_horarios(self, pelicula, horarios):
        self.pelicula_var.set(pelicula)
        self.funcion_var.set(horarios[pelicula][0])  # Ponemos el primer horario

        self.horarios_menu['menu'].delete(0, 'end')
        for horario in horarios[pelicula]:
            self.horarios_menu['menu'].add_command(label=horario, command=tk._setit(self.funcion_var, horario))

        self.deshabilitar_asientos_reservados()

    # Esta función desactiva los asientos que ya están reservados
    def deshabilitar_asientos_reservados(self):
        reservas = leer_datos(RESERVAS_PATH)
        reservas_hechas = [(r["pelicula"], r["horario"], r["asientos"]) for r in reservas]

        for asiento_id, var in self.asientos.items():
            reservado = any(
                asiento_id in asientos for pelicula, horario, asientos in reservas_hechas
                if self.pelicula_var.get() == pelicula and self.funcion_var.get() == horario
            )

            for widget in self.winfo_children():
                if isinstance(widget, tk.Frame):
                    for btn in widget.winfo_children():
                        if isinstance(btn, tk.Checkbutton) and btn.cget("text") == asiento_id:
                            if reservado:
                                var.set(0)
                                btn.config(state="disabled")  # No se puede elegir
                            else:
                                btn.config(state="normal")  # Disponible

    # Esta función guarda la reserva cuando el usuario confirma
    def confirmar_reserva(self):
        pelicula = self.pelicula_var.get()
        horario = self.funcion_var.get()
        asientos = [id for id, var in self.asientos.items() if var.get() == 1]

        if pelicula and horario and asientos:
            agregar_reserva(pelicula, horario, asientos)
            messagebox.showinfo("Reserva Confirmada", "Se ha generado un archivo de reserva.")

    # Cada vez que esta pantalla se muestra, actualizamos los datos
    def tkraise(self, aboveThis=None):
        super().tkraise(aboveThis)
        self.recargar_datos()
