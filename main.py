from flask import Flask, render_template, url_for, request, session, redirect
from db_scripts import *

app = Flask(__name__, static_url_path='/static')

def start():
    return redirect(url_for('home'))

def home():
    print("CPAKA")
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
    mail = request.form.get('email')
    password = request.form.get('password')
    db_open()
    id = db_do(f"select id from users where mail='{mail}'")
    if id:
        if password == db_do(f"select * from auth where id='{id}'"):
            session['user'] = mail
            return redirect(url_for('home'))
    return redirect(url_for('login'))
            


app.add_url_rule('/', 'start', start)
app.add_url_rule('/home', 'home', home,  methods=['post', 'get'])
app.add_url_rule('/registration', 'registration', registration)
app.add_url_rule('/login', 'login', login)

app.run()