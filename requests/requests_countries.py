import requests
from prettytable import PrettyTable

def get_country_data(country_name):
    """
    Получает данные о стране из API RestCountries по заданному имени страны.
    
    Параметры:
    country_name (str): Название страны для поиска данных. 
    
    Возвращает:
    dict или None: Возвращает словарь с данными о стране в формате JSON, 
                    если запрос успешен. В случае ошибки возвращает None.
    """
    # Формируем URL для запроса, добавляя название страны в строку запроса
    url = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        # Выполняем GET-запрос к API
        response = requests.get(url=url)
        # Проверка, что запрос прошел успешно (статус код 200)
        response.raise_for_status()  # Если статус не 200, будет вызвана ошибка
        # Возвращаем данные в формате JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        # В случае ошибки запроса, выводим сообщение и возвращаем None
        print(f"Ошибка при запросе: {e}")
        return None
