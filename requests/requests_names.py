# Импортируем библиотеку requests для выполнения HTTP-запросов
import requests

# URL-адреса для различных API, которые будем использовать для получения данных о поле, возрасте и национальности
URL_GENDER = "https://api.genderize.io"
URL_AGE = "https://api.agify.io"
URL_NATIONALITY = "https://api.nationalize.io"

def get_all_by_name():
    """
    Функция запрашивает у пользователя имя и использует три различных API для получения информации:
    1. API Genderize для определения пола на основе имени.
    2. API Agify для получения приблизительного возраста по имени.
    3. API Nationalize для определения вероятных стран происхождения на основе имени.
    
    Для каждого из этих API отправляется запрос, и выводятся результаты в консоль.
    
    Параметры:
    - Нет.

    Возвращаемое значение:
    - Нет. Функция выводит информацию в консоль, но ничего не возвращает.
    """
    # Запрашиваем у пользователя имя, удаляя возможные лишние пробелы в начале и в конце строки
    user_name = input("Введите имя для проверки: ").strip()
    
    # Проверка, что имя не пустое
    if not user_name:  
        # Если имя пустое, выводим ошибку
        print("Ошибка: вы не ввели имя.")
        # Завершаем выполнение функции, так как без имени запросить данные невозможно
        return
    
    # Параметры для запросов, передаваемые в API. Каждое имя будет передано в запрос как параметр "name".
    params = {"name": user_name}

    try:
        # Выполняем запросы к API для получения данных о поле, возрасте и национальности.
        # Запрос на получение пола
        response_gender = requests.get(url=URL_GENDER, params=params)
        # Запрос на получение возраста
        response_age = requests.get(url=URL_AGE, params=params)
        # Запрос на получение национальности
        response_nationality = requests.get(url=URL_NATIONALITY, params=params)

        # Проверяем, были ли запросы успешными. Если нет, метод raise_for_status() вызовет исключение.
        response_gender.raise_for_status()
        response_age.raise_for_status()
        response_nationality.raise_for_status()

        # Преобразуем ответы от API в формат JSON (словарь), чтобы работать с данными
        resp_json_gender = response_gender.json()
        resp_json_age = response_age.json()
        resp_json_nationality = response_nationality.json()

        # Выводим результаты пользователю:
        # Показываем, какой пол вероятен для введённого имени с точностью до двух знаков после запятой
        print(f"\nВы ввели имя - {user_name}")
        print(f"{user_name} является {resp_json_gender['gender']} с вероятностью {resp_json_gender['probability']:.2f}")
        
        # Примерный возраст
        print(f"{user_name} примерно {resp_json_age['age']} лет.")
        
        # Возможные страны происхождения
        print(f"{user_name} может быть из:")
        for country_info in resp_json_nationality['country']:
            # Для каждого результата по странам выводим страну и вероятность (с точностью до двух знаков)
            print(f"Страна: {country_info['country_id']} с вероятностью {country_info['probability']:.2f}")

    except requests.exceptions.RequestException as e:
        # Обрабатываем ошибки, связанные с запросами (например, если API не доступен)
        print(f"Ошибка запроса: {e}")
    except KeyError as e:
        # Обрабатываем ошибки, если в ответе API отсутствуют ожидаемые ключи
        print(f"Ошибка в данных API: отсутствует ключ {e}")
    except Exception as e:
        # Обрабатываем все остальные ошибки, которые могут возникнуть (например, ошибки форматирования)
        print(f"Произошла непредвиденная ошибка: {e}")

# Запуск программы
if __name__ == "__main__":
    get_all_by_name()  # Вызов основной функции для получения данных по введённому имени