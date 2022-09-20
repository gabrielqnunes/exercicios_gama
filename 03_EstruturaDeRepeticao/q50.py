class Main:
    @classmethod
    def run(self):
        n_term = Input.handle_positive_int('Insert the n term: ')
        self.print_result(n_term)

    @staticmethod
    def print_result(n_term: int) -> None:
        calculation = 'S = 1/1'
        calculation_result = 1

        for i in range(2, n_term + 1):
            calculation = '{} + 1/{}'.format(calculation, i)
            calculation_result += 1/i

        print(calculation)
        print('S = {}'.format(calculation_result))


class Input:
    @staticmethod
    def handle_positive_int(message: str) -> int:
        user_input = -1
        while user_input < 0:
            try:
                user_input = int(input(message))
            except Exception:
                user_input = -1
            if user_input < 0:
                print('Input must be an integer number greater than 0.')
        return user_input


main = Main()
main.run()
