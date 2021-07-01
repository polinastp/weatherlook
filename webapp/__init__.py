from flask import Flask, render_template
from webapp.forms import LoginForm

def create_app():
    app = Flask(__name__, template_folder={})
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return render_template('index.html')  ## здесь какая-то непонятная ошибка - typeerror


    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app