class Main:
    def Run(self):
        number = int(input('Insert a number: '))
        isPrimeNumber = self.CheckIsPrimeNumber(number)
        self.HandleResultMessage(isPrimeNumber, number)

    @staticmethod
    def CheckIsPrimeNumber(number):
        isPrimeNumber = True

        if (number == 1):
            isPrimeNumber = False

        for count in range(2, number):
            if (number % count == 0):
                isPrimeNumber = False

        return isPrimeNumber

    @staticmethod
    def HandleResultMessage(isPrimeNumber, number):
        if (isPrimeNumber):
            print('The number {} is a prime number.'.format(number))
        else:
            print('The number {} is not a prime number.'.format(number))


main = Main()
main.Run()
