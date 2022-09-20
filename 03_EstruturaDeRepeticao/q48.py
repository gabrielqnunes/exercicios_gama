class Main:
    @classmethod
    def run(self):
        reversed_number = self.handle_input()
        print('=> {}'.format(reversed_number))

    @staticmethod
    def handle_input() -> str:
        number = Input.handle_positive_int('Insert an integer number: ')
        reversedNumber = str(number)[::-1]

        return reversedNumber


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
