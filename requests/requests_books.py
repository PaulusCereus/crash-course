import requests
from prettytable import PrettyTable

def get_books_data(query="", num_results=5):
    """
    Функция для получения данных о книгах с использованием Google Books API.
    Выполняет HTTP-запрос к API и возвращает JSON-ответ с данными о книгах.

    Параметры:
    query (str): Строка запроса для поиска книг. По умолчанию пустая строка.
    num_results (int): Количество книг, которое необходимо вернуть. По умолчанию 5.

    Возвращает:
    dict: Словарь с данными о книгах или сообщение об ошибке.
    В случае ошибки в запросе, возвращается словарь с ключом 'error' и сообщением об ошибке.
    """
    # Формируем URL для запроса с параметрами query и num_results
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={num_results}"

    try:
        # Выполняем запрос к API
        response = requests.get(url)
        # Проверяем статус ответа (если статус не 200, вызовет исключение)
        response.raise_for_status()
        # Возвращаем JSON-ответ в виде словаря
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # В случае ошибки запроса, выводим сообщение и возвращаем словарь с ошибкой
        return {"error": f"Ошибка при запросе: {e}"}

def extract_books_info(data):
    """
    Извлекает информацию о книгах из данных, полученных от Google Books API.
    Обрабатывает данные в формате JSON и извлекает важную информацию о книгах.

    Параметры:
    data (dict): Данные, полученные от Google Books API в формате JSON.
    
    Возвращает:
    list: Список кортежей, каждый из которых содержит информацию о книге:
          (название, авторы, дата публикации, описание книги).
    Если в данных нет нужной информации, возвращаются значения по умолчанию.
    """
    books_info = []
    # Извлекаем все книги из данных
    for item in data.get('items', []):
        volume_info = item.get('volumeInfo', {})
        
        # Безопасно извлекаем информацию о книге, используя get()
        title = volume_info.get('title', 'Неизвестно')
        authors = ', '.join(volume_info.get('authors', ['Неизвестен автор']))
        published_date = volume_info.get('publishedDate', 'Неизвестна дата')
        description = volume_info.get('description', 'Описание отсутствует')
        
        # Добавляем информацию о книге в список
        books_info.append((title, authors, published_date, description))
    
    # Возвращаем список информации о книгах
    return books_info

def create_books_table(books_info):
    """
    Создает таблицу с информацией о книгах, используя PrettyTable.
    Каждая строка таблицы соответствует одной книге.

    Параметры:
    books_info (list): Список кортежей с информацией о книгах.

    Возвращает:
    PrettyTable: Объект PrettyTable с таблицей, содержащей информацию о книгах.
    """
    # Создаем объект таблицы с названиями столбцов
    table = PrettyTable()
    table.field_names = ["Название", "Авторы", "Дата публикации", "Описание"]
    # Настраиваем все разделительные линии между строками и столбцами
    table.hrules = 1
    # Настраиваем максимальную ширину для столбца
    table._max_width = {"Название": 15, "Авторы": 10, "Дата публикации": 7, "Описание": 70, }
    
    # Добавляем строки таблицы с информацией о книгах
    for info in books_info:
        table.add_row(info)
    
    # Возвращаем сформированную таблицу
    return table

def main():
    """
    Основная функция программы.
    Запрашивает у пользователя ввод для поиска книг, затем получает данные от API,
    извлекает информацию о книгах и выводит ее в виде таблицы.

    В случае ошибок, выводится сообщение об ошибке.
    """
    # Запрашиваем у пользователя ключевое слово для поиска
    query = input("Введите ключевое слово для поиска: ")

    # Запрашиваем количество книг для вывода
    try:
        num_results = int(input("Введите количество книг для извлечения: "))
    except ValueError:
        # В случае неверного ввода (не число), выводим ошибку и завершаем выполнение программы
        print("Ошибка: введите целое число для количества книг.")
        return

    # Получаем данные о книгах от API
    data = get_books_data(query=query, num_results=num_results)

    # Если в данных есть ошибка, выводим ее
    if 'error' in data:
        print(data['error'])
    else:
        # Извлекаем информацию о книгах
        books_info = extract_books_info(data)
        # Создаем таблицу с полученной информацией
        table = create_books_table(books_info)
        # Выводим таблицу
        print(table)
