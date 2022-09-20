from os import system
from statistics import mean


class Main:
    @classmethod
    def run(self):
        athlete = self.handle_athlete_input()
        self.print_result(athlete)

    @staticmethod
    def handle_athlete_input() -> dict:
        athlete = str(input('Athlete: ')).capitalize().strip()
        scores = []
        for i in range(1, 8):
            score = Input.handle_positive_float(
                'Score {}: '.format(i)
            )
            scores.append(score)
        return {"name": athlete, "scores": scores}

    @staticmethod
    def print_result(athlete: dict) -> None:
        system('clear')
        print(60 * '=')
        print('||{:^56}||'.format('FINAL RESULT'))
        print(60 * '=')
        print('||{:^35}|{:^20}||'.format(
            'Athlete',
            athlete["name"]
        ))
        print(60 * '=')
        print('||{:^35}|{:^20}||'.format(
            'Best score',
            '{:.2f}'.format(max(athlete["scores"]))
        ))
        athlete["scores"].remove(max(athlete["scores"]))
        print('||{:^35}|{:^20}||'.format(
            'Worst score',
            '{:.2f}'.format(min(athlete["scores"]))
        ))
        athlete["scores"].remove(min(athlete["scores"]))
        print('||{:^35}|{:^20}||'.format(
            'Average of remaining scores',
            '{:.2f}'.format(mean(athlete["scores"]))
        ))
        print(60 * '=')


class Input:
    @staticmethod
    def handle_positive_float(message: str) -> float:
        user_input = -1
        while user_input < 0:
            try:
                user_input = float(input(message))
            except Exception:
                user_input = -1
            if user_input < 0:
                print('Input must be a float number greater than 0.')
        return user_input


main = Main()
main.run()
