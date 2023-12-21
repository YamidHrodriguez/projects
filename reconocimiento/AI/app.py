from flask import Flask, render_template, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)

class Chatbot:
    def __init__(self):
        # Cargar el modelo preentrenado y el tokenizador
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()

    def generate_response(self, input_text, max_length=50):
        # Tokenizar la entrada
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt").to(self.device)

        # Generar una respuesta
        output = self.model.generate(
            input_ids,
            max_length=500,
            num_return_sequences=1,
            num_beams=5,
            no_repeat_ngram_size=2,
            top_k=50,
            top_p=0.95,
            temperature=0.7,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id,
        )

        # Decodificar la salida
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        print(response)
        return response

# Instanciar el chatbot
chatbot = Chatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    
    # Salir del bucle si el usuario escribe "salir"
    if user_input.lower() == "salir":
        return render_template('index.html', response="Hasta luego. ¡Que tengas un buen día!")

    # Generar y mostrar la respuesta del chatbot
    response = chatbot.generate_response(user_input)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
