class Main:
    def Run(self):
        number = int(input('Insert a number: '))
        (isPrimeNumber, divisibleNumbers) = self.CheckIsPrimeNumber(number)
        self.HandleResultMessage(isPrimeNumber, number, divisibleNumbers)

    @staticmethod
    def CheckIsPrimeNumber(number):
        isPrimeNumber = True
        divisibleNumbers = [1, number]

        if (number == 1):
            isPrimeNumber = False

        for count in range(2, number):
            if (number % count == 0):
                divisibleNumbers.append(count)
                isPrimeNumber = False

        divisibleNumbers.sort()

        return isPrimeNumber, divisibleNumbers

    @staticmethod
    def HandleResultMessage(isPrimeNumber, number, divisibleNumbers):
        if (isPrimeNumber):
            print('The number {} is a prime number.'.format(number))
        else:
            print('The number {} is not a prime number.'.format(number))
            print("It's divisible per: {}".format(divisibleNumbers))


main = Main()
main.Run()
