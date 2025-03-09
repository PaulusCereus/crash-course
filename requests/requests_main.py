# Импортируем библиотеку requests для работы с HTTP-запросами
import requests

# Определяем URL-адрес API, с которого будем получать данные
URL = "https://official-joke-api.appspot.com/random_joke"

# Отправляем GET-запрос по указанному URL
response = requests.get(url=URL)

# Проверяем, был ли запрос успешным (код состояния 200)
if response.ok:
    # Выводим объект ответа для общего ознакомления
    print(f"Ответ response - {response}\n")

    # Выводим статус-код ответа
    print(f"Статус-код ответа - {response.status_code}\n")

    # Выводим текстовое содержимое ответа
    print(f"Текст ответа - {response.text}\n")

    # Преобразуем ответ в формат JSON
    resp_json = response.json()

    # Выводим JSON-ответ для анализа
    print(f"JSON ответа - {resp_json}\n")

    # Извлекаем и выводим отдельные данные из JSON-ответа
    print(f"""
    Номер шутки: {resp_json['id']}
    Тип шутки: {resp_json['type']}
    Сетап: {resp_json['setup']}
    Панчалайн: {resp_json['punchline']}
    """)
else:
    # Если запрос не был успешным, выводим сообщение об ошибке
    print(f"Не можем получить доступ к указанному ресурсу")
    # Выводим код состояния ответа для диагностики
    print(f"Результат запроса - {response.status_code}")