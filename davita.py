from flask import Flask, render_template, request, redirect

class Unidade:
    def __init__(self, name, street):
        self.name = name
        self.street = street

unidade1 = Unidade('Pantanal', 'Rua...-MS')
lista = [unidade1]

app = Flask(__name__) #__name__ faz referência ao próprio arquivo
@app.route('/') #quando criamos uma nova rota, precisamos de uma função que crie uma nova rota.
def ola():
    return render_template('clinicas.html', titulo="Unidades", unidades=lista)

@app.route('/new-unidade')
def newClinica():
    return render_template('new-clinica.html', titulo='Nova unidade Davita')

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    street = request.form['street']
    unidade = Unidade(name, street)
    lista.append(unidade)
    return redirect('/')

app.run(debug=True) #aqui eu poderia definir (host='0.0.0.0', port=8080), mas não levar essas configurações para produção.


app.run()
