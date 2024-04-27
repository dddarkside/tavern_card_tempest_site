from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')

def start():
    return render_template("home.html")

def registration():
    return render_template("registration.html")

def login():
    return render_template("login.html")


app.add_url_rule('/', 'home', start)
app.add_url_rule('/registration', 'registration', registration)
app.add_url_rule('/login', 'login', login)

app.run()