import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    # Carga el archivo CSV
    data = pd.read_csv('modelo-machine-learning\datos.csv')

    # Contadores para "sí" y "no"
    si_count = data['respuesta'].eq('si').sum()
    no_count = data['respuesta'].eq('no').sum()

    # Calcula los porcentajes
    total_respuestas = si_count + no_count
    porcentaje_si = (si_count / total_respuestas) * 100
    porcentaje_no = (no_count / total_respuestas) * 100

    # Crea un gráfico de barras
    labels = ['Sí', 'No']
    porcentajes = [porcentaje_si, porcentaje_no]

    plt.bar(labels, porcentajes, color=['green', 'red'])
    plt.ylabel('Porcentaje')
    plt.title('Respuestas Sí/No')

    # Convierte el gráfico a imagen
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Renderiza la plantilla con la imagen del gráfico
    return render_template('index.html', image=img.read().encode('base64').decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)
