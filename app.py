from flask import Flask, render_template, request, jsonify
from openai import Model, GPT, Completion

app = Flask(__name__)

# Replace 'your_openai_api_key' with your OpenAI API key
openai_api_key = 'your_openai_api_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_text', methods=['POST'])
def generate_text():
    input_text = request.json['input_text']
    openai_model = GPT(model="text-davinci-003", api_key=openai_api_key)
    response = openai_model.Completion.create(prompt=input_text, max_tokens=50)
    generated_text = response.choices[0].text.strip()
    return jsonify({"generated_text": generated_text})

if __name__ == '__main__':
    app.run(debug=True)
