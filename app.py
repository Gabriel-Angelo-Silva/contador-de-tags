#pip install requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '%'
app.config['NOME_SITE'] = 'Contador de Tags HTML'

@app.route('/')
def indice():
    return render_template('indice.html', nome_site=app.config['NOME_SITE'])

@app.route('/contar_tags', methods=['POST'])
def contador_tag():
    entrada_dados = request.form['entrada_dados']
    
    try:
        codigo = obter_codigo(entrada_dados)
        contador_de_tags = contar_tags(codigo)
        return render_template('resultado.html', contador_de_tags = contador_de_tags)
    except requests.exceptions.RequestException as e:
        return "<p>Erro ao acessar a URL ou analisar o código HTML.</p>"

def obter_codigo(entrada_dados):
    if entrada_dados.startswith(("http://", "https://")):
        resposta = requests.get(entrada_dados)
        resposta.raise_for_status()
        return resposta.text
    return entrada_dados

def contar_tags(codigo):
    soup = BeautifulSoup(codigo, 'html.parser')
    contador_de_tags = {}
    for tag in soup.find_all():
        contador_de_tags[tag.name] = contador_de_tags.get(tag.name, 0) + 1
    return contador_de_tags
