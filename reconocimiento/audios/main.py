import speech_recognition as sr

def detectar_palabras_clave(audio_file_path, palabras_clave):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as audio_file:
        audio = recognizer.record(audio_file)

    try:
        texto = recognizer.recognize_google(audio, language="es-ES")  # Puedes cambiar el idioma según tus necesidades
        print("Texto detectado: {}".format(texto))

        for palabra_clave in palabras_clave:
            if palabra_clave.lower() in texto.lower():
                print("Palabra clave encontrada: {}".format(palabra_clave))
        
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")
    except sr.RequestError as e:
        print("Error en la solicitud al servicio de reconocimiento de voz: {}".format(e))

if __name__ == "__main__":
    archivo_audio = "audios/Grabación-_2_.wav"  # Reemplaza con la ruta de tu archivo de audio
    palabras_clave = ["hola mundo", "jesucristo", "1914"]  # Reemplaza con tus palabras clave

    detectar_palabras_clave(archivo_audio, palabras_clave)
