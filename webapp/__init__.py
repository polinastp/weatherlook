from flask import Flask, render_template, redirect, request, url_for, flash
from webapp.forms import CityForm, LoginForm
from get_weather import weather_by_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')



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
        return redirect('index.html')


        
    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app