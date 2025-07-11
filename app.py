from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="¡Hola desde el backend")

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return jsonify(message=f"¡Hola, {nombre}! como estas?")

@app.route('/info')
def info():
    return jsonify(
        api_name="Simple Flask Backend",
        version="1.0.0",
        description="Un pequeño backend de ejemplo para demostrar Flask y Docker ECR y demas."
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
