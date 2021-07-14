from webapp.db import db_session
from webapp.models import Clothes
from webapp.get_weather import weather_by_city



def get_clothes(gender, weather_info):
    """Завел константы для удобного сравнения. По итогу возвращается список словарей где в каждом словаре ключ тип одежды , а значение ссылка на иконку для вывода.
    """
    FREEZING = -50 < int(weather_info['temp_now']) <= -5
    COLD = -5 < int(weather_info['temp_now']) <= 6
    CHILLY = 6 < int(weather_info['temp_now']) <= 15
    WARM = 15 < int(weather_info['temp_now']) <= 20
    HOT = 20 < int(weather_info['temp_now']) <= 50
    RAIN = int(weather_info['chanceofrain']) 
    SUN = weather_info['weather_desk_now']
    #print(weather_info)

    if gender and FREEZING:
        clothes = db_session.query(Clothes.cloth_type, Clothes.icon_path).filter(Clothes.temp_freezing == True, Clothes.gender.in_((gender, 'any')))
        clothes_list = []
        for key, value in clothes:
            clothes_dict = {}
            clothes_dict[key] = value
            clothes_list.append(clothes_dict)
        return clothes_list
    
    elif gender and COLD:
        clothes = db_session.query(Clothes.cloth_type, Clothes.icon_path).filter(Clothes.temp_cold == True, Clothes.gender.in_((gender, 'any')))
        clothes_list = []
        for key, value in clothes:
            clothes_dict = {}
            clothes_dict[key] = value
            clothes_list.append(clothes_dict)
        return clothes_list
    
    elif gender and CHILLY:
        clothes = db_session.query(Clothes.cloth_type, Clothes.icon_path).filter(Clothes.temp_chilly == True, Clothes.gender.in_((gender, 'any')))
        clothes_list = []
        for key, value in clothes:
            clothes_dict = {}
            clothes_dict[key] = value
            clothes_list.append(clothes_dict)
        return clothes_list

    elif gender and WARM:
        clothes = db_session.query(Clothes.cloth_type, Clothes.icon_path).filter(Clothes.temp_warm == True, Clothes.gender.in_((gender, 'any')))
        clothes_list = []
        for key, value in clothes:
            clothes_dict = {}
            clothes_dict[key] = value
            clothes_list.append(clothes_dict)
        return clothes_list

    elif gender and HOT:
        clothes = db_session.query(Clothes.cloth_type, Clothes.icon_path).filter(Clothes.temp_hot == True, Clothes.gender.in_((gender, 'any')))
        clothes_list = []
        for key, value in clothes:
            clothes_dict = {}
            clothes_dict[key] = value
            clothes_list.append(clothes_dict)
        return clothes_list


# if __name__ == '__main__':
#     print(get_clothes('female', weather_by_city('Виннипег')))