from flask import Flask, render_template

app = Flask(__name__)

# Lista de versículos
versiculos = [
    "O Senhor é o meu pastor; nada me faltará. – Salmos 23:1",
    "Entrega o teu caminho ao Senhor; confia nele, e ele tudo fará. – Salmos 37:5",
    "Tudo posso naquele que me fortalece. – Filipenses 4:13",
    "Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito... – João 3:16",
    "O Senhor é bom, um refúgio em tempos de angústia. – Naum 1:7",
    "Alegrai-vos na esperança, sede pacientes na tribulação... – Romanos 12:12",
    "Lâmpada para os meus pés é a tua palavra... – Salmos 119:105",
    "Não temas, porque eu sou contigo. – Isaías 41:10",
    "Bem-aventurados os que choram, porque serão consolados. – Mateus 5:4",
    "Buscai ao Senhor enquanto se pode achar... – Isaías 55:6",
    "O choro pode durar uma noite, mas a alegria vem pela manhã. – Salmos 30:5",
    "Sede fortes e corajosos. Não temais. – Deuteronômio 31:6",
    "Em tudo dai graças. – 1 Tessalonicenses 5:18",
    "O Senhor te guardará de todo mal. – Salmos 121:7",
    "Aquele que habita no esconderijo do Altíssimo... – Salmos 91:1",
    "Confia no Senhor de todo o teu coração. – Provérbios 3:5",
    "Mas os que esperam no Senhor renovarão as suas forças. – Isaías 40:31",
    "Não se turbe o vosso coração... – João 14:1",
    "Regozijai-vos sempre no Senhor. – Filipenses 4:4",
    "O Senhor pelejará por vós, e vós vos calareis. – Êxodo 14:14"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/versiculos")
def versiculos_page():
    return render_template("versiculos2.html", versiculos2=versiculos2)

if __name__ == "__main__":
    app.run(debug=True)
