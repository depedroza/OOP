class Item:
    def __init__(self, desc, inv, price):
        self.__description = desc
        self.__inventory = inv
        self.__price = price

    def set_description(self, desc):
        self.__description = desc

    def set_inventory(self, inv):
        self.__inventory = inv

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_inventory(self):
        return self.__inventory

    def get_price(self):
        return self.__price
