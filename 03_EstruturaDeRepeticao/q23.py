class Main:
    def Run(self):
        number = int(input('Insert an integer: '))

        (primeNumbers, divisionsCount) = self.GetPrimeNumbers(number)

        print('The prime numbers between 1 and {} are:'.format(number))
        print(primeNumbers)
        print('It was made {} divisions.'.format(divisionsCount))

    @staticmethod
    def GetPrimeNumbers(limitNumber):
        primeNumbers = []
        divisionsCount = 0

        for testedNumber in range(2, limitNumber + 1):
            isPrimeNumber = True
            for dividendNumber in range(2, testedNumber):
                divisionsCount += 1
                if (testedNumber % dividendNumber == 0):
                    isPrimeNumber = False

            if (isPrimeNumber):
                primeNumbers.append(testedNumber)

        return primeNumbers, divisionsCount


main = Main()
main.Run()
