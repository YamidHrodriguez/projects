import cv2
import mediapipe as mp
import pyautogui

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Parámetros para la detección de movimiento
umbral_movimiento = 50  # Umbral de movimiento para la detección de gestos

while True:
    # Capturar el fotograma actual
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el fotograma a escala de grises
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Obtener resultados de la detección de manos
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        # Obtener la posición de la muñeca de la primera mano detectada
        hand_landmarks = results.multi_hand_landmarks[0]
        x, y = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * frame.shape[1]), int(
            hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * frame.shape[0])

        # Dibujar un círculo en la posición de la muñeca
        cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

        # Detectar movimiento de la mano
        if y < frame.shape[0] / 2 - umbral_movimiento:
            pyautogui.scroll(1)  # Desplazamiento hacia abajo
        elif y > frame.shape[0] / 2 + umbral_movimiento:
            pyautogui.scroll(-1)  # Desplazamiento hacia arriba

    # Mostrar la imagen en una ventana
    cv2.imshow('Detección de Movimiento', frame)

    # Salir del bucle cuando se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
