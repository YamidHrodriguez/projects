import cv2

# Carga el clasificador de rostros preentrenado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Carga el clasificador de sonrisas preentrenado
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
# Carga el clasificador de ojos preentrenado
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Abre la cámara
cap = cv2.VideoCapture(0)

# Verifica si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error al abrir la cámara")
    exit()

while True:
    # Lee el fotograma de la cámara
    ret, frame = cap.read()

    # Convierte la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostros en la imagen
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Dibuja un rectángulo alrededor del rostro
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Extrae la región de interés (ROI) que contiene el rostro
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detecta ojos en la región del rostro
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # Verifica la posición de los ojos para determinar si la persona mira hacia la derecha
        for (ex, ey, ew, eh) in eyes:
            eye_center_x = x + ex + ew // 2
            eye_center_y = y + ey + eh // 2
            cv2.circle(frame, (eye_center_x, eye_center_y), 2, (0, 255, 0), 2)
            
            if eye_center_x > x + w // 2:  # Si el centro del ojo está a la derecha del centro del rostro
                print("¡Mirando hacia la derecha!")

        # Detecta sonrisas en la región del rostro
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))

        for (sx, sy, sw, sh) in smiles:
            # Dibuja un rectángulo alrededor de la sonrisa
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
            print("¡Sonrisa detectada!")

    # Muestra la transmisión en tiempo real con los rectángulos alrededor de los rostros y sonrisas
    cv2.imshow('Detección de Sonrisas y Mirada', frame)

    # Sale del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()
