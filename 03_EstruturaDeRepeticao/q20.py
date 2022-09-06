from math import factorial


class Main:
    def Run(self):
        executeProgram = True

        while (executeProgram):
            number = self.HandleInputNumber()

            print('The factorial of {} is {}.'.format(
                number, factorial(number)))

            executeProgram = bool(input('Do you want to try again? '))

    @staticmethod
    def HandleInputNumber():
        number = -1
        isFirstIteration = True

        while (number not in range(17)):
            if (not isFirstIteration):
                print('The number must be between 0 and 16.')

            number = int(input('Insert a number: '))

            isFirstIteration = False

        return number


main = Main()
main.Run()
