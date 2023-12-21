from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import numpy as np
import cv2

# Cargar el modelo preentrenado MobileNetV2
modelo = MobileNetV2(weights='imagenet')

# Cargar y preprocesar la imagen
imagen_path = 'C:/Users/Sena/Downloads/archivos/jpg/michi.jpg'
img = image.load_img(imagen_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Realizar la predicción
predicciones = modelo.predict(img_array)

# Decodificar y mostrar las predicciones
etiquetas = decode_predictions(predicciones, top=3)[0]

for etiqueta in etiquetas:
    print(f'{etiqueta[1]}: {etiqueta[2]:.2f}')

# Mostrar la imagen con las predicciones
img = cv2.imread(imagen_path)
img = cv2.resize(img, (224, 224))
cv2.putText(img, f'{etiquetas[0][1]}: {etiquetas[0][2]:.2f}', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
cv2.imshow('Resultado', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
