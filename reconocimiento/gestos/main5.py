import cv2
import webbrowser
import numpy as np
import pyautogui
import mediapipe as mp

# Inicializar el módulo de MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Configuración de la cámara
cap = cv2.VideoCapture(0)
width, height = 640, 480
cap.set(3, width)
cap.set(4, height)

# Convertir colores RGB a HSV
color1_rgb = np.uint8([[[250, 204, 62]]])  # #FACC3E en RGB
color2_rgb = np.uint8([[[250, 208, 59]]])  # #FAD03B en RGB
color1_hsv = cv2.cvtColor(color1_rgb, cv2.COLOR_BGR2HSV)[0][0]
color2_hsv = cv2.cvtColor(color2_rgb, cv2.COLOR_BGR2HSV)[0][0]

# Rangos de color para los colores específicos en HSV
lower_color1 = np.array([color1_hsv[0] - 10, 100, 100])
upper_color1 = np.array([color1_hsv[0] + 10, 255, 255])

lower_color2 = np.array([color2_hsv[0] - 10, 100, 100])
upper_color2 = np.array([color2_hsv[0] + 10, 255, 255])

# Rango de color para el objeto de color rosado (ajusta estos valores según tus necesidades)
lower_pink = np.array([140, 100, 100])
upper_pink = np.array([180, 255, 255])

# Variable de control para asegurar que la página solo se cierre una vez
facebook_opened = False
close_page = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el marco de BGR a RGB para mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detección de gestos con la mano
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)

            # Verificar si el pulgar está arriba
            if thumb_y < height // 2:
                cv2.putText(frame, "Pulgar Arriba - Cerrar Página", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                pyautogui.hotkey('ctrl', 'w')
                close_page = True

            # Verificar el movimiento horizontal del pulgar
            if thumb_x > width // 2:
                cv2.putText(frame, "Movimiento hacia la derecha - Bajar", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                pyautogui.press('down')  # Simula pulsar la tecla "abajo" para desplazarse hacia abajo
            elif thumb_x < width // 2:
                cv2.putText(frame, "Movimiento hacia la izquierda - Subir", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                pyautogui.press('up')  # Simula pulsar la tecla "arriba" para desplazarse hacia arriba

    # Convertir el marco de BGR a HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crear máscaras para los rangos de color
    mask_color1 = cv2.inRange(hsv_frame, lower_color1, upper_color1)
    mask_color2 = cv2.inRange(hsv_frame, lower_color2, upper_color2)
    mask_pink = cv2.inRange(hsv_frame, lower_pink, upper_pink)

    # Combinar las máscaras
    combined_mask = mask_color1 | mask_color2 | mask_pink

    # Encontrar contornos en la máscara combinada
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 3)

            if not facebook_opened and cv2.inRange(hsv_frame, lower_pink, upper_pink).any():
                cv2.putText(frame, "Objeto Rosado Detectado (Facebook)", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                webbrowser.open("https://www.facebook.com")
             

            if not close_page and (cv2.inRange(hsv_frame, lower_color1, upper_color1).any() or cv2.inRange(hsv_frame, lower_color2, upper_color2).any()):
                cv2.putText(frame, "Color Detectado - Cerrar Página", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                pyautogui.hotkey('ctrl', 'w')
                close_page = True

    # Mostrar el marco con la detección
    cv2.imshow('Color Detection', frame)

    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
