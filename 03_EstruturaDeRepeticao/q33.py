from statistics import mean


class Main:

    @classmethod
    def run(self):
        temperatures = self.handle_temperature_imputs()

        print('\nThe lowest temperature was {}.'.format(min(temperatures)))
        print('The greater temperature was {}.'.format(max(temperatures)))
        print("The temperature's average was {}.".format(mean(temperatures)))

    @staticmethod
    def handle_temperature_imputs():
        temperatures = []
        exit_input = False
        count = 1
        print("*Type 'exit' to quit*")
        while not exit_input:
            temperature = input(
                'Insert the temperature {} in celsius: '.format(count)).upper()
            try:
                temperatures.append(int(temperature))
                count += 1
            except Exception:
                if temperature == 'EXIT':
                    exit_input = True
                else:
                    print('Insert a integer number.')
        return temperatures


main = Main()
main.run()
