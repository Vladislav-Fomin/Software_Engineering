import time
import random

class RetryDecorator:
    def __init__(self, max_attempts=3, delay=1):
        self.max_attempts = max_attempts
        self.delay = delay

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for attempt in range(self.max_attempts):
                try:
                    print(f"Попытка {attempt + 1} из {self.max_attempts}...")
                    result = func(*args, **kwargs)
                    print("Успешно!")
                    return result
                except Exception as ex:
                    print(f"Ошибка: {ex}")
                    if attempt < self.max_attempts - 1:
                        print(f"Ждем {self.delay} сек...")
                        time.sleep(self.delay)
                    else:
                        print("Все попытки исчерпаны!")
                        raise

        return wrapper

retry = RetryDecorator(max_attempts=3, delay=1)

@retry
def connect_to_database():
    """Имитация ненадежного подключения к БД"""
    if random.random() < 0.7:  #шанс ошибки
        raise ConnectionError("Нет подключения к БД")
    return "Подключено к БД"

@retry
def download_file(url):
    """Имитация ненадежной загрузки"""
    if random.random() < 0.6:  #шанс ошибки
        raise TimeoutError("Таймаут загрузки")
    return f"Файл {url} загружен"

if __name__ == "__main__":
    connect_to_database()
    download_file("https://example.com/file.txt")
