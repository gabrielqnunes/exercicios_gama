from os import system


class Main:
    @classmethod
    def run(self):
        menu = self.get_menu()
        self.print_menu(menu)
        order = self.handle_order_input()
        self.print_order_total(order, menu)

    @staticmethod
    def handle_order_input() -> list:
        order = []
        meal_code = None
        quantity = 0
        while meal_code != 0:
            print('Insert 0 to (EXIT).')
            meal_code = Input.handle_positive_int("Insert the meal's code: ")
            while meal_code not in [0, 100, 101, 102, 103, 104, 105]:
                meal_code = Input.handle_positive_int(
                    "Insert a valid code: ")

            if meal_code != 0:
                quantity = Input.handle_positive_int(
                    "Insert how many meals you want: ")
                while quantity == 0:
                    quantity = Input.handle_positive_int(
                        "Insert a valid quantity: ")

                order.append(
                    {"code": meal_code, "quantity": quantity}
                )

        return order

    @staticmethod
    def print_order_total(order: list, menu: list) -> None:
        total = 0

        for item in order:
            for meal in menu:
                if item["code"] == meal["code"]:
                    item.update({"meal": meal["meal"]})
                    item.update({"price": meal["price"]})
                    break

        system('clear')
        print(80 * '=')
        print('||{:^76}||'.format('ORDER'))
        print(80 * '=')
        print('||{:^25}|{:^25}|{:^24}||'.format(
            'MEAL', 'CODE', 'PRICE'
        ))
        print(80 * '=')

        for item in order:
            print('||{:^25}|{:^25}|{:^24}||'.format(
                item["meal"], item["code"], '{:.2f} x {} = AU$ {:.2f}'.format(
                    item["price"], item["quantity"], item["price"] * item["quantity"])
            ))
            total += item["price"] * item["quantity"]

        print(80 * '=')
        print('||{:^26}{:^25}|{:^24}||'.format(
            '', '', 'TOTAL: AU$ {:.2f}'.format(total)
        ))
        print(80 * '=')

    @staticmethod
    def print_menu(menu: dict) -> None:
        system('clear')
        print(80 * '=')
        print('||{:^76}||'.format('MENU'))
        print(80 * '=')
        print('||{:^25}|{:^25}|{:^24}||'.format(
            'MEAL', 'CODE', 'PRICE'
        ))
        print(80 * '=')
        for item in menu:
            print('||{:^25}|{:^25}|{:^24}||'.format(
                item["meal"], item["code"], 'AU$ {:.2f}'.format(item["price"])
            ))
        print(80 * '=')

    @staticmethod
    def get_menu() -> dict:
        menu = [
            {
                "meal": 'HOT DOG',
                "code": 100,
                "price": 1.20
            },
            {
                "meal": 'GRILLED BREAD',
                "code": 101,
                "price": 1.30
            },
            {
                "meal": 'GRILLED BREAD WITH EGGS',
                "code": 102,
                "price": 1.50
            },
            {
                "meal": 'HAMBURGER',
                "code": 103,
                "price": 1.20
            },
            {
                "meal": 'CHEESEBURGUER',
                "code": 104,
                "price": 1.30
            },
            {
                "meal": 'SODA',
                "code": 105,
                "price": 1.00
            },
        ]
        return menu


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
