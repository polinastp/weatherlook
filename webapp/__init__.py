from flask import Flask, render_template, redirect, request, url_for, flash
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from webapp.forms import CityForm, LoginForm
from get_weather import weather_by_city
from webapp.models import User
from webapp.db import db_session

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        title = 'Погода в городе'
        city_form = CityForm()
        if city_form.validate_on_submit():
            city = city_form.city.data
            print(city)
            flash('Введите название города')
            return redirect(url_for('weather_clothes', city=city))
        return render_template('index.html', page_title=title, form=city_form)  


    @app.route('/weather', methods=['GET', 'POST'])
    def weather_clothes():
        title = "Погода"
        if request.method == 'GET':
            city = request.args.get('city')
            weather_info = weather_by_city(city)
            print(weather_info)
            return render_template('weather.html', page_title=title)
        return redirect(url_for('index'))

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('weather_clothes'))
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)


    @app.route('/process-login', methods = ['POST'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash("Вы успешно вошли в профиль")
                return redirect(url_for('weather_clothes'))

        flash("Неправильное имя пользователя или пароль")
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы вышли из профиля')
        return redirect(url_for('index'))


    return app