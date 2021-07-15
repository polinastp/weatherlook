import requests
# from webapp.config import WEATHER_API_KEY, WEATHER_URL


def weather_by_city(city_name, num_of_days=1):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': 'ddc1f1e295a54d1ea20213601213105', 
        'q': city_name,
        'format': 'json',
        'num_of_days': num_of_days,
        'tp': 24,
        'showlocaltime': 'yes',
        'lang': 'ru'
    }
    try:
        response = requests.get(weather_url, params=params)
        response.raise_for_status()
        weather = response.json()
        try:
            local_time = weather['data']['time_zone'][0]['localtime']
            current_condition = weather['data']['current_condition'][0]
            weather_by_day = weather['data']['weather'][0]
        except(IndexError, KeyError):
            return False
        if current_condition and weather_by_day:
            try:
                weather_info = {
                    'city': weather['data']['request'][0]['query'],
                    'local_time': weather['data']['time_zone'][0]['localtime'],
                    'temp_now': current_condition['temp_C'],
                    'feelsLike_now': current_condition['FeelsLikeC'],
                    'humidity_now': current_condition['humidity'],
                    'icon': current_condition['weatherIconUrl'][0]['value'],
                    'wind_speed_now': current_condition['windspeedKmph'],
                    'weather_desk_now': current_condition['lang_ru'][0]['value'],
                    'weather_desk_now_ru': current_condition['weatherDesc'][0]['value'],
                    'sunrise': weather_by_day['astronomy'][0]['sunrise'],
                    'sunset': weather_by_day['astronomy'][0]['sunset'],
                    'min_temp': weather_by_day['mintempC'],
                    'max_temp': weather_by_day['maxtempC'],
                    'avg_temp': weather_by_day['avgtempC'],
                    'weather_desk_day': weather_by_day['hourly'][0]['weatherDesc'][0]['value'],
                    'weather_desk_day_ru': weather_by_day['hourly'][0]['lang_ru'][0]['value'],
                    'chanceofrain': weather_by_day['hourly'][0]['chanceofrain']
                }
                return weather_info
            except(IndexError, TypeError, KeyError):
                return False
    except(requests.RequestException, ValueError):
        print('Ошибка подключения')
        return False
    return False


# if __name__ == '__main__':
#     print(weather_by_city('Moscow,Russia'))