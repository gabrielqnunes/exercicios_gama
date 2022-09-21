class Main:
    @classmethod
    def run(self):
        integers = self.set_integers()
        evens = self.get_evens(integers)
        odds = self.get_odds(integers)

        print('The even numbers inserted are: {}'.format(evens))
        print('The odd numbers inserted are: {}'.format(odds))

    @staticmethod
    def set_integers() -> list:
        integers = []
        for i in range(1, 21):
            integer = Input.integer('Insert the {} integer: '.format(i))
            integers.append(integer)
        return integers

    @staticmethod
    def get_evens(integers: list) -> list:
        evens = []
        for integer in integers:
            if integer % 2 == 0:
                evens.append(integer)
        return evens

    @staticmethod
    def get_odds(integers: list) -> list:
        odds = []
        for integer in integers:
            if integer % 2 != 0:
                odds.append(integer)
        return odds


class Input:
    @staticmethod
    def integer(message: str) -> int:
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
