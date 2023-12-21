import os

def obtener_archivos_en_carpeta(ruta_carpeta):
    lista_archivos = []
    
    # Recorre todos los archivos en la carpeta
    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        
        # Verifica si es un archivo (no un directorio)
        if os.path.isfile(ruta_archivo):
            lista_archivos.append(ruta_archivo)

    return lista_archivos

# Ruta de la carpeta que quieres explorar
ruta_carpeta = 'C:/Users/Sena/OneDrive/Documentos/Sound recordings'

# Obtener la lista de archivos
archivos = obtener_archivos_en_carpeta(ruta_carpeta)

# Imprimir la lista de archivos
print("Archivos en la carpeta:")
for i in range(len(archivos)):
    if i == 1:
        print(archivos[i])
