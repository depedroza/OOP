import random


class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.lenflight = 0

    def length_of_flight(self):
        self.lenflight = random.randint(1, 10)

    def get_lenflight(self):
        return self.lenflight
