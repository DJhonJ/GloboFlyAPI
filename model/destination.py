class Destination():
    def __init__(self, city, country, description):
        self.__city = city
        self.__country = country
        self.__description = description

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def country(self):
        return self.__city

    @country.setter
    def country(self, country):
        self.__country = country

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description
