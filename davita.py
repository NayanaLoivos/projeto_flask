from flask import Flask, render_template, request, redirect, session, flash
class Unidade:
    def __init__(self, name, street):
        self.name = name
        self.street = street

unidade1 = Unidade('Pantanal', 'Rua...-MS')
lista = [unidade1]

app = Flask(__name__) #__name__ faz referência ao próprio arquivo
app.secret_key = 'goofy'
@app.route('/') #quando criamos uma nova rota, precisamos de uma função que crie uma nova rota.
def ola():
    return render_template('clinicas.html', titulo="Unidades", unidades=lista)

@app.route('/new-unidade')
def newClinica():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=new-unidade')
    return render_template('new-clinica.html', titulo='Nova unidade Davita')

@app.route('/create', methods=['POST',])
def create():
    name = request.form['name']
    street = request.form['street']
    unidade = Unidade(name, street)
    lista.append(unidade)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if '123456' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + 'logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        session['usuario_logado'] = None
        flash('Login ou senha inválidos!!!')
        return redirect('/login')
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado!')
    return redirect('/login')

app.run(debug=True) #aqui eu poderia definir (host='0.0.0.0', port=8080), mas não levar essas configurações para produção.

app.run()
