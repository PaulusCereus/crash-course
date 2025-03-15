import configparser
import os

class MyConfig:
    """
    Класс для работы с конфигурационным файлом в формате .ini.

    Этот класс предоставляет методы для чтения конфигурационных файлов,
    извлечения различных секций и значений, а также для проверки существования
    конфигурационного файла в текущей директории.
    """

    def __init__(self, filename="flowwow/config.ini"):
        """
        Инициализация экземпляра класса MyConfig.
        
        Параметры:
        filename (str): Имя конфигурационного файла. По умолчанию 'config.ini'.
                        Этот файл должен быть в формате .ini и содержать секции с ключами.
        """
        self.__filename = filename  # Имя конфигурационного файла
        self.__config = configparser.ConfigParser()  # Объект для работы с конфигурационным файлом
        self.__file_loaded = False  # Флаг для проверки, что файл был успешно считан
        self.read_file()
    def get_filename(self):
        """
        Получить имя конфигурационного файла.

        Возвращает:
        str: Имя конфигурационного файла.
        """
        return self.__filename

    def get_filename(self):
        """
        Получить имя конфигурационного файла.

        Возвращает:
        str: Имя конфигурационного файла.
        """
        return self.__filename

    def get_config(self):
        """
        Получить объект конфигурации для работы с секциями и ключами.

        Возвращает:
        ConfigParser: Объект конфигурации для работы с секциями и значениями.
        """
        return self.__config

    def is_file_loaded(self):
        """
        Проверить, был ли успешно считан конфигурационный файл.

        Возвращает:
        bool: True, если файл был успешно считан, иначе False.
        """
        return self.__file_loaded

    def get_user_agent(self):
        """
        Извлечь значение для ключа 'user_agent' из секции 'Requests' конфигурационного файла.

        Возвращает:
        str: Значение, ассоциированное с ключом 'user_agent' в секции 'Requests'.
             В случае отсутствия ключа вызовет ошибку.
        """
        if self.is_file_loaded():
            try:
                return self.get_config().get("Requests", "user_agent")
            except (configparser.NoSectionError, configparser.NoOptionError) as e:
                print(f"Ошибка при извлечении user_agent: {e}")
        else:
            print("Конфигурационный файл не был загружен.")
        return None

    def get_cake_url(self):
        """
        Извлечь значение для ключа 'cake_url' из секции 'Urls' конфигурационного файла.

        Возвращает:
        str: Значение, ассоциированное с ключом 'cake_url' в секции 'Urls'.
             В случае отсутствия ключа вызовет ошибку.
        """
        if self.is_file_loaded():
            try:
                return self.get_config().get("Urls", "cake_url")
            except (configparser.NoSectionError, configparser.NoOptionError) as e:
                print(f"Ошибка при извлечении cake_url: {e}")
        else:
            print("Конфигурационный файл не был загружен.")
        return None
