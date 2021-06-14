import requests


def weather_by_city(city_name, num_of_days=1):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': 'ddc1f1e295a54d1ea20213601213105',
        'q': city_name,
        'format': 'json',
        'num_of_days': num_of_days,
        'lang': 'ru'
    }
    try:
        response = requests.get(weather_url, params=params)
        response.raise_for_status()
        weather = response.json()
        if 'data' in weather:
            try:
                weather_info = {
                    'city': weather['data']['request'][0]['query'],
                    'temp_now': weather['data']['current_condition'][0]['temp_C'],
                    'feelsLike_now': weather['data']['current_condition'][0]['FeelsLikeC'],
                    'humidity': weather['data']['current_condition'][0]['humidity'],
                    'icon': weather['data']['current_condition'][0]['weatherIconUrl'][0]['value'],
                    'wind_speed_now': weather['data']['current_condition'][0]['windspeedKmph'],
                    'weather_desk': weather['data']['current_condition'][0]['weatherDesc'][0]['value'],
                    'sunrise': weather['data']['weather'][0]['astronomy'][0]['sunrise'],
                    'sunset': weather['data']['weather'][0]['astronomy'][0]['sunset'],
                    'min_temp': weather['data']['weather'][0]['mintempC'],
                    'max_temp': weather['data']['weather'][0]['maxtempC'],
                    'avg_temp': weather['data']['weather'][0]['avgtempC']
                }
                return weather_info
            except(IndexError, TypeError):
                return False
        return False
    
    except(requests.RequestException, ValueError):
        return False





if __name__ == '__main__':
    print(weather_by_city('Moscow,Russia'))