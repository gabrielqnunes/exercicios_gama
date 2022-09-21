from os import system
from numpy import product


class Main:
    @classmethod
    def run(self):
        numbers = self.input_numbers()
        system('clear')
        print('The inserted numbers were: {}'.format(numbers))
        print('Sum: {}'.format(sum(numbers)))
        print('Product: {}'.format(product(numbers)))

    @staticmethod
    def input_numbers() -> list:
        numbers = []
        system('clear')
        for i in range(1, 6):
            number = Input.integer('Insert the {} number: '.format(i))
            numbers.append(number)
        return numbers


class Input:
    @staticmethod
    def integer(message: str) -> int:
        user_input = None
        while user_input == None:
            try:
                user_input = int(input(message))
            except Exception:
                user_input = None
            if user_input == None:
                print('Input must be an integer number.')
        return user_input


main = Main()
main.run()
