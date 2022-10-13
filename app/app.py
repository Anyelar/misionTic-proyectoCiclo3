from webbrowser import get
from flask import Flask, render_template, request, jsonify, redirect, url_for
import utils, os
from forms import FormInicio
from db import get_db, close_db
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__, static_folder='./static')
app.debug = True

#if __name__ =='__main__': 
    #app.run(debug = True)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    if (request.method=='POST'):
        user = request.form['user']
        password = request.form['password']
    else:
        return render_template('login.html')

@app.route('/registro')
def registro():
    #error = None
    db = get_db()
    if(request.method =="POST"):
        userName = request.form['user']
        password = request.form['password']
        email = request.form['userEmail']
        error = []
        if not utils.isUsernameValid(userName):
            error.append('El usuario debe ser alfanumerico, o incluir . , - _')

        if not utils.isPasswordValid(password):
            error.append('La clave debe contener al menos una minuscula, una mayuscula y longitud de 8 caracteres')
        
        if not utils.isEmailValid(email):
            error.append('Correo no valido.')
            
        return render_template('formulario.html', errorMessages=error)
        #userDB = db.execute('select * FROM usuario where usuario = ? ',(user,)).fetchone()
        #close_db()
        #if userDB is not None:#(user == 'Prueba' and password =='Prueba1234'):
                
            #stored_password = userDB[4]
            #swClaveCorrecta = check_password_hash(stored_password, password)
            #if(swClaveCorrecta):
                #return redirect('message')
            #else:
                #return 'clave incorrecta.'
            #return 'sin acceso, usuario no existe.'
    #else:
        #return render_template('formulario.html')
    #    formulario = FormInicio()
    #    return render_template('login.html', form=formulario)
    #formulario = FormInicio()
    return render_template('formulario.html')

"""
@app.route('/registro', methods=('GET','POST'))
def registro():
    
    if request.method == 'POST':
        name = request.form['userName']
        user = request.form['user']
        password = request.form['password']
        email = request.form['userMail']
        error =[]

        db = get_db()
        
        if not utils.isUsernameValid(user):
            error.append('El usuario debe ser alfanumerico, o incluir . , - _')

        if not utils.isPasswordValid(password):
            print('La clave debe contener al menos una minuscula, una mayuscula y longitud de 8 caracteres')
            #error.append('La clave debe contener al menos una minuscula, una mayuscula y longitud de 8 caracteres')
            
        if not utils.isEmailValid(email):
            error.append('Correo no valido.')
        
        if len(error) == 0:
             db.execute('insert into usuario (nombre, usuario, correo, contraseña) values(name, user, email, password)',
                (name, user,email, generate_password_hash(password)))

             db.commit()

             close_db()

        
        return render_template('formulario.html', errorMessages=error)
"""    

@app.route('/cartelera')
def catalogo():
    return render_template('catalogo.html')
    
@app.route('/reseñas')
def reseñas():
    return render_template('reseñas.html')

@app.route('/pagos')
def pagos():
   return render_template('pagoTickets.html')