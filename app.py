#pip install requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '%'
app.config['SITE_NAME'] = 'Contador de Tags HTML'

@app.route('/')
def indice():
    return render_template('indice.html', site_nome=app.config['SITE_NAME'])

@app.route('/count_tags', methods=['POST'])
def contador_tag():
    url = request.form['url']
    try:
        response = requests.get(url)
        response.raise_for_status()
        contador_de_tags = contar_tags(response.text)
        return render_template('resultado.html', contador_de_tags=contador_de_tags)
        
    except requests.exceptions.RequestException as e:
        return f"<p>Erro ao acessar a URL: {url}, verifique se está correta </p>"

def contar_tags(codigo):
    soup = BeautifulSoup(codigo, 'html.parser')
    contador_de_tags = {}
    for tag in soup.find_all():
        contador_de_tags[tag.name] = contador_de_tags.get(tag.name, 0) + 1
    return contador_de_tags
