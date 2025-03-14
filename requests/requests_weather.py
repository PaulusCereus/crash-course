import requests
from prettytable import PrettyTable
import configparser

def get_api_key(filename="requests/config.ini"):
    """
    Читает API-ключ для доступа к OpenWeather из конфигурационного файла.
    
    Файл конфигурации должен содержать секцию 'api' с ключом 'api_key', который будет 
    использован для запросов к OpenWeather.

    Параметры:
    filename (str): Путь к конфигурационному файлу. По умолчанию используется 
                    'requests/config.ini'. Этот файл должен быть в формате .ini и 
                    содержать необходимые данные для подключения.

    Возвращает:
    str: API-ключ, считанный из конфигурационного файла. Если ключ не найден, будет 
         вызвана ошибка при чтении файла.
    """
    # Создаем объект для чтения конфигурационного файла
    conf = configparser.ConfigParser()
    # Читаем файл конфигурации
    conf.read(filename)

    # Извлекаем API-ключ из секции 'api', под ключом 'api_key'
    my_api_key = conf.get('api', 'api_key')
    
    # Возвращаем считанный API-ключ
    return my_api_key

def get_weather_data(city="Moscow", api_key=""):
    """
    Получает данные о погоде для указанного города, отправляя запрос к OpenWeather API.

    В случае, если API-ключ не передан, функция автоматически загрузит его из конфигурационного файла.
    
    Параметры:
    city (str): Название города, для которого нужно получить данные о погоде.
                По умолчанию используется "Moscow". Название города чувствительно к регистру.
    api_key (str): API-ключ для подключения к OpenWeather API. Если ключ не передан, 
                   будет загружен из конфигурационного файла.

    Возвращает:
    dict или None: Если запрос успешен, возвращает данные о погоде в формате JSON.
                   Если возникла ошибка при запросе (например, неверный город или проблемы с API), 
                   возвращает None.
    """
    # Если API-ключ не был передан, загружаем его из конфигурации
    if api_key == "":
        api_key = get_api_key()

    # Формируем URL для запроса к OpenWeather API, добавляем параметры: город, ключ и единицы измерения
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric", "lang": "ru"}
    try:
        # Выполняем HTTP-запрос к OpenWeather API
        response = requests.get(url=url, params=params)
        
        # Проверяем статус ответа. Если статус не 200, будет выброшено исключение.
        response.raise_for_status()

        # Если запрос прошел успешно, возвращаем данные в формате JSON
        return response.json()

    except requests.exceptions.RequestException as e:
        # В случае ошибки при запросе выводим сообщение и возвращаем None
        print(f"Ошибка при запросе к API: {e}")
        return None

def extract_weather_info(data):
    """
    Извлекает важную информацию о погоде из ответа API.

    Данные о погоде содержат множество параметров, и эта функция извлекает наиболее
    важные из них, такие как температура, влажность, описание погоды и другие.
    
    Параметры:
    data (dict): Данные, полученные от OpenWeather API в формате JSON. Эти данные содержат информацию
                 о погоде в запрашиваемом городе.
    
    Возвращает:
    tuple или None: Кортеж с извлеченной информацией о погоде (город, температура, влажность, описание погоды, 
                     скорость ветра, давление). Если данные не могут быть извлечены, возвращается None.
    """
    # Проверяем, что данные о погоде были получены
    if data:
        # Извлекаем информацию из ответа API
        city_name = data['name']  # Название города
        temperature = data['main']['temp']  # Температура в градусах Цельсия
        humidity = data['main']['humidity']  # Влажность в процентах
        weather_description = data['weather'][0]['description']  # Описание погоды (например, "ясно")
        wind_speed = data['wind']['speed']  # Скорость ветра в м/с
        pressure = data['main']['pressure']  # Атмосферное давление в гПа

        # Возвращаем информацию как кортеж
        return (city_name, temperature, humidity, weather_description, wind_speed, pressure)
    
    # Если данные не были получены, возвращаем None
    return None

def get_weather_info_table(weather_info):
    """
    Формирует таблицу с информацией о погоде с использованием библиотеки PrettyTable.
    
    Параметры:
    weather_info (tuple): Кортеж с данными о погоде, который был извлечен из API.
    
    Возвращает:
    PrettyTable: Таблица с форматированными данными о погоде.
    """
    # Создаем объект таблицы PrettyTable
    table = PrettyTable()

    # Устанавливаем заголовки столбцов для таблицы
    table.field_names = ["Город", "Температура", "Влажность", "Описание", "Скорость ветра", "Давление"]

    # Добавляем строку с данными о погоде
    table.add_row(weather_info)

    # Возвращаем таблицу для вывода
    return table
