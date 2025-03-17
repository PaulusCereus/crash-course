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

    def get_template_cakes_url(self):
        """
        Извлечь значение для ключа 'template_cakes_url' из секции 'Urls' конфигурационного файла.

        Возвращает:
        str: Значение, ассоциированное с ключом 'template_cakes_url' в секции 'Urls'.
             В случае отсутствия ключа вызовет ошибку.
        """
        if self.is_file_loaded():
            try:
                return self.get_config().get("Urls", "template_cakes_url")
            except (configparser.NoSectionError, configparser.NoOptionError) as e:
                print(f"Ошибка при извлечении template_cakes_url: {e}")
        else:
            print("Конфигурационный файл не был загружен.")
        return None

    def read_file(self):
        """
        Прочитать конфигурационный файл.

        Проверяет наличие конфигурационного файла в текущей директории. Если файл существует,
        он загружается в объект конфигурации. В случае отсутствия файла выводится сообщение об ошибке.
        """
        # Проверяем, существует ли файл в текущей директории
        if not os.path.exists(self.get_filename()):
            print(f"Файла {self.get_filename()} нет в текущей папке")  # Выводим ошибку, если файла нет
        else:
            try:
                # Читаем конфигурационный файл
                self.get_config().read(self.get_filename())
                self.__file_loaded = True  # Устанавливаем флаг, что файл успешно считан
                print(f"Считали конфиг с файла {self.get_filename()}")  # Выводим сообщение, что файл считан
            except Exception as e:
                print(f"Ошибка при чтении конфигурационного файла: {e}")
                self.__file_loaded = False  # Устанавливаем флаг в False, если файл не был считан

if __name__ == "__main__":
    """
    Основная функция для тестирования работы с конфигурационным файлом.
    
    Создает экземпляр класса MyConfig, пытается прочитать конфигурационный файл и 
    извлекает некоторые значения из секций 'Requests' и 'Urls'.
    """
    # Создаем объект конфигурации
    conf = MyConfig()

    # Выводим значение 'cake_url', если оно было успешно считано
    cake_url = conf.get_cake_url()
    if cake_url:
        print(cake_url)

    # Выводим значение 'user_agent', если оно было успешно считано
    user_agent = conf.get_user_agent()
    if user_agent:
        print(user_agent)
