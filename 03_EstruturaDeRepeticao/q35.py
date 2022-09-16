from sympy.ntheory.primetest import isprime


class Main:
    @classmethod
    def run(self):
        number = self.input_number_handler()
        primes = self.check_all_primes_until(number)
        print('The list of prime numbers between 1 and {} is:'.format(number))
        print(str(primes).replace('[', '').replace(']', ''))

    @staticmethod
    def input_number_handler():
        number = 0
        is_first_iteration = True

        while number <= 1:
            if not is_first_iteration:
                print('The input must be a number greater than 1.')

            try:
                number = int(input('Insert an integer number: '))
            except Exception:
                number = 0

            is_first_iteration = False

        return number

    @staticmethod
    def check_all_primes_until(number):
        primes = []

        for count in range(1, number):
            if isprime(count):
                primes.append(count)

        return primes


main = Main()
main.run()
