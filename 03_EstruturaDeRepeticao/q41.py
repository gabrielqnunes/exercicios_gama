from os import system


class Main:
    @classmethod
    def run(self):
        debt = self.handle_input_positive_float("Insert the debt's value: ")
        debt_table = self.calculate_fees(debt)
        self.print_debt_table(debt_table)

    @staticmethod
    def calculate_fees(debt: float) -> list:
        debt_table = [
            {
                "debt": debt,
                "fees": 0,
                "portions": 1,
                "portion_value": debt
            },
            {
                "debt": debt * 1.1,
                "fees": debt * 0.1,
                "portions": 3,
                "portion_value": debt / 3
            },
            {
                "debt": debt * 1.15,
                "fees": debt * 0.15,
                "portions": 6,
                "portion_value": debt / 6
            },
            {
                "debt": debt * 1.2,
                "fees": debt * 0.2,
                "portions": 9,
                "portion_value": debt / 9
            },
            {
                "debt": debt * 1.25,
                "fees": debt * 0.25,
                "portions": 12,
                "portion_value": debt / 12
            },
        ]
        return debt_table

    @staticmethod
    def print_debt_table(debt_table: list) -> None:
        system('clear')
        print(80 * '=')
        print('||{:^76}||'.format('DEBT TABLE'))
        print(80 * '=')
        print('|| {:^18}|{:^18}|{:^18}|{:^17} ||'.format(
            'DEBT VALUE', 'FEES VALUE', 'PORTIONS', 'PORTION VALUE'
        ))
        for debt in debt_table:
            print('|| {:^18}|{:^18}|{:^18}|{:^17} ||'.format(
                '{:.2f}'.format(debt["debt"]), '{:.2f}'.format(
                    debt["fees"]), debt["portions"], '{:.2f}'.format(debt["portion_value"])
            ))
        print(80 * '=')

    @staticmethod
    def handle_input_positive_float(message: str) -> float:
        user_input = -1
        while user_input <= 0:
            try:
                user_input = float(input(message).replace(',', '.'))
            except Exception:
                user_input = -1
            if user_input <= 0:
                print('Input must be a float grater than 0.')
        return user_input


main = Main()
main.run()
