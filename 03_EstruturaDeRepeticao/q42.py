from os import system


class Main:
    @classmethod
    def run(self):
        values_table = self.handle_input()
        self.print_values_table(values_table)

    @classmethod
    def handle_input(self) -> dict:
        values_table = {
            "0_to_25": 0, "26_to_50": 0, "51_to_75": 0, "76_to_100": 0
        }
        user_input = 0

        while user_input >= 0:
            system('clear')
            print(40 * '=')
            print('||{:^36}||'.format('INPUT'))
            print(40 * '=')
            user_input = self.handle_input_int('Insert a number: ')

            if user_input in range(26):
                values_table["0_to_25"] += 1
            elif user_input in range(26, 51):
                values_table["26_to_50"] += 1
            elif user_input in range(51, 76):
                values_table["51_to_75"] += 1
            elif user_input in range(76, 101):
                values_table["76_to_100"] += 1
        return values_table

    @staticmethod
    def print_values_table(values_table: dict) -> None:
        system('clear')
        print(40 * '=')
        print('||{:^36}||'.format('VALUES TABLE'))
        print(40 * '=')
        print('||{:^36}||'.format(
            ' [0-25]: {}'.format(values_table["0_to_25"])
        ))
        print('||{:^36}||'.format(
            '[26-50]: {}'.format(values_table["26_to_50"])
        ))
        print('||{:^36}||'.format(
            '[51-75]: {}'.format(values_table["51_to_75"])
        ))
        print('||{:^36}||'.format(
            '[76-100]: {}'.format(values_table["76_to_100"])
        ))
        print(40 * '=')

    @staticmethod
    def handle_input_int(message: str) -> int:
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
