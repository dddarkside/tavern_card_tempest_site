from flask import Flask, render_template, url_for, request, session, redirect
from db_scripts import *

app = Flask(__name__, static_url_path='/static')

def start():
    session['status'] = None
    return redirect(url_for('home'))

def home():
    if not session['status']:
        return render_template("home.html")
    if request.method == 'POST':
        if session['status'] == "login":
            return auth()
        elif session['status'] == "reg":
            return reg()
   

def registration():
    session['status'] = 'reg'
    return render_template("registration.html")

def reg():
    '''Функция регистрации'''
    session['auth_name'] = request.form.get('name')
    session['auth_mail'] = request.form.get('email')
    session['auth_pass'] = request.form.get('password')

    db_open()
    if db_do(f"select mail from users where mail='{session['auth_mail']}'"):  # Такая почта уже есть
        return redirect(url_for('registration'))
    db_do(f"insert into users(mail, name) values ('{session['auth_mail']}', '{session['auth_name']}')")
    session['auth_id'] = db_do(f"select id from users where mail='{session['auth_mail']}'")[0]
    db_do(f"insert into auth(id, password) values ({session['auth_id']}, '{session['auth_pass']}')")
    session['user'] = session['auth_mail']
    session['status'] = None
    db_close()
    return redirect(url_for('home'))

def login():
    session['status'] = 'login'
    return render_template("login.html")

def auth():
    '''Функция аутентификации'''
    session['auth_mail'] = request.form.get('email')
    session['auth_pass'] = request.form.get('password')
    db_open()
    session['auth_id'] = db_do(f"select id from users where mail='{session['auth_mail']}'")
    if session['auth_id']:
        session['auth_pass_true'] = db_do(f"select * from auth where id={session['auth_id'][0]}")
        db_close()
        if not session['auth_pass_true']:
            return redirect(url_for('login'))  # Нет такого пользователя
        
        if session['auth_pass'] == session['auth_pass_true'][1]:
            session['user'] = session['auth_mail']
            session['status'] = None
            return redirect(url_for('home'))
    db_close()
    return redirect(url_for('login'))
            


app.add_url_rule('/', 'start', start)
app.add_url_rule('/home', 'home', home, methods=['post', 'get'])
app.add_url_rule('/registration', 'registration', registration)
app.add_url_rule('/login', 'login', login)

app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretKey'

app.run()