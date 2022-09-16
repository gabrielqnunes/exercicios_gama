from math import factorial
from multiprocessing.spawn import is_forking


class Main:
    @classmethod
    def run(self):
        number = self.handle_number_input()
        self.calculate_factorial(number)

    @staticmethod
    def handle_number_input():
        number = 0
        is_first_iteration = True
        while number <= 0:
            if not is_first_iteration:
                print('Number must be an integer grater than 0.')

            try:
                number = int(input('Insert a integer number: '))
            except Exception:
                number = 0

            is_first_iteration = False
        return number

    @staticmethod
    def calculate_factorial(number):

        final_message = '{}! ='.format(number)
        is_first_iteration = True

        for count in reversed(range(1, number + 1)):
            if is_first_iteration:
                final_message = final_message + ' ' + str(count)
                is_first_iteration = False
            else:
                final_message = final_message + ' . ' + str(count)

        final_message = '{} = {}'.format(final_message, factorial(number))

        print('Factorial of: {}'.format(number))
        print(final_message)


main = Main()
main.run()
