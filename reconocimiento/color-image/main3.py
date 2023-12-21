import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

def categorizar_color(color):
    luminancia = (0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]) / 255.0
    return "Oscuro" if luminancia < 0.5 else "Claro"

def extraer_paleta_desde_video(numero_colores=5):
    root = tk.Tk()
    root.title('Stream de Video y Categorización de Colores')

    lienzo_video = tk.Canvas(root, width=640, height=480)
    lienzo_video.pack()

    lienzo_paleta = tk.Canvas(root, width=640, height=100)
    lienzo_paleta.pack()

    captura = cv2.VideoCapture(0)

    while True:
        ret, frame = captura.read()

        if not ret:
            print("Error al capturar el fotograma.")
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pixeles = frame_rgb.reshape((-1, 3))
        pixeles = np.float32(pixeles)

        criterios = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, etiquetas, centros = cv2.kmeans(pixeles, numero_colores, None, criterios, 10, cv2.KMEANS_RANDOM_CENTERS)

        centros = np.uint8(centros)

        img = Image.fromarray(frame_rgb)
        img = ImageTk.PhotoImage(img)
        lienzo_video.delete("all")
        lienzo_video.create_image(0, 0, anchor=tk.NW, image=img)

        lienzo_paleta.delete("all")

        # Calcular el ancho total necesario para las paletas
        ancho_total = numero_colores * 70

        for i, color in enumerate(centros):
            color_str = f"Color {i + 1}: \n#{color[0]:02X}{color[1]:02X}{color[2]:02X}"
            categoria = categorizar_color(color)

            # Calcular la posición x para cada paleta de color
            x_position = (640 - ancho_total) // 2 + i * 70

            lienzo_paleta.create_rectangle(x_position, 10, x_position + 60, 90,
                                          fill=f"#{color[0]:02X}{color[1]:02X}{color[2]:02X}")

            label_color = tk.Label(root, text=color_str, font=("Arial", 10))
            lienzo_paleta.create_window(x_position + 50, 40, window=label_color)

            label_categoria = tk.Label(root, text=categoria, font=("Arial", 10))
            lienzo_paleta.create_window(x_position + 50, 70, window=label_categoria)

        root.update_idletasks()
        root.update()

    captura.release()
    cv2.destroyAllWindows()

numero_colores = 7
extraer_paleta_desde_video(numero_colores)
