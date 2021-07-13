import csv

from webapp.models import Clothes
from webapp.db import db_session


def save_data(row):
    clothes = Clothes(name=row['name'], gender=row['gender'],
    cloth_type=row['cloth_type'], temp_tag=row['temp_tag'].split(';'), 
    rain=bool(int(row['rain'])), sun=bool(int(row['sun'])), icon_path=row['icon_path'])
    
    db_session.add(clothes)
    db_session.commit()

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['name', 'gender', 'cloth_type', 'temp_tag',
         'rain', 'sun', 'icon_path']
        reader = csv.DictReader(f, fields, delimiter =',')
        for row in reader:
            save_data(row)

    
if __name__ == "__main__":
    read_csv('weatherlook.csv')
