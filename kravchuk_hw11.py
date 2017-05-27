import pretty
import random

# Task 34. Создать класс Годзила. У данного класса должен быть атрибут - объем желудка.
# Написать для данного класса метод поедания людей. В данную функцию должен
# передаваться объем съеденного и соответственно уменьшаться место в желудке.
# Когда Годзила заполнит желудок на 90%, метод должен выводить надпись, что
# Годзила наелся и больше не может поедать людей.

pretty.pretty_task(34)

class Godzilla:

    def __invert__(self,volume_of_stomach = 0):
        self.volume_of_stomach = volume_of_stomach


    def god_zilla(self):

        last_volume_of_stomach = self.volume_of_stomach

        while last_volume_of_stomach:
            human = random.randint(1, 120)

            if last_volume_of_stomach - human < 0.1*self.volume_of_stomach:
                continue


            elif last_volume_of_stomach - human == 0.1*self.volume_of_stomach:
                last_volume_of_stomach -= human
                print("Last human:", human, "Volume:", last_volume_of_stomach, "'nym nym nym'", end="\n")
                print("Godzilla is full and can no longer eat people")
                break

            else:
                last_volume_of_stomach -= human
                print("Human:", human, "Volume:", last_volume_of_stomach, "'nym nym nym'", end="\n")

a = Godzilla()
a.volume_of_stomach = 1000

a.god_zilla()