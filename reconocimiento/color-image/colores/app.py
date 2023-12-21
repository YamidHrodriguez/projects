from flask import Flask, render_template, request, jsonify
from colorthief import ColorThief
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_palette', methods=['POST'])
def get_palette():
    data = request.get_json()
    image_data = data.get('image_data', '')

    # Eliminamos el encabezado 'data:image/png;base64,' del string de datos
    image_data = image_data.replace('data:image/png;base64,', '')

    # Decodificamos el string base64
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))

    # Convertimos la imagen a formato RGB
    image = image.convert('RGB')

    # Guardamos la imagen en un objeto de archivo en memoria
    image_file = io.BytesIO()
    image.save(image_file, format="PNG")
    image_file.seek(0)

    # Utilizamos ColorThief para extraer la paleta de colores
    color_thief = ColorThief(image_file)
    colors = color_thief.get_palette(color_count=5)  # Puedes ajustar el número de colores según tus necesidades

    # Convertimos los colores a formato hexadecimal
    hex_colors = ['#%02x%02x%02x' % color for color in colors]

    return jsonify({'colors': hex_colors})

if __name__ == '__main__':
    app.run(debug=True)
