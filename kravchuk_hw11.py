import pretty
import random

# Task 34. Создать класс Годзила. У данного класса должен быть атрибут - объем желудка.
# Написать для данного класса метод поедания людей. В данную функцию должен
# передаваться объем съеденного и соответственно уменьшаться место в желудке.
# Когда Годзила заполнит желудок на 90%, метод должен выводить надпись, что
# Годзила наелся и больше не может поедать людей.

pretty.pretty_task(34)

class Godzilla:

    volume_of_stomach = 1000

    def __init__(self,eaten_human_volume=0):
        self.eaten_human_volume = eaten_human_volume
        self.last_volume = Godzilla.volume_of_stomach

    def eat_humans(self):
        if self.last_volume - self.eaten_human_volume == 0.1*Godzilla.volume_of_stomach:
            print("Godzilla is full and can no longer eat people")

        else:
            self.last_volume -= self.eaten_human_volume




dinner = Godzilla()

while dinner.last_volume > 100:
    dinner.eaten_human_volume = random.randint(1,120)
    if dinner.last_volume - dinner.eaten_human_volume < 100:
        continue
    elif dinner.last_volume - dinner.eaten_human_volume == 100:
        print("Last human:", dinner.eaten_human_volume, "nym nym nym nym nym")
        dinner.eat_humans()
        break
    else:
        dinner.eat_humans()
        print("Human:",dinner.eaten_human_volume,"nym nym nym","Last volume:", dinner.last_volume)


