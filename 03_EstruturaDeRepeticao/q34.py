class Main:
    @classmethod
    def run(self):
        number = self.handle_number_input()
        is_prime = self.check_is_prime_number(number)
        self.handle_messages(number, is_prime)

    @staticmethod
    def handle_number_input():
        number = 0
        is_first_iteration = True

        while number <= 0:
            if not is_first_iteration:
                print('The number must be an integer greater than 0.')

            try:
                number = int(input('Insert an integer number: '))
            except Exception:
                number = 0

            is_first_iteration = False

        return number

    @staticmethod
    def check_is_prime_number(number):

        for count in range(2, number):
            if number % 2 == 0:
                return False

        return True

    @staticmethod
    def handle_messages(number, is_prime):
        if is_prime:
            print('The number {} is prime.'.format(number))
        else:
            print('The number {} is not prime.'.format(number))


main = Main()
main.run()
