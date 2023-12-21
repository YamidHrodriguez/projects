import speech_recognition as sr
import webbrowser

def reconocer_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Utiliza la API de reconocimiento de voz de Google en español
        texto = recognizer.recognize_google(audio, language="es-ES")
        print(f"\rHas dicho: {texto}", end='', flush=True)
        return texto.lower()
    except sr.UnknownValueError:
        print(" ")
        return ""
    except sr.RequestError as e:
        print("Error en la solicitud al servicio de reconocimiento de voz de Google; {0}".format(e))
        return ""

def main():
    while True:
        entrada = reconocer_audio()

        if "google" in entrada:
            print("Abriendo Google...")
            webbrowser.open("\rhttps://www.google.com")
        elif "gmail" in entrada:
            print("Abriendo gmail...")
            webbrowser.open("\rhttps://www.gmail.com")
        elif "facebook" in entrada:
            print("Abriendo Facebook...")
            webbrowser.open("\rhttps://www.facebook.com")

if __name__ == "__main__":
    main()
