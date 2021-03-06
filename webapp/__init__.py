from flask import Flask, render_template, redirect, request, url_for, flash
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from webapp.forms import CityForm, LoginForm, RegistationForm
from webapp.get_weather import weather_by_city
from query_clothes import get_clothes
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
            gender = city_form.gender.data
            #print(city, gender)
            return redirect(url_for('weather_clothes', city=city, gender=gender))
        return render_template('index.html', page_title=title, city_form=city_form)  


    @app.route('/weather', methods=['GET', 'POST'])
    def weather_clothes():
        title = "Погода"
        city_form= CityForm()
        if request.method == 'GET':
            city = request.args.get('city')
            gender = request.args.get('gender')
            #print(gender)
            weather_info = weather_by_city(city)
            if weather_info and gender:
                clothes_info = get_clothes(gender, weather_info)
                print(weather_info)
                print(clothes_info)
                return render_template('weather.html', page_title=title, city_form=city_form, weather_info=weather_info, clothes_info=clothes_info)  
        flash('Введите название города')
        return redirect(url_for('index'))


    @app.route('/login')
    def login():
        form = LoginForm()
        if current_user.is_authenticated:
            city = current_user.city
            gender = current_user.gender
            return redirect(url_for('weather_clothes', city=city, gender=gender))
        title = "Авторизация"
        login_form = LoginForm()
        city_form = CityForm()
        return render_template('login.html', page_title=title, form=login_form, city_form=city_form)


    @app.route('/process-login', methods = ['POST'])
    def process_login():
        form = LoginForm()


        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            city = user.city
            gender = user.gender
            if user and user.check_password(form.password.data):
                login_user(user)
                flash("Вы успешно вошли в профиль")
                return redirect(url_for('weather_clothes', city=city, gender=gender))

        flash("Неправильное имя пользователя или пароль")
        return redirect(url_for('login'))


    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы вышли из профиля')
        return redirect(url_for('index'))


    @app.route('/register')
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('weather_clothes'))
        registration_form = RegistationForm()
        city_form = CityForm()
        title = 'Регистрация'
        return render_template('registration.html', page_title=title, form=registration_form, city_form=city_form)


    @app.route('/process-register', methods=['POST'])
    def process_register():
        form = RegistationForm()
        if form.validate_on_submit():
            new_user = User(username=form.username.data, email=form.email.data,
                            gender=form.gender.data, city=form.city.data,
                            password=form.password.data, role='user')
            new_user.set_password(form.password.data)
            db_session.add(new_user)
            db_session.commit()
            flash('Регистрация прошла успешно!')
            return redirect(url_for('login'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash('Ошибка в поле "{}": - {}'.format(getattr(form, field).label.text,error))
            return redirect(url_for('register'))

    return app