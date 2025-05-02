# Importamos las librerías necesarias
import json
import os
from datetime import datetime

# Definimos las rutas de los archivos JSON que vamos a usar para guardar información
FUNCIONES_PATH = "funciones.json"
RESERVAS_PATH = "reservas.json"
PROMOS_PATH = "promociones.json"

# ---------- Funciones genéricas ----------

# Esta función lee datos desde un archivo JSON.
# Si el archivo no existe, devuelve una lista vacía.
def leer_datos(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as file:
        return json.load(file)

# Esta función guarda una lista de datos en un archivo JSON.
# Los datos se guardan con formato bonito (indentado).
def guardar_datos(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)

# ---------- Funciones relacionadas con funciones de cine ----------

# Agrega una nueva función de cine al archivo de funciones
def agregar_funcion(pelicula, horario, sala):
    funciones = leer_datos(FUNCIONES_PATH)  # Cargamos las funciones actuales
    funciones.append({
        "pelicula": pelicula,
        "horario": horario,
        "sala": sala
    })  # Agregamos la nueva función
    guardar_datos(FUNCIONES_PATH, funciones)  # Guardamos la lista actualizada

# Reemplaza los datos de una función existente en base a su índice
def editar_funcion(index, nueva_funcion):
    funciones = leer_datos(FUNCIONES_PATH)
    funciones[index] = nueva_funcion  # Sobrescribe la función en esa posición
    guardar_datos(FUNCIONES_PATH, funciones)

# Elimina una función del archivo según su posición en la lista
def eliminar_funcion(index):
    funciones = leer_datos(FUNCIONES_PATH)
    if 0 <= index < len(funciones):  # Validamos que el índice sea válido
        funciones.pop(index)  # Eliminamos la función
        guardar_datos(FUNCIONES_PATH, funciones)

# ---------- Funciones para manejar reservas ----------

# Agrega una reserva y crea un comprobante en un archivo de texto
def agregar_reserva(pelicula, horario, asientos):
    reservas = leer_datos(RESERVAS_PATH)
    reserva = {
        "pelicula": pelicula,
        "horario": horario,
        "asientos": asientos,
        "fecha": datetime.now().isoformat()  # Fecha y hora actual
    }
    reservas.append(reserva)
    guardar_datos(RESERVAS_PATH, reservas)

    # También crea un archivo de texto con los datos de la reserva
    with open(f"reserva_{pelicula}_{horario.replace(':','')}.txt", "w", encoding="utf-8") as f:
        f.write(f"Película: {pelicula}\n")
        f.write(f"Horario: {horario}\n")
        f.write(f"Asientos: {', '.join(asientos)}\n")
        f.write(f"Fecha de reserva: {reserva['fecha']}\n")

# ---------- Funciones para promociones ----------

# Agrega una promoción nueva al archivo de promociones
def agregar_promocion(texto):
    promociones = leer_datos(PROMOS_PATH)
    promociones.append(texto)  # Añade el texto de la promoción
    guardar_datos(PROMOS_PATH, promociones)
