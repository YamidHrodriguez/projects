import keyboard
import webbrowser

def abrir_google():
    url = "https://www.google.com"
    webbrowser.open(url)

def abrir_youtube():
    url = "https://www.youtube.com"
    webbrowser.open(url)

def abrir_facebook():
    url = "https://www.facebook.com"
    webbrowser.open(url)

# Define las teclas de activación para cada acción
tecla_google = "ctrl+alt+g"
tecla_youtube = "ctrl+alt+y"
tecla_facebook = "ctrl+alt+"

# Asigna las funciones a las teclas correspondientes
keyboard.add_hotkey(tecla_google, abrir_google)
keyboard.add_hotkey(tecla_youtube, abrir_youtube)

# Mantén el script en ejecución
keyboard.wait("esc")
