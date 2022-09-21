class Main:
    @classmethod
    def run(self):
        number_list = self.handle_list_input()
        print(f'The list inserted was {number_list}.')

    @staticmethod
    def handle_list_input() -> list:
        numbers_list = []
        for i in range(1, 6):
            number = Input.handle_int(f'Insert the {i} number: ')
            numbers_list.append(number)
        return numbers_list


class Input:
    @staticmethod
    def handle_int(message: str) -> int:
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
