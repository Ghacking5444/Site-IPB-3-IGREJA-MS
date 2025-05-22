from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/versiculos')
def versiculos():
    return render_template('versiculos2.html')

if __name__ == '__main__':
    app.run(debug=True)
