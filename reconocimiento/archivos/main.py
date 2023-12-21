import os
import shutil

def organizar_archivos_por_tipo(directorio_origen, directorio_destino):
    # Obtener la lista de archivos en el directorio de origen
    archivos = os.listdir(directorio_origen)

    for archivo in archivos:
        # Obtener la ruta completa del archivo
        ruta_completa = os.path.join(directorio_origen, archivo)

        if os.path.isfile(ruta_completa):
            # Obtener la extensión del archivo
            _, extension = os.path.splitext(archivo)
            # Eliminar el punto de la extensión
            extension = extension[1:]

            # Crear un directorio para la extensión si no existe
            directorio_extension = os.path.join(directorio_destino, extension)
            if not os.path.exists(directorio_extension):
                os.makedirs(directorio_extension)

            # Mover el archivo al directorio de la extensión
            shutil.move(ruta_completa, os.path.join(directorio_extension, archivo))

if __name__ == "__main__":
    directorio_origen = "C:\Users\Sena\Downloads\marketing\1. Instagram para Ecommerce"
    directorio_destino = "C:/Users/Sena/Downloads/archivos"

    organizar_archivos_por_tipo(directorio_origen, directorio_destino)
