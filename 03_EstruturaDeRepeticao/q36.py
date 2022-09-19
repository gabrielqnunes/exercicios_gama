class Main:
    @classmethod
    def run(self):
        number = self.handle_int_input('Insert the number: ')
        first_multiplication_number = self.handle_int_input(
            'Insert the first multiplication number: '
        )
        last_multiplication_number = 0

        while last_multiplication_number < first_multiplication_number:
            last_multiplication_number = self.handle_int_input(
                'Insert the last multiplication number: '
            )

        self.print_multiplication_table(
            number, first_multiplication_number, last_multiplication_number)

    @staticmethod
    def handle_int_input(input_phrase):
        number = 0
        is_first_iteration = True

        while number <= 0:
            if not is_first_iteration:
                print('The input must be an integer greater than 0.')

            try:
                number = int(input(input_phrase))
            except Exception:
                number = 0

            is_first_iteration = False

        return number

    @staticmethod
    def print_multiplication_table(
        number,
        first_multiplication_number,
        last_multiplication_number
    ):
        print(34 * '=')
        print('||{:^30}||'.format('MULTIPLICATION TABLE'))
        print(34 * '=')
        for count in range(
            first_multiplication_number, last_multiplication_number + 1
        ):
            print('||{:^30}||'.format(
                '{} x {} = {}'.format(count, number, count * number)
            ))
        print(34 * '=')


main = Main()
main.run()
