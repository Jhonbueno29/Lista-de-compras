from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os itens (em um aplicativo real, usaríamos um banco de dados)
lista_compras = []

@app.route('/')
def index():
    return render_template('index.html', itens=lista_compras)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    item = request.form.get('item')
    if item and item.strip():  # Verifica se o item não está vazio
        lista_compras.append({'nome': item, 'comprado': False})
    return redirect(url_for('index'))

@app.route('/marcar/<int:id>')
def marcar(id):
    if 0 <= id < len(lista_compras):
        lista_compras[id]['comprado'] = not lista_compras[id]['comprado']
    return redirect(url_for('index'))

@app.route('/remover/<int:id>')
def remover(id):
    if 0 <= id < len(lista_compras):
        lista_compras.pop(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)