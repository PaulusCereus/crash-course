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
else:
    # Если запрос не был успешным, выводим сообщение об ошибке
    print(f"Не можем получить доступ к указанному ресурсу")
    # Выводим код состояния ответа для диагностики
    print(f"Результат запроса - {response.status_code}")
