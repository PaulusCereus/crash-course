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
