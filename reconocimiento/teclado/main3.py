import subprocess

ruta_script = "./AI/app.py"

print(f"Ejecutando el script en la ruta: {ruta_script}")

try:
    subprocess.run(["python", ruta_script])
except Exception as e:
    print(f"Error al ejecutar el script: {e}")
