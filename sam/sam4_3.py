from datetime import datetime
from time import sleep

def show_time():
    for i in range(5):
        now = datetime.now().strftime("%H:%M:%S")
        print(now)
        sleep(1)

if __name__ == "__main__":
    show_time()

#Изучение модуля datetime и time для "заморозки" на секунду
