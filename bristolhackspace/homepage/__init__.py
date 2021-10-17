from flask import Flask, render_template
from bristolhackspace.flask_theme import theme_blueprint

app = Flask(__name__)

app.register_blueprint(theme_blueprint, url_prefix='/theme')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/member')
def member():
    return render_template("member.html")