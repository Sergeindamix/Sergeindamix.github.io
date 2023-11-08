import tkinter as tk
import gdown
import os
import json
import re

# Definir una función para limpiar el nombre del archivo
def limpiar_nombre_archivo(nombre):
    # Eliminar caracteres inválidos para el sistema de archivos
    nombre_limpio = re.sub(r'[\/:*?"<>|]', '', nombre)
    return nombre_limpio

# Definir una función para extraer el ID del enlace de Google Drive
def obtener_id_desde_enlace(link):
    # Buscar el ID en el enlace proporcionado
    match = re.search(r"/file/d/([^/]+)/", link)
    if match:
        return match.group(1)
    return None

# Definir una función para descargar un archivo desde Google Drive usando el ID
def descargar_desde_google_drive(id, nombre_archivo):
    nombre_archivo_limpio = limpiar_nombre_archivo(nombre_archivo)
    gdown.download(f"https://drive.google.com/uc?id={id}", nombre_archivo_limpio, quiet=False)

# Crear la función para descargar la selección
def descargar_seleccion():
    seleccion = lista_desplegable.get()
    
    # Obtener el elemento seleccionado del diccionario de videos
    for video in videos:
        if video["name"] == seleccion:
            item = video
            break
    else:
        return  # Salir si no se encuentra la selección
    
    nombre_archivo = item["name"]
    link = item["link"]
    
    # Obtener el ID del enlace de Google Drive
    id_drive = obtener_id_desde_enlace(link)
    
    if id_drive is not None:
        if os.path.exists(limpiar_nombre_archivo(nombre_archivo)):
            respuesta = input(f"'{nombre_archivo}' ya existe. ¿Deseas descargarlo de nuevo? (Sí/No): ").strip().lower()
            if respuesta != "si":
                return
        descargar_desde_google_drive(id_drive, nombre_archivo)
        mensaje.config(text=f"Descargado: {nombre_archivo}")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Descargar Videos")

# Cargar datos desde el archivo JSON
with open("videos.json", "r") as json_file:
    videos = json.load(json_file)

# Crear una lista desplegable con los nombres de los videos
etiqueta = tk.Label(ventana, text="Selecciona un video:")
etiqueta.pack()
lista_desplegable = tk.StringVar(ventana)
lista_desplegable.set(videos[0]["name"])
menu = tk.OptionMenu(ventana, lista_desplegable, *[item["name"] for item in videos])
menu.pack()

# Crear un botón para descargar
boton_descargar = tk.Button(ventana, text="Descargar Seleccion", command=descargar_seleccion)
boton_descargar.pack()

# Crear una etiqueta para mostrar el resultado de la descarga
mensaje = tk.Label(ventana, text="")
mensaje.pack()

# Iniciar la aplicación
ventana.mainloop()
