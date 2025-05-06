import json # добавляем модуль для работы с JSON-форматом
import urllib.request # добавляем модуль для HTTP-запросов
import turtle # модуль рисования
import os # модуль для использования возможностей операционной системы
import time # модуль для работы со временем
import webbrowser # модуль для открытия URL-адресов по умолчанию
from typing import Dict, List, Any
from http.client import HTTPResponse # импорт типов данных для аннотации типов



# пишем функцию
def main():
    url: str='http://api.open-notify.org/astros.json' # задаём адрес для запроса списка космонавтов
    res: HTTPResponse = urllib.request.urlopen(url) # открываем URL, используя urllib.request
    result: Dict[str, Any] = json.loads(res.read()) # загружаем и читаем json-файл

    # в этой же папке создаём текстовый файл с именами членов экипажа
    with open('iss.txt','w')as file: # открываем файл для записи
        file.write(f'В настоящий момент на МКС {str(result["number"])} космонавтов:\n\n')
        print('В настоящий момент на МКС '+ str(result["number"]) + ' космонавтов:\n') #добавляем запись
        people: List[Dict[str, str]] = result['people']
        for person in people:
            file.write(person['name'] + '\n')
            print(person['name'] )  # для каждого человека в списке выводим его имя
    screen: turtle.Screen = turtle.Screen() # создаём главное окно для графической работы
    screen.setup(1280,720) # устанавливаем размеры окна
    screen.setworldcoordinates(-180, -90, 180, 90) # устанавливаем систему координат для экрана, аналогичную с координатами Земли
    screen.bgpic('map.gif') # загружаем изображение карты мира из файла
    screen.register_shape('iss.gif') # загружаем изображение станции из файла
    iss = turtle.Turtle() # присваиваем переменной iss значение объекта Turtle
    iss.shape('iss.gif') # придаём переменной вид изображения из станции файла
    iss.penup() # выключаем функцию рисования следа от объекта Turtle()

    while True: # запускаем бесконечный цикл
        url: str = 'http://api.open-notify.org/iss-now.json' # адрес для запроса о текущем местоположении МКС
        res: HTTPResponse = urllib.request.urlopen(url) # объявляем переменную и сохраняем в неё ответ
        result: Dict[str, Dict[str, str]] = json.loads(res.read()) # переводим ответ в JSON и читаем
        location: Dict[str, str] = result['iss_position'] # извлекаем локацию станции
        lat: float = float(location['latitude'])
        lon: float = float(location['longitude'])
        current_time: str = time.strftime("%Y-%m-%d %H:%M:%S") # Положение текущего времени
        print("\nДата и время:", current_time) # вывод на экран
        print(f'Широта: {lat}')
        print(f'Долгота:{lon}') # вывод долготы и широты в терминал

        iss.goto(lon, lat)

        time.sleep(60)

if __name__ == "__main__":
    main()