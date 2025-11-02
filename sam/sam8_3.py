class Book:
    def __init__(self, author, name):
        self.author = author
        self.name = name

    def info(self):
        print(f"Книгу {self.name} написал {self.author}")

class AudioBook(Book):
    def __init__(self, author, name, voice, duration):
        super().__init__(author, name)
        self.voice = voice
        self.duration = duration

    def audio_info(self):
        print(f"Книга {self.name} автора {self.author} в озвучке {self.voice} длится {self.duration} минут")

my_audio_book = AudioBook("Лев Толстой", "Война и мир", "Гоблина", 4000)
my_audio_book.info()
my_audio_book.audio_info()
