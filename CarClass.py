from pyexpat import model


class Car:
    def __init__(self, yearModel, make, speed):
        self.__year_model = yearModel
        self.__make = make
        self.__speed = 0

    def accelerate(self, SPEEDUP):
        self.__speed += SPEEDUP

    def brake(self, SLOWDOWN):
        self.__speed += SLOWDOWN

    # def get_year_model(self):
    #   return self.__year_model

    # def get_make(self):
    #    return self.__make

    def get_speed(self):
        return self.__speed
