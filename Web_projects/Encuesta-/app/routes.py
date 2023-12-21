from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
import csv
import re
main = Blueprint('main', __name__)
porcentajes = []
porcentajes_lista = []

@main.route('/')
def index():
    datos = obtener_datos_desde_csv()
    return render_template('formulario.html', datos=datos)

@main.route('/index')
def volver_index():
    return render_template('formulario.html')

@main.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    ide = generar_id()
    print(ide)

    datos_actualizados = [ide, request.form['nombre'], request.form.get('pregunta-1'),
                          request.form.get('pregunta-2'), request.form.get('pregunta-3'),
                          request.form.get('pregunta-4'), request.form.get('pregunta-5'),
                          request.form.get('pregunta-6'), request.form.get('pregunta-7'),
                          request.form.get('pregunta-8'), request.form.get('pregunta-9'),
                          request.form['pregunta-10']]

    porcen = analizar(datos_actualizados)
    print(porcen)
    print(f"{sacar_porcentajes(porcen)}")
    guardar_datos_en_csv(datos_actualizados)
    ordenar_datos()
    return redirect(url_for('main.index'))

@main.route('/resultados')
def resultados():
    datos = obtener_datos_desde_csv()
    porcentajes = obtener_porcentajes_desde_archivo()
    return render_template('respuesta.html', datos=datos, porcentajes=porcentajes)

@main.route('/ver_porcentajes')
def ver_porcentajes():
    porcentajes = obtener_porcentajes_desde_archivo()
    return render_template('porcentajes.html',porcentajes=porcentajes)

@main.route('/borrar_registros')
def borrar_registros():
    borrar_registros()
    return render_template('respuesta.html') 

def generar_id():
    ruta = 'app/data/id.txt'
    with open(ruta, "r+") as file:
        ide = int(file.read().strip() or 0)
        ide += 1
        file.seek(0)
        file.write(str(ide))
        file.truncate()
    return ide


def guardar_datos_en_csv(datos):
    with open('app\data\datos.csv', 'a', newline='', encoding='utf-8') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(datos)

def obtener_datos_desde_csv():
    with open('app/data/datos.csv', 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        return list(lector_csv)


def analizar(datos):
    porcentajes = []

    def separar_si_no(n, iden, i, opc):
        print(f"Entró contenedor-{n}")
        ruta = f"app/data/contadores-{n}.csv"
        print(ruta)
        total = float(100)
        with open(ruta, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)[0]
            num = int(i)

            data[num - 1] = str(int(data[num - 1]) + 1)
            valor = data[num - 1]
            print(valor)

            porcentaje = int(valor) / int(iden) * 100
            restante = round((total - float(porcentaje)), 2)
            porcentaje = round(porcentaje, 2)
            restante = round(restante, 2)

            if opc == "si":
                porcentajes.append(
                    f"P{num} {opc.upper()} = {porcentaje}%  NO = {restante}%")
            else:
                porcentajes.append(
                    f"P{num} {opc.upper()} = {porcentaje}%  SI = {restante}%")

        with open(ruta, 'w', newline='') as files:
            writer = csv.writer(files)
            writer.writerow(data)

    ult = datos
    iden = ult[0]
    for i in range(len(ult)):
        if ult[i] == "si" or ult[i] == "diariamente" or ult[i] == "mensualmente" or ult[i] == "semanalmente" or ult[i] == "aveces":
            contadores = 1
            opc = "si"
            separar_si_no(contadores, iden, i, opc)

        else:
            contadores = 2
            opc = "no"
            separar_si_no(contadores, iden, i, opc)

    print(iden)
    ordenar_porcentajes(porcentajes)

    return porcentajes


def ordenar_datos():
    with open('app/data/datos.csv', 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        info = list(lector_csv)
    with open('app/data/datos.txt', "w", encoding="utf-8") as archivo:
        for i in range(len(info)):
            archivo.write(
                f'''\nPERSONA ID {i + 1}: {info[i][0]}\nNOMBRE TIENDA: {info[i][1]}\nPREGUNTA 1: {info[i][2]}\nPREGUNTA 2: {info[i][3]}\nPREGUNTA 3: {info[i][4]}\nPREGUNTA 4: {info[i][5]}\nPREGUNTA 5: {info[i][6]}\nPREGUNTA 6: {info[i][7]}\nPREGUNTA 7: {info[i][8]}\nPREGUNTA 8: {info[i][9]}\nPREGUNTA 9: {info[i][10]}\nPREGUNTA 10:  {info[i][11]}\n''')  

def obtener_porcentajes_desde_archivo():
    with open('app/data/porcentajes.txt','r',encoding="utf-8") as archivo:
        porcentajes=archivo.readlines()
    return porcentajes

def ordenar_porcentajes(porcentajes):
    
    with open('app/data/porcentajes.txt', "w", encoding="utf-8") as archivo:
        for i in range(len(porcentajes)):
            archivo.write(f'''{porcentajes[i]}\n''')
    return porcentajes

def sacar_porcentajes(porcen):
         #Abrir el archivo y leer cada línea
        for linea in porcen:
            resultado = re.search(r'\b(\d+)\b', linea)
        if resultado:
            porcentaje_int = int(resultado.group())
            porcentajes_lista.append(porcentaje_int)
         # Imprimir la lista de porcentajes
        return porcentajes_lista

def borrar_registros():
    # Listas de datos y rutas de archivos
    listas = [[0]*12, [0]*12]  # Dos listas con 12 ceros
    archivos = ['app/data/contadores-1.csv', 'app/data/contadores-2.csv']

    # Borrar el contenido de los archivos de contadores
    for i, archivo in enumerate(archivos):
        with open(archivo, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(listas[i])

    # Borrar el contenido del archivo datos.csv
    with open('app/data/datos.csv', 'w', encoding='utf-8', newline='') as datos_csv:
        pass  # Al abrir en modo escritura, ya borra el contenido
    with open('app/data/datos.txt','w',encoding='utf-8') as datos_txt:
        datos_txt.write('')
    with open('app/data/id.txt','w',encoding='utf-8') as identificacion:
        identificacion.write('0')
    with open('app/data/porcentajes.txt','w',encoding='utf-8') as porcentajes:
        porcentajes.write('')
    print('archivos formateados con éxito')