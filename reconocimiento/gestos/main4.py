import cv2
import mediapipe as mp
import webbrowser
import math
import pyautogui

# Inicializar el módulo de MediaPipe Hands y Face
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_detection
hands = mp_hands.Hands()
face = mp_face.FaceDetection(min_detection_confidence=0.3)

# Configuración de la cámara
cap = cv2.VideoCapture(0)
width, height = 640, 480
cap.set(3, width)
cap.set(4, height)

# Variable para almacenar la URL de la página abierta y controlar si ya se abrió YouTube
current_url = None
youtube_opened = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el marco de BGR a RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Obtener los resultados de la detección de manos
    results_hands = hands.process(rgb_frame)

    # Obtener los resultados de la detección de rostros
    results_face = face.process(rgb_frame)

    # Verificar si se detecta alguna mano
    if results_hands.multi_hand_landmarks:
        # Obtener la primera mano detectada
        hand_landmarks = results_hands.multi_hand_landmarks[0]

        # Obtener la posición vertical y horizontal de la punta del pulgar
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)

        # Obtener la posición vertical de la punta del índice
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

        # Calcular la distancia entre los puntos de referencia del pulgar e índice
        distance = math.sqrt((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2)

        # Verificar el control del slider
        if thumb_y < 100:
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), -1)  # Dibujar un círculo en la muñeca
            cv2.putText(frame, "Movimiento hacia arriba (Control del slider)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            pyautogui.press('down')  # Simula pulsar la tecla "abajo" para desplazarse hacia abajo
        elif thumb_y > 300:
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), -1)  # Dibujar un círculo en la muñeca
            cv2.putText(frame, "Movimiento hacia abajo (Control del slider)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            pyautogui.press('up')  # Simula pulsar la tecla "arriba" para desplazarse hacia arriba

    # Mostrar el marco con la detección
    cv2.imshow('Hand Detection', frame)

    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
