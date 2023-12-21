import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

def extraer_paleta_desde_video(numero_colores=5):
    # Crear una ventana de Tkinter
    root = tk.Tk()
    root.title('Stream de Video y Códigos de Color')

    # Crear un lienzo para el stream de video
    lienzo_video = tk.Canvas(root, width=640, height=480)
    lienzo_video.pack()

    # Crear un lienzo para la paleta de colores
    lienzo_paleta = tk.Canvas(root, width=300, height=480)
    lienzo_paleta.pack(side=tk.RIGHT)

    # Inicializar la cámara (0 indica la cámara predeterminada)
    captura = cv2.VideoCapture(0)

    # Bucle para capturar y procesar cada fotograma
    while True:
        # Capturar un fotograma
        ret, frame = captura.read()

        # Verificar si la captura fue exitosa
        if not ret:
            print("Error al capturar el fotograma.")
            break

        # Convertir el fotograma de BGR a RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Reshape del fotograma para aplicar k-means
        pixeles = frame_rgb.reshape((-1, 3))

        # Convertir los píxeles a tipo flotante para k-means
        pixeles = np.float32(pixeles)

        # Especificar criterios y aplicar k-means
        criterios = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, etiquetas, centros = cv2.kmeans(pixeles, numero_colores, None, criterios, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Convertir los centros a valores enteros
        centros = np.uint8(centros)

        # Mostrar el stream de video en el lienzo correspondiente
        img = Image.fromarray(frame_rgb)
        img = ImageTk.PhotoImage(img)
        lienzo_video.delete("all")
        lienzo_video.create_image(0, 0, anchor=tk.NW, image=img)

        # Limpiar la ventana Tkinter antes de actualizar los colores
        lienzo_paleta.delete("all")

        # Mostrar los cuadros de color y códigos en la ventana
        for i, color in enumerate(centros):
            color_str = f"Color {i + 1}: #{color[0]:02X}{color[1]:02X}{color[2]:02X}"

            # Crear un lienzo con el color
            lienzo_paleta.create_rectangle(10, i * 50, 60, (i + 1) * 50, fill=f"#{color[0]:02X}{color[1]:02X}{color[2]:02X}")

            # Mostrar el código de color
            label = tk.Label(root, text=color_str, font=("Arial", 12))
            lienzo_paleta.create_window(150, i * 50 + 25, window=label)

        # Actualizar la ventana de Tkinter
        root.update_idletasks()
        root.update()

    # Liberar los recursos al salir
    captura.release()
    cv2.destroyAllWindows()

# Número de colores en la paleta
numero_colores = 5

# Llamar a la función para extraer la paleta desde la transmisión de video
extraer_paleta_desde_video(numero_colores)
