class Book:
    def __init__(self, author, name):
        self.author = author
        self.name = name

    def info(self):
        print(f"Книгу {self.name} написал {self.author}")


my_book = Book("Лев Толстой","Война и мир")
my_book.info()
