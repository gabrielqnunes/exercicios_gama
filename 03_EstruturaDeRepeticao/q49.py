class Main:
    @classmethod
    def run(self):
        term_n = Input.handle_positive_int('Insert an integer number: ')
        self.print_result(term_n)

    @staticmethod
    def print_result(term_n: int) -> None:
        result = 'S = 1/1'
        term_m = 3
        total = 1
        for i in range(2, term_n + 1):
            result = '{} + {}'.format(
                result,
                '{}/{}'.format(i, term_m)
            )
            total += i / term_m
            term_m += 2
        print(result)
        print('S = {}'.format(total))


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
                print('The input must be an integer number greater than 0.')
        return user_input


main = Main()
main.run()
