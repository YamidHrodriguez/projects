import pyautogui
import cv2
import numpy as np

# Configuración de la grabación
SCREEN_SIZE = (1920, 1080)
OUTPUT_FILE = 'screen_record.mp4'
FPS = 30.0

# Configuración de la grabación de pantalla
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(OUTPUT_FILE, fourcc, FPS, SCREEN_SIZE)

try:
    while True:
        # Captura de pantalla y conversión a formato de imagen
        screen = pyautogui.screenshot()
        frame = np.array(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Grabar el fotograma en el archivo de salida
        out.write(frame)

except KeyboardInterrupt:
    # Detener la grabación al presionar Ctrl+C
    pass

finally:
    # Liberar recursos
    out.release()
    cv2.destroyAllWindows()
