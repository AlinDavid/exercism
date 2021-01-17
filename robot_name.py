import random


class Robot:

    already_taken = list()

    def __init__(self):

        self.name = chr(random.randint(65, 91)) + chr(random.randint(65, 91)) + str(random.randint(0, 999)).zfill(3)
        if self.name in self.already_taken:
            self.reset()
        self.already_taken.append(self.name)

    def reset(self):
        self.__init__()
