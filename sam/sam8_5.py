class Dog:
    def make_sound(self):
        return "Гав"

class Cat:
    def make_sound(self):
        return "Мяу"

class Cow:
    def make_sound(self):
        return "МУУУУУУУУУ"

def produce_sound(animal):
    return animal.make_sound()

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(produce_sound(animal))