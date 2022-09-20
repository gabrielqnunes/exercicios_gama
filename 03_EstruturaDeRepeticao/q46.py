from os import system
from statistics import mean


class Main:
    @classmethod
    def run(self):
        athlete = {"name": 'Begins'}
        while athlete["name"] != '':
            athlete = self.handle_athlete_input()
            if athlete["name"] != '':
                self.handle_print_result(athlete)

    @staticmethod
    def handle_athlete_input() -> dict:
        athlete = input('Atlhete: ').capitalize().strip()
        jumps = []
        if athlete != '':
            for i in range(1, 6):
                jump = Input.handle_positive_float('Jump {}: '.format(i))
                jumps.append(jump)
        return {"name": athlete, "jumps": jumps}

    @staticmethod
    def handle_print_result(athltete: dict) -> None:
        count = 1
        system('clear')
        print(80 * '=')
        print('||{:^76}||'.format('RESULT'))
        print(80 * '=')
        print('||{:^76}||'.format(
            'Athlete: {}'.format(athltete["name"])
        ))
        print(80 * '=')
        for jump in athltete["jumps"]:
            print('||{:^50}|{:^25}||'.format(
                'Jump {}'.format(count),
                '{:.2f} m'.format(jump)
            ))
            count += 1
        print(80 * '=')
        print('||{:^50}|{:^25}||'.format(
            'Best jump',
            '{:.2f} m'.format(max(athltete["jumps"]))
        ))
        athltete["jumps"].remove(max(athltete["jumps"]))
        print('||{:^50}|{:^25}||'.format(
            'Worst jump',
            '{:.2f} m'.format(min(athltete["jumps"]))
        ))
        athltete["jumps"].remove(min(athltete["jumps"]))
        print('||{:^50}|{:^25}||'.format(
            'Average of ramaining jumps',
            '{:.2f} m'.format(mean(athltete["jumps"]))
        ))
        print(80 * '=')
        athltete["jumps"].remove(min(athltete["jumps"]))
        print('||{:^50}|{:^25}||'.format(
            'FINAL RESULT',
            '{:.2f} m'.format(mean(athltete["jumps"]))
        ))
        print(80 * '=')


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
                print('Input must be a float number greater than or equal 0.')
        return user_input


main = Main()
main.run()
