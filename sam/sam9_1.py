class Tomato:
    #Статическая переменная - список стадий созревания томата
    states = ['отсутствует', 'цветение', 'зеленый', 'красный']

    def __init__(self, index, state = states[0]):
        self._index = index
        self._state = state

    def grow(self):
        """Переводит томат на следующую стадию созревания"""
        #Находим индекс текущей стадии
        current_index = self.states.index(self._state)
        #Проверяем, можно ли перейти на следующую стадию
        if current_index < len(self.states) - 1:
            self._state = self.states[current_index + 1]
            return True #Если томат вырос
        return False #Если томат созрел


    def is_ripe(self):
        """Проверяет, созрел ли томат"""
        return self._state == self.states[-1]

class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [] #Список томатов
        #Создает указанное кол-во томатов
        for i in range(num_tomatoes):
            tomato = Tomato(i + 1)
            self.tomatoes.append(tomato)

    def grow_all(self):
        """Переводит все томаты на кусте на следующую стадию созревания"""
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        """Проверяет, все ли томаты на кусте созрели"""
        if not self.tomatoes:
            return False
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
        return True

    def give_away_all(self):
        """Очищает куст от томатов"""
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        """Садовник работает - выращивает все томаты на кусте"""
        self._plant.grow_all()

    def harvest(self):
        """Собирает урожай, если все томаты созрели"""
        if self._plant.all_are_ripe():
            self._plant.give_away_all() #очищаем куст
        else:
            print(f"Не все томаты созрели {self.show_plant_status()}")

    def show_plant_status(self):
        """Показывает текущее состояние всех томатов на кусте"""
        print(f"Состояние куста у садовника {self.name}:")
        if not self._plant.tomatoes:
            print("Куст пуст (урожай собран)")
        else:
            #Выводим состояние каждого томата
            for tomato in self._plant.tomatoes:
                print(f"Томат {tomato._index}: {tomato._state}")
        print()

    @staticmethod
    def knowledge_base():
        print("=== Справка по садоводству ===")
        print("1. Томаты проходят стадии: отсутствует → цветение → зеленый → красный")
        print("2. Садовник должен работать (work()), чтобы томаты росли")
        print("3. Урожай можно собрать только когда все томаты красные")
        print("4. После сбора урожая куст очищается")


Gardener.knowledge_base()
bush = TomatoBush(3)
gardener = Gardener("Иван", bush)
gardener.show_plant_status()

# Цикл выращивания томатов
for day in range(1, 6):
    print(f"--- День {day} ---")
    gardener.work()
    if gardener.harvest():
        break   #если урожай собран - выходим из цикла
gardener.show_plant_status()