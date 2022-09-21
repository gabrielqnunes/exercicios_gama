class Main:
    @classmethod
    def run(self):
        numbers_list = self.handle_list_input()
        print('The list in reverse is:')
        print(list(reversed(numbers_list)))

    @staticmethod
    def handle_list_input() -> list:
        numbers_list = []
        for i in range(1, 11):
            number = Input.handle_float(f'Insert the number in position {i}: ')
            numbers_list.append(number)
        return numbers_list


class Input:
    @staticmethod
    def handle_float(message: str) -> float:
        user_input = None
        while user_input == None:
            try:
                user_input = float(input(message))
            except Exception:
                user_input = None
            if user_input == None:
                print('Input must be a float number.')
        return user_input


main = Main()
main.run()
