# import webbrowser
# Ejecutar la tarea a las 2:26 AM
import schedule
import pygame
import time

def tarea_especifica():
    print("Tarea ejecutada a las 2:58 am")
    
    def reproducir_alarma():
        pygame.init()
        pygame.mixer.music.load("emociones\human-tetris.wav")  # Reemplaza con la ruta de tu archivo de sonido
        pygame.mixer.music.play()

# Llamar a la función para sonar la alarma
    reproducir_alarma()

    # url_facebook = "https://www.facebook.com"
    # webbrowser.open(url_facebook)
    
    

# Ejecutar la tarea a las 2:26 AM
schedule.every().day.at("02:58").do(tarea_especifica)

while True:
    schedule.run_pending()
    time.sleep(1)
