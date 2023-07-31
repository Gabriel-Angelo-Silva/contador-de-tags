from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count_tags', methods=['POST'])
def count_tags():
    codigo = request.form['codigo']
    contador_de_tags = contar_tags(codigo)
    return render_template('resultado.html', contador_de_tags = contador_de_tags)

def contar_tags(codigo):
    soup = BeautifulSoup(codigo, 'html.parser')
    tags = soup.find_all()
    contador_de_tags = {}
    
  for tag in tags:
        nome_tag = tag.name
        contador_de_tags[nome_tag] = contador_de_tags.get(nome_tag, 0) + 1
    return contador_de_tags

if __name__ == '__main__':
    app.run(debug=True)
