from os import system
from statistics import mean


class Main:
    @classmethod
    def run(self):
        cities_data = self.handle_cities_data_input()
        less_accidents_city = self.get_less_accidents_city(cities_data)
        most_accidents_city = self.get_most_accidents_city(cities_data)
        qtd_vehicles = self.get_vehicles_qtd(cities_data)
        qtt_accidents = self.get_accidents_qtd(cities_data)

        system('clear')

        print('City with less accidents: {} with {} accidents'.format(
            less_accidents_city["code"], less_accidents_city["qtd_transit_accidents_with_victims"]
        ))
        print('City with most accidents: {} with {} accidents'.format(
            most_accidents_city["code"], most_accidents_city["qtd_transit_accidents_with_victims"]
        ))

        print("The vehicle's average among the cities is: {}".format(
            mean(qtd_vehicles)
        ))

        print("The accident's average in cities with less than 2000 tour cars is: {}".format(
            mean(qtt_accidents)
        ))

    @classmethod
    def handle_cities_data_input(self) -> list:
        cities = []
        for index in range(1, 6):
            system('clear')
            city = {
                "code": None, "qtd_tour_vehicles": None, "qtd_transit_accidents_with_victims": None
            }
            city["code"] = self.handle_input_int(
                "Insert the {} city's code: ".format(index))
            city["qtd_tour_vehicles"] = self.handle_input_positive_int(
                "Insert the {} city's tour vehicles's quantity: ".format(index))
            city["qtd_transit_accidents_with_victims"] = self.handle_input_positive_int(
                "Insert the {} city's transit accidents with victims's quantity: ".format(index))
            cities.append(city)
        return cities

    @staticmethod
    def get_less_accidents_city(cities: list) -> dict:
        less_accidents_city = {
            "qtd_transit_accidents_with_victims": float('inf')}
        for city in cities:
            if city["qtd_transit_accidents_with_victims"] < less_accidents_city["qtd_transit_accidents_with_victims"]:
                less_accidents_city = city
        return less_accidents_city

    @staticmethod
    def get_most_accidents_city(cities: list) -> dict:
        most_accidents_city = {"qtd_transit_accidents_with_victims": -1}
        for city in cities:
            if city["qtd_transit_accidents_with_victims"] > most_accidents_city["qtd_transit_accidents_with_victims"]:
                most_accidents_city = city
        return most_accidents_city

    @staticmethod
    def get_vehicles_qtd(cities: list) -> list:
        vehicles = []
        for city in cities:
            vehicles.append(city["qtd_tour_vehicles"])
        return vehicles

    @staticmethod
    def get_accidents_qtd(cities: list) -> list:
        accidents_qtds = []
        for city in cities:
            if city["qtd_tour_vehicles"] <= 2000:
                accidents_qtds.append(
                    city["qtd_transit_accidents_with_victims"])
        return accidents_qtds

    @staticmethod
    def handle_input_int(message: str) -> int:
        user_input = None
        while user_input == None:
            try:
                user_input = int(input(message))
            except Exception:
                user_input = None
            if user_input == None:
                print('The input must be an integer number.')
        return user_input

    @staticmethod
    def handle_input_positive_int(message: str) -> int:
        user_input = -1
        while user_input < 0:
            try:
                user_input = int(input(message))
            except Exception:
                user_input = -1

            if user_input < 0:
                print('The input must be an integer greater than 0.')
        return user_input


main = Main()
main.run()
