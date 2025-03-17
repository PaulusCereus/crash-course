import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class MyWebdriver:
    """
    Класс для управления браузером с использованием Selenium WebDriver.
    
    Этот класс позволяет автоматизировать задачи, такие как открытие URL, получение исходного кода страницы и снятие скриншотов.
    """

    def __init__(self, headless=False):
        """
        Инициализация экземпляра класса WebDriver.
        
        Параметры:
        headless (bool): Если True, браузер будет работать в фоновом режиме (без GUI), иначе откроется окно браузера.
        """
        self.headless = headless  # Устанавливаем режим headless (без GUI)
        self.__driver = self._start_driver()  # Запускаем драйвер

    def _start_driver(self):
        """
        Настройка и запуск драйвера Chrome с необходимыми параметрами и опциями.

        Возвращает:
        webdriver.Chrome: Запущенный экземпляр браузера Chrome.
        """
        # Загружаем конфигурацию для использования кастомного User-Agent
        conf = config.MyConfig()
        options = Options()
        if self.headless:
            # Если режим headless, добавляем соответствующий флаг
            options.add_argument("--headless")
        # Отключаем некоторые параметры, чтобы избежать ошибок в headless-режиме
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"user-agent={conf.get_user_agent()}")  # Добавляем User-Agent из конфигурации

        # Запускаем Chrome с установленными опциями
        driver = webdriver.Chrome(options=options)
        return driver

    def get_driver(self):
        """
        Получаем экземпляр веб-драйвера.

        Возвращает:
        webdriver.Chrome: Экземпляр драйвера, который используется для управления браузером.
        """
        return self.__driver
