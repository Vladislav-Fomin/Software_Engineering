class Book:
    def __init__(self, author, name, rating, price):
        self.author = author
        self.name = name
        self._rating = rating
        self.__price = price

    def info(self):
        print(f"Книгу {self.name} написал {self.author}. Рейтинг {self._rating}. Книга стоит {self.__price}")


my_book = Book("Лев Толстой","Война и мир", 4.2, 780)
my_book.info()
print(my_book._rating)
