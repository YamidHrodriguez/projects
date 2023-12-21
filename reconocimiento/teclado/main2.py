import keyboard
import webbrowser

def abrir_facebook():
    url = "https://www.facebook.com"
    webbrowser.open(url)

def realizar_accion():
    print("Acción realizada: Abrir Facebook") # Agrega aquí la lógica para realizar la acción que desees al escribir "facebook"
    abrir_facebook()

teclas_facebook = ["f", "a", "c", "e"]

teclas_pulsadas = []
print("Presiona las teclas para formar la palabra:")

while True:
    evento = keyboard.read_event(suppress=True)
    
    if evento.event_type == keyboard.KEY_DOWN:
        if evento.name == "enter":
            break  # Sal del bucle si se presiona la tecla "Enter"
        elif evento.name == "backspace":
            teclas_pulsadas = teclas_pulsadas[:-1]  # Elimina el último carácter si se presiona la tecla "Backspace"
        else:
            teclas_pulsadas.append(evento.name)

    # Verifica si se ha ingresado la secuencia de teclas correspondiente a "facebook"
    if teclas_pulsadas == teclas_facebook:
        realizar_accion()
        teclas_pulsadas = []  # Reinicia la lista de teclas después de realizar la acción
