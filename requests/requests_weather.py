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
