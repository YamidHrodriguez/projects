import cv2
import numpy as np
import tkinter as tk
from tkinter import Label

def extraer_paleta(imagen_path, k=5):
    # Cargar la imagen
    imagen = cv2.imread(imagen_path)
    
    # Verificar si la imagen se cargó correctamente
    if imagen is None:
        print(f"No se pudo cargar la imagen desde la ruta: {imagen_path}")
        return

    # Convertir la imagen de BGR a RGB
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

    # Reshape de la imagen para aplicar k-means
    pixeles = imagen_rgb.reshape((-1, 3))

    # Convertir los píxeles a tipo flotante para k-means
    pixeles = np.float32(pixeles)

    # Especificar criterios y aplicar k-means
    criterios = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, etiquetas, centros = cv2.kmeans(pixeles, k, None, criterios, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convertir los centros a valores enteros
    centros = np.uint8(centros)

    # Crear una ventana de Tkinter
    root = tk.Tk()
    root.title('Códigos de Color')

    # Mostrar los cuadros de color y códigos en la ventana
    for i, color in enumerate(centros):
        color_str = f"Color {i + 1}: #{color[0]:02X}{color[1]:02X}{color[2]:02X}"

        # Crear un lienzo con el color
        canvas = tk.Canvas(root, width=50, height=50, bg=f"#{color[0]:02X}{color[1]:02X}{color[2]:02X}")
        canvas.pack()

        # Mostrar el código de color
        label = Label(root, text=color_str, font=("Arial", 12))
        label.pack()

    # Bucle principal de la aplicación Tkinter
    root.mainloop()

# Ruta completa de la imagen que deseas procesar
ruta_imagen = 'C:/Users/Sena/Downloads/archivos/jpg/michi.jpg'  # Cambia esto a la ruta correcta

# Número de colores en la paleta
numero_colores = 10

# Extraer la paleta de colores y mostrar visualmente los códigos en una interfaz gráfica
extraer_paleta(ruta_imagen, numero_colores)
