from flask import Flask, render_template, request
from models.calculadora import PegadaHidrica

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        banho = int(request.form['banho'])
        roupa = int(request.form['roupa'])
        torneira = int(request.form['torneira'])
    except (ValueError, KeyError):
        return render_template('resultado.html', total=None, mensagem="⚠️ Verifique os campos: use apenas números inteiros.")

    calculadora = PegadaHidrica(banho, roupa, torneira)
    total = calculadora.calcular_total()

    if total > 1500:
        mensagem = "🚨 Consumo alto! Hora de rever seus hábitos."
    elif total > 800:
        mensagem = "⚖️ Consumo médio. Dá pra melhorar!"
    else:
        mensagem = "🌿 Parabéns! Você tem uma boa pegada hídrica!"

    return render_template('resultado.html', total=total, mensagem=mensagem)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)