class Main:
    def Run(self):
        number = int(input('Insert a integer: '))

        factorialResult = self.CalculateFactorial(number)

        print('The factorial of {} is {}.'.format(number, factorialResult))

    @staticmethod
    def CalculateFactorial(number):
        result = 1
        for number in range(1, number + 1):
            result *= number
        return result


main = Main()
main.Run()
