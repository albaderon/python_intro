import pretty
import random

# Task 34. Создать класс Годзила. У данного класса должен быть атрибут - объем желудка.
# Написать для данного класса метод поедания людей. В данную функцию должен
# передаваться объем съеденного и соответственно уменьшаться место в желудке.
# Когда Годзила заполнит желудок на 90%, метод должен выводить надпись, что
# Годзила наелся и больше не может поедать людей.

pretty.pretty_task(34)

class Godzilla:


    PERSENT = 0.1

    def __init__(self,eaten_human_volume=0,volume_of_stomach = 1000):
        self.eaten_human_volume = eaten_human_volume
        self.volume_of_stomach = volume_of_stomach
        self.free_volume_space = volume_of_stomach

    def eat_humans(self,eat_human):
        self.free_volume_space -= eat_human


    def is_hungry(self):
        return self.free_volume_space > Godzilla.PERSENT * godzilla_1.volume_of_stomach




godzilla_1 = Godzilla()

while godzilla_1.is_hungry():
    godzilla_1.eaten_human_volume = random.randint(1,120)
    if godzilla_1.free_volume_space - godzilla_1.eaten_human_volume < Godzilla.PERSENT*godzilla_1.volume_of_stomach:
        continue
    else:
        godzilla_1.eat_humans(godzilla_1.eaten_human_volume)
        print("Human:",godzilla_1.eaten_human_volume,"nym nym nym","Last volume:", godzilla_1.free_volume_space)
        if not godzilla_1.is_hungry():
            print("Godzilla is full and can no longer eat people")


