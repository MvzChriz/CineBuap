
# Cine BUAP - Un sistema de cine con funcionalidades de reservar y ver promociones :P

Este es un sistema para gestionar funciones de cine, realizar reservas de boletos y visualizar promociones. Está diseñado para ser fácil de usar y proporciona una interfaz grafica basada en `tkinter` con una interfaz similar a la de la BUAP (Me quede sin ideas).

## Requisitos para correr el programa :D

- Python 3.x
- Bibliotecas de Python:
  - `tkinter`
  - `Pillow` (para manejo de imagenes)

Instalar `Pillow`:

```bash
pip install pillow
```

## Estructura del Sistema ✌️ 

- `CineApp.py`: El archivo principal que ejecuta la aplicacion.
- `inicio.py`: Pagina de inicio con opciones de navegacion que contiene el menu de opciones.
- `reservar.py`: Pagina para realizar reservas de boletos y ver funciones disponibles.
- `admin.py`: Pagina para administrar funciones y promociones permitiendo registrar,editar o borrar registros.
- `promociones.py`: Pagina para mostrar las promociones actuales.
- `datos.py`: Funciones para manipular archivos JSON con funciones, reservas y promociones y que son llamadas en cada modulo dependiendo cual se use.
- Archivos de datos:
  - `funciones.json`: Datos de las funciones de cine (peliculas, horarios, salas).
  - `reservas.json`: Datos de las reservas realizadas.
  - `promociones.json`: Datos de las promociones activas.
- Archivos de imagen:
  - `logo.jpg`: Logo de la pagina (Logo de la BUAP).
  - `fondo.png`: Imagen de fondo de la página de inicio (Una sala de cine).

## Funcionalidades

### Pagina de Inicio (`InicioPage`)

- Muestra un menu de navegacion con las opciones:
  - **Reservar Boletos**: Permite a los usuarios realizar reservas de boletos.
  - **Administrar Funciones**: Permite a los administradores agregar, editar y eliminar funciones de cine.
  - **Ver Promociones**: Muestra una lista de las promociones activas.

### Pagina de Reservas (`ReservarPage`)

- Permite a los usuarios seleccionar una pelicula, horario y asientos disponibles.
- Los asientos reservados se deshabilitan para evitar reservas duplicadas.
- Una vez confirmada la reserva, se guarda un archivo de texto con los detalles de la reserva.

### Pagina de Administracion (`AdminPage`)

- Permite a los administradores agregar, editar y eliminar funciones de cine.
- Los administradores tambien pueden agregar nuevas promociones.
- Las funciones se guardan en un archivo JSON (`funciones.json`), y las promociones se guardan en `promociones.json`.

### Pagina de Promociones (`PromocionesPage`)

- Muestra una lista de las promociones actuales, cargadas desde un archivo JSON (`promociones.json`).

## Archivos y Datos

### `funciones.json`

Este archivo contiene las funciones de cine, con los siguientes campos:

- `pelicula`: Nombre de la pelicula.
- `horario`: Hora de la funcin.
- `sala`: Sala donde se proyecta la pelicula.

Ejemplo de contenido:

```json
[
  {"pelicula": "Cars", "horario": "14:00", "sala": "A1"},
  {"pelicula": "Cars 2", "horario": "16:00", "sala": "A2"}
]
```

### `reservas.json`

Este archivo contiene las reservas realizadas, con los siguientes campos:

- `pelicula`: Nombre de la pelicula reservada.
- `horario`: Hora de la funcion reservada.
- `asientos`: Lista de asientos reservados.
- `fecha`: Fecha y hora de la reserva.

Ejemplo de contenido:

```json
[
  {"pelicula": "Cars ", "horario": "14:00", "asientos": ["A1", "A2"], "fecha": "2025-05-01T14:00:00"}
]
```

### `promociones.json`

Este archivo contiene las promociones activas, con el siguiente formato:

```json
[
  "Promoción 1: Gratis para los lobosbuap",
  "Promoción 2: 30% menos con credencial estudiantil"
]
```

## Ejecución

Para ejecutar el sistema, simplemente corre el archivo `CineApp.py`:

```bash
python CineApp.py
```

## Creditos

-Cristian Emilio Muñoz Vazquez - Alumno de la Benemerita Universidad Autonoma de Puebla
