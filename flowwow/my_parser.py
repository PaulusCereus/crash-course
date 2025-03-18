import my_webdriver
import config
import json 
import os
import pandas as pd
from bs4 import BeautifulSoup

class MyParser:
    """
    Класс для парсинга веб-страниц с использованием веб-драйвера.

    Атрибуты:
        __driver (my_webdriver.MyWebdriver): Экземпляр веб-драйвера, который используется для работы с браузером.
        url (str): URL текущей веб-страницы, которую мы парсим.
        html_page (str): HTML-код текущей веб-страницы, полученный после её загрузки.

    Методы:
        get_driver(): Возвращает веб-драйвер.
        get_url(): Возвращает URL текущей страницы.
        get_html_page(): Возвращает HTML-код текущей страницы.
        get_page(url): Загружает страницу по указанному URL и сохраняет её HTML.
        get_page_title(): Извлекает заголовок страницы.
        get_product_category(): Возвращает категорию продукта.
        get_product_url(): Возвращает URL продукта.
        get_product_photo_url(): Извлекает URL фото продукта.
        get_product_name(): Извлекает название продукта.
        get_product_price(): Извлекает цену продукта.
        get_product_weight(): Извлекает вес продукта.
        get_product_added(): Извлекает информацию о дате добавления продукта.
        get_product_bought(): Извлекает количество покупок продукта.
        get_shop_name(): Извлекает название магазина.
        get_shop_url(): Извлекает URL магазина.
        get_all_info(): Собирает всю информацию о продукте и магазине в виде словаря.
        print_product_info(): Выводит собранную информацию из словаря в консоль.
        get_last_page_number(): Извлекает максимальное количество страниц
        get_product_links(): Извлекает ссылки на все карточки товаров
        save_products_info_to_json(): Проходит по всем тортам страницы и загружает данные в файл JSON
        save_info_to_excel(): Преобразует JSON в Excel
    """

    def __init__(self, headless=False):
        """
        Инициализирует экземпляр парсера.

        Аргументы:
            headless (bool): Флаг, который определяет, будет ли браузер работать в безголовом режиме.
                             Если True, браузер будет работать без визуального интерфейса.
                             По умолчанию False (т.е. браузер будет с интерфейсом).
        """
        # Создаем экземпляр веб-драйвера. В зависимости от флага headless, браузер может работать без интерфейса.
        self.__driver = my_webdriver.MyWebdriver(headless=headless)
        
        # Инициализация переменных для хранения URL и HTML-кода страницы
        self.url = ""
        self.html_page = ""

    def get_driver(self):
        """
        Возвращает текущий экземпляр веб-драйвера.

        Возвращает:
            my_webdriver.MyWebdriver: Экземпляр веб-драйвера.
        """
        return self.__driver

    def get_url(self):
        """
        Возвращает URL текущей страницы.

        Возвращает:
            str: URL текущей веб-страницы.
        """
        return self.url

    def get_html_page(self):
        """
        Возвращает HTML-код страницы, полученный после её загрузки.

        Возвращает:
            str: HTML-код страницы, сохранённый в переменной html_page.
        """
        return self.html_page

    def get_page(self, url):
        """
        Загружает веб-страницу по указанному URL и сохраняет её HTML-код.

        Этот метод:
        - Открывает страницу по переданному URL.
        - Получает HTML-код страницы.
        - Преобразует HTML-код в объект BeautifulSoup для дальнейшей работы с DOM.
        - Сохраняет URL и HTML-код в соответствующие атрибуты класса.
        - Завершается завершением работы веб-драйвера.

        Аргументы:
            url (str): URL страницы для загрузки.

        Примечание:
            После вызова этого метода атрибуты `url` и `html_page` будут содержать актуальные данные.
        """
        try:
            # Открываем URL через веб-драйвер
            self.get_driver().open_url(url=url)
            
            # Получаем HTML-код страницы через веб-драйвер
            self.html_page = BeautifulSoup(self.get_driver().get_page_source(), 'html.parser')
            
            # Сохраняем URL текущей страницы
            self.url = url
            
            # Закрываем веб-драйвер после получения данных
            self.get_driver().quit()
        # В случае ошибки выводим сообщение
        except Exception as e:
            print(f"Ошибка при загрузке страницы: {e}")
            # Очищаем переменные, если возникла ошибка
            self.url = ""
            self.html_page = None

    def get_page_title(self):
        """
        Извлекает заголовок (title) страницы, который находится в теге <title>.

        Этот метод:
        - Ищет тег <title> в HTML-странице.
        - Если тег <title> найден, возвращает его текстовое содержимое.
        - Если тег <title> не найден, возвращает строку "Без заголовка".

        Возвращает:
            str: Заголовок страницы, или "Без заголовка", если тег <title> не найден.
        """
        try:
            # Ищем тег <title> в HTML-коде страницы
            title_tag = self.html_page.find('title')
            
            # Если тег <title> найден, возвращаем его содержимое
            if title_tag:
                return title_tag.get_text()
            else:
                # Если тег <title> не найден, возвращаем дефолтное сообщение
                return "Без заголовка"
        # В случае ошибки выводим сообщение и возвращаем дефолтное значение
        except Exception as e:
            print(f"Ошибка при извлечении заголовка страницы: {e}")
            return "Ошибка при извлечении заголовка"

    def get_product_category(self):
        """
        Возвращает категорию продукта. Если ошибка, возвращает сообщение об ошибке.

        Возвращает:
            str: Категория продукта.
        """
        try:
            # Возвращаем категорию продукта, можно адаптировать под реальную структуру страницы
            return "Торт"
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем дефолтное значение
            print(f"Ошибка при извлечении категории продукта: {e}")
            return "Ошибка при извлечении категории"

    def get_product_url(self):
        """
        Возвращает URL страницы продукта.

        Возвращает:
            str: URL текущей страницы.
        """
        return self.url

    def get_product_photo_url(self):
        """
        Извлекает URL фото продукта.

        Этот метод:
        - Ищет все изображения с классом "main-image-content is-zoom".
        - Извлекает атрибут 'src' для первого найденного изображения.
        
        Возвращает:
            str: URL фото продукта.
        """
        try:
            # Ищем все изображения с классом "main-image-content is-zoom"
            photo_url = self.html_page.find_all("img", class_="main-image-content is-zoom")
            if photo_url:
                return photo_url[0]['src']  # Возвращаем ссылку на первое изображение
            else:
                return "Фото не найдено"  # Если фото не найдено, возвращаем дефолтное сообщение
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем дефолтное значение
            print(f"Ошибка при извлечении фото продукта: {e}")
            return "Ошибка при извлечении фото"

    def get_product_name(self):
        """
        Извлекает название продукта.

        Этот метод:
        - Ищет все элементы с классом "name-wrapper".
        - Возвращает текстовое содержимое первого найденного элемента.

        Возвращает:
            str: Название продукта.
        """
        try:
            # Ищем элементы с классом "name-wrapper" для извлечения названия продукта
            name = self.html_page.find_all("div", class_="name-wrapper")
            if name:
                return name[0].get_text().strip()  # Возвращаем текстовое содержимое
            else:
                return "Название не найдено"  # Если название не найдено, возвращаем дефолтное сообщение
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем дефолтное значение
            print(f"Ошибка при извлечении названия продукта: {e}")
            return "Ошибка при извлечении названия"

    def get_product_price(self):
        """
        Извлекает цену продукта.

        Этот метод:
        - Ищет все элементы с классом "footer-price".
        - Извлекает цену из первого найденного элемента.

        Возвращает:
            str: Цена продукта.
        """
        try:
            # Ищем элементы с классом "footer-price" для извлечения цены
            price = self.html_page.find_all("span", class_="footer-price")
            if price:
                return price[0].find("span").contents[0]  # Извлекаем цену
            else:
                return "Цена не указана"  # Если цена не указана, возвращаем дефолтное сообщение
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем дефолтное значение
            print(f"Ошибка при извлечении цены продукта: {e}")
            return "Ошибка при извлечении цены"

    def get_product_weight(self):
        """
        Извлекает вес продукта.

        Этот метод:
        - Ищет все элементы с классом "pre-line property-text".
        - Возвращает текстовое содержимое первого найденного элемента.

        Возвращает:
            str: Вес продукта.
        """
        try:
            # Ищем элементы с классом "pre-line property-text" для извлечения веса
            weight = self.html_page.find_all("p", class_="pre-line property-text")
            if weight:
                return weight[0].get_text().strip()  # Возвращаем вес
            else:
                return "Вес не указан"  # Если вес не указан, возвращаем дефолтное сообщение
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем дефолтное значение
            print(f"Ошибка при извлечении веса продукта: {e}")
            return "Ошибка при извлечении веса"

    def get_product_added(self):
        """
        Извлекает информацию о количестве людей, добавивших в подборку.

        Этот метод:
        - Ищет все элементы с классом "info-text".
        - Извлекает количество людей, кому понравился товар.

        Возвращает:
            str: Количество людей.
        """
        try:
            # Ищем элементы с классом "info-text" для извлечения даты добавления
            added = self.html_page.find_all("div", class_="info-text")
            if added:
                return added[2].get_text().strip().split()[0]  # Возвращаем дату добавления
            else:
                return "Количество не указано"  # Если дата не указана, возвращаем дефолтное сообщение
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем дефолтное значение
            print(f"Ошибка при извлечении количества людей, добавивших в подборку: {e}")
            return "Ошибка при извлечении количества людей"

    def get_product_rating(self):
        """
        Извлекает рейтинг продукта.

        Этот метод:
        - Ищет все элементы с классом "el-rate".
        - Извлекает значение атрибута 'aria-valuenow'.

        Возвращает:
            str: Рейтинг продукта.
        """
        try:
            # Ищем элементы с классом "el-rate" для извлечения рейтинга
            rat = self.html_page.find_all("div", class_="el-rate")
            if rat:
                return rat[0]['aria-valuenow']  # Возвращаем рейтинг
            else:
                return "Рейтинг не найден"  # Если рейтинг не найден, возвращаем дефолтное сообщение
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем дефолтное значение
            print(f"Ошибка при извлечении рейтинга продукта: {e}")
            return "Ошибка при извлечении рейтинга"

    def get_product_bought(self):
        """
        Извлекает количество покупок продукта.

        Этот метод:
        - Ищет все элементы с классом "shop-score".
        - Извлекает количество покупок из четвертого <span>.

        Возвращает:
            str: Количество покупок продукта.
        """
        try:
            # Ищем элементы с классом "shop-score" для извлечения количества покупок
            bought = self.html_page.find_all("p", class_="shop-score")
            if bought:
                spans = bought[0].find_all("span")
                if spans:
                    return spans[3].get_text().strip().split()[0]  # Извлекаем количество покупок
            return "Информация о покупках не найдена"  # Если информация не найдена, возвращаем дефолтное сообщение
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем дефолтное значение
            print(f"Ошибка при извлечении количества покупок продукта: {e}")
            return "Ошибка при извлечении покупок"

    def get_shop_name(self):
        """
        Извлекает название магазина.

        Этот метод:
        - Ищет все элементы с классом "shop-name".
        - Возвращает текстовое содержимое первого элемента.

        Возвращает:
            str: Название магазина.
        """
        try:
            # Ищем элементы с классом "shop-name" для извлечения названия магазина
            shop_name = self.html_page.find_all("p", class_="shop-name")
            if shop_name:
                return shop_name[0].get_text().strip()  # Возвращаем название магазина
            else:
                return "Название магазина не найдено"  # Если магазин не найден, возвращаем дефолтное сообщение
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем дефолтное значение
            print(f"Ошибка при извлечении названия магазина: {e}")
            return "Ошибка при извлечении названия магазина"

    def get_shop_url(self):
        """
        Извлекает URL магазина.

        Этот метод:
        - Ищет все элементы с классом "shop-link".
        - Извлекает атрибут 'href' для первого найденного элемента.

        Возвращает:
            str: URL магазина.
        """
        try:
            # Ищем элементы с классом "shop-link" для извлечения URL магазина
            shop_url = self.html_page.find_all("a", class_="shop-link")
            if shop_url:
                return shop_url[0]['href']  # Возвращаем URL магазина
            else:
                return "URL магазина не найден"  # Если магазин не найден, возвращаем дефолтное сообщение
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем дефолтное значение
            print(f"Ошибка при извлечении URL магазина: {e}")
            return "Ошибка при извлечении URL магазина"

    def get_all_info(self):
        """
        Собирает всю информацию о продукте и магазине в виде словаря.

        Возвращает:
            dict: Словарь с данными о продукте и магазине.
        """
        try:
            # Собираем всю информацию о продукте и магазине в словарь
            data = {
                "product_url": self.get_product_url(),
                'product_category': self.get_product_category(),
                'product_photo_url': self.get_product_photo_url(),
                "product_name": self.get_product_name(),
                "product_price": self.get_product_price(),
                "product_weight": self.get_product_weight(),
                "product_added": self.get_product_added(),
                "product_rating": self.get_product_rating(),
                "product_bought": self.get_product_bought(),
                "shop_name": self.get_shop_name(),
                "shop_url": self.get_shop_url()
            }
            return data
        except Exception as e:
            # В случае ошибки при сборе всей информации выводим сообщение и возвращаем пустой словарь
            print(f"Ошибка при сборе всей информации: {e}")
            return {}

    def print_product_info(self):
        """
        Форматирует и выводит информацию о продукте и магазине в читаемом виде.
        Этот метод использует данные, собранные методом get_all_info, и выводит их в понятном формате.

        Выводит:
            str: Читаемая и структурированная информация о продукте и магазине.
        """
        info = self.get_all_info()  # Получаем все данные о продукте и магазине

        # Выводим информацию в красивом и структурированном виде
        print("\nИнформация о продукте и магазине:")
        print("=" * 40)
        print(f"URL продукта: {info['product_url']}")
        print(f"Категория продукта: {info['product_category']}")
        print(f"Название продукта: {info['product_name']}")
        print(f"Цена продукта: {info['product_price']}")
        print(f"Вес продукта: {info['product_weight']}")
        print(f"Количество людей, добавивших товар: {info['product_added']}")
        print(f"Рейтинг продукта: {info['product_rating']}")
        print(f"Количество покупок продукта: {info['product_bought']}")
        print("-" * 40)
        print(f"URL магазина: {info['shop_url']}")
        print(f"Название магазина: {info['shop_name']}")
        print("=" * 40)

    def get_last_page_number(self):
        """
        Определяет номер последней страницы пагинации.

        Возвращает:
            int: Номер последней страницы.
        """
        try:
            # Ищем все элементы пагинации (ссылки с классом 'pagination-item')
            pagination = self.html_page.find_all('a', class_='pagination-item')
            if pagination:
                # Берем текст последнего элемента пагинации
                last_page = pagination[-1].get_text()
                # Преобразуем текст в число и возвращаем его
                return int(last_page)
            else:
                # Если элементы пагинации не найдены, предполагаем, что страниц одна
                return 1
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем 1
            print(f"Ошибка при определении последней страницы: {e}")
            return 1

    def get_product_links(self):
        """
        Извлекает все ссылки на карточки товаров с тортами.

        Возвращает:
            list: Список URL ссылок на карточки товаров.
        """
        try:
            # Находим все элементы <a> с классом 'product-card'
            product_elements = self.html_page.find_all('a', class_='product-card')
            # Формируем список ссылок, извлекая атрибут 'href' у каждого элемента, если он присутствует
            product_links = [element['href'] for element in product_elements if 'href' in element.attrs]
            return product_links
        except Exception as e:
            # В случае ошибки выводим сообщение и возвращаем пустой список
            print(f"Ошибка при извлечении ссылок на продукты: {e}")
            return []

    @staticmethod
    def save_products_info_to_json():
        """
        Сохраняет информацию по всем страницам с тортами постепенно в JSON-файл.
        """
        try:
            # Получаем URL шаблона для тортов из конфигурации
            conf = config.MyConfig()
            template_cakes_url = conf.get_template_cakes_url()
            
            # Создаём экземпляр парсера в headless-режиме
            cake_parser = MyParser(True)
            cake_parser.get_page(template_cakes_url)
            
            # Определяем номер последней страницы пагинации
            last_page_number = cake_parser.get_last_page_number()
            
            # Путь к файлу, где будет храниться информация о тортах
            file_path = 'flowwow/cakes.json'
            
            # Проверяем, существует ли файл; если нет, создаём его с пустым словарем
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump({}, f, ensure_ascii=False, indent=4)
            
            # Проходим по всем страницам пагинации
            for page_num in range(1, last_page_number + 1):
                # Создаем новый экземпляр парсера для каждой страницы
                current_cakes_page = MyParser(True)
                # Формируем URL текущей страницы (например, template URL + номер страницы)
                page_url = f"{template_cakes_url}{page_num}/"
                current_cakes_page.get_page(page_url)
                
                # Извлекаем ссылки на карточки продуктов с текущей страницы
                product_links = current_cakes_page.get_product_links()
                
                for link in product_links:
                    # Загружаем текущие данные из JSON-файла
                    with open(file_path, 'r', encoding='utf-8') as f:
                        all_products_info = json.load(f)
                    
                    # Если информация о данном продукте уже существует, пропускаем его
                    if link in all_products_info:
                        print(f"Информация о продукте {link} уже существует. Пропускаем.")
                        continue
                    
                    # Создаем экземпляр парсера для загрузки конкретного продукта
                    current_page = MyParser(True)
                    current_page.get_page(f"https://flowwow.com{link}")
                    
                    # Получаем информацию о продукте с помощью метода get_all_info()
                    product_info = current_page.get_all_info()
                    
                    # Добавляем информацию о продукте в словарь с данными
                    all_products_info[link] = product_info
                    
                    # Перезаписываем JSON-файл с обновленными данными
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(all_products_info, f, ensure_ascii=False, indent=4)
            
            print("Информация о продуктах успешно сохранена в cakes.json")
        
        except Exception as e:
            # В случае возникновения ошибки выводим сообщение
            print(f"Ошибка при сохранении информации о продуктах: {e}")

    @staticmethod
    def save_info_to_excel(json_file='flowwow/cakes.json', excel_file='flowwow/cakes.xlsx'):
        """
        Сохраняет информацию из JSON-файла в Excel-таблицу.

        Аргументы:
            json_file (str): Имя входного JSON-файла.
            excel_file (str): Имя выходного Excel-файла.
        """
        try:
            # Задаем путь к JSON-файлу с данными о тортах
            json_file = 'flowwow/cakes.json'

            # Открываем и загружаем данные из JSON-файла
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Преобразуем данные из словаря в список словарей для формирования таблицы
            data_list = []
            for key, value in data.items():
                # Формируем словарь с необходимыми полями
                product_data = {
                    'Ссылка на товар': value.get('product_url', ''),
                    'Категория': value.get('product_category', ''),
                    'Ссылка на первое фото': value.get('product_photo_url', ''),
                    'Название': value.get('product_name', ''),
                    'Цена': value.get('product_price', ''),
                    'Вес товара': value.get('product_weight', ''),
                    'Добавили в подборки': value.get('product_added', ''),
                    'Оценка магазина': value.get('product_rating', ''),
                    'Покупок': value.get('product_bought', ''),
                    'Магазин': value.get('shop_name', ''),
                    'Ссылка на магазин': value.get('shop_url', ''),
                }
                data_list.append(product_data)

            # Создаем DataFrame из списка словарей (требуется библиотека pandas)
            df = pd.DataFrame(data_list)

            # Определяем путь для сохранения Excel-файла
            excel_file = 'flowwow/cakes.xlsx'

            # Сохраняем DataFrame в Excel-файл с использованием движка openpyxl
            df.to_excel(excel_file, index=False, engine='openpyxl')

            print(f"Данные успешно сохранены в {excel_file}")
        except Exception as e:
            # В случае ошибки выводим сообщение
            print(f"Ошибка при сохранении информации в Excel: {e}")

if __name__ == "__main__":
    # Код для запуска сохранения данных в JSON-формат
    MyParser.save_products_info_to_json()
    
    # Код для формирования таблицы по содержимому JSON-файла
    MyParser.save_info_to_excel()
