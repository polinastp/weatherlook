from flask import Flask, render_template, redirect, url_for
from webapp.forms import CityForm, LoginForm
from get_weather import weather_by_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')



    @app.route('/')
    def index():
        title = 'Погода в городе'
        city_form = CityForm()
        return render_template('index.html', page_title=title, form=city_form)  ## здесь какая-то непонятная ошибка - typeerror


    @app.route('/weather', methods=['GET', 'POST'])
    def weather_clothes():
        title = "Погода"
        city_form = CityForm()
        if city_form.validate_on_submit():
            city = city_form.city.data
            weather_info = weather_by_city(city)
            print(weather_info)
            return render_template('weather.html')
        return redirect(url_for('index'))



    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app