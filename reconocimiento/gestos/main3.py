import cv2
import mediapipe as mp
import webbrowser

# Inicializar el módulo de MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Configuración de la cámara
cap = cv2.VideoCapture(0)
width, height = 640, 480
cap.set(3, width)
cap.set(4, height)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el marco de BGR a RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Obtener los resultados de la detección de manos
    results = hands.process(rgb_frame)

    # Verificar si se detecta alguna mano
    if results.multi_hand_landmarks:
        # Iterar sobre las manos detectadas
        for hand_landmarks in results.multi_hand_landmarks:
            # Obtener la posición vertical y horizontal de la punta del pulgar
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_x = int(thumb_tip.x * width)
            thumb_y = int(thumb_tip.y * height)
            # Verificar la posición vertical para YouTube
            if thumb_y < 100:
                cv2.putText(frame, "Hacia arriba (YouTube)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                webbrowser.open("https://www.youtube.com")

            # Verificar la posición horizontal para Facebook
            elif thumb_x < 200:
                cv2.putText(frame, "Hacia la izquierda (Facebook)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                webbrowser.open("https://www.facebook.com")

            # Verificar la posición horizontal para Twitter
            elif thumb_x > 400:
                cv2.putText(frame, "Hacia la derecha (Twitter)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                webbrowser.open("https://www.twitter.com")

    # Mostrar el marco con la detección
    cv2.imshow('Hand Detection', frame)

    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()

