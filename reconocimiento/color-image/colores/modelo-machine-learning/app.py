import tensorflow as tf
import matplotlib.pyplot as plt

# Cargar el conjunto de datos MNIST
(x_train, y_train), _ = tf.keras.datasets.mnist.load_data()

# Normalizar los valores de píxeles entre 0 y 1
x_train = x_train / 255.0

# Visualizar algunas imágenes de entrenamiento
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')
plt.show()

# Definir el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compilar y entrenar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
