from flask import Flask, render_template, url_for, request, session, redirect
from db_scripts import *

app = Flask(__name__, static_url_path='/static')

def start():
    return redirect(url_for('home'))

def home():
    if request.method == "POST":
        return auth()
    return render_template("home.html")

def registration():
    # mail = request.form.get('email')
    # password = request.form.get('password')
    # id = int(db_do("select max(id) from users"))
    # db_do(f"insert into users(id, mail, name) values ({id}, {mail}, {})")
    return render_template("registration.html")

def login():
    return render_template("login.html")

def auth():
    '''Функция аутентификации'''
    session['auth_mail'] = request.form.get('email')
    session['auth_pass'] = request.form.get('password')
    db_open()
    session['auth_id'] = db_do(f"select id from users where mail='{session['auth_mail']}'")
    if session['auth_id']:
        session['auth_pass_true'] = db_do(f"select * from auth where id={session['auth_id'][0]}")
        if not session['auth_pass_true']:
            return redirect(url_for('login'))  # Нет такого пользователя
        
        if session['auth_pass'] == session['auth_pass_true'][1]:
            session['user'] = session['auth_mail']
            return redirect(url_for('home'))
    return redirect(url_for('login'))
            


app.add_url_rule('/', 'start', start)
app.add_url_rule('/home', 'home', home,  methods=['post', 'get'])
app.add_url_rule('/registration', 'registration', registration)
app.add_url_rule('/login', 'login', login)

app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretKey'

app.run()