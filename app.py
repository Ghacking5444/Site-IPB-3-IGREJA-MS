from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Garante segurança para sessões e futuros formulários

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')  # Executa com HTTPS autoassinado
