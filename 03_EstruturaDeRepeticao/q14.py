class Main:
    def Run(self):
        numbers = self.HandleInputNumbers()
        evenNumbersQuantity = self.GetEvenNumbersQuantity(numbers)
        oddNumbersQuantity = self.GetOddNumbersQuantity(numbers)

        print('There are:')
        print('{} even numbers.'.format(evenNumbersQuantity))
        print('{} odd numbers.'.format(oddNumbersQuantity))

    @staticmethod
    def HandleInputNumbers():
        numbers = []

        print('Insert ten integers:')
        for count in range(10):
            number = int(input(''))
            numbers.append(number)

        return numbers

    @staticmethod
    def GetEvenNumbersQuantity(numbers):
        evenNumbersQuantity = 0
        for number in numbers:
            if (number % 2 == 0):
                evenNumbersQuantity += 1
        return evenNumbersQuantity

    @staticmethod
    def GetOddNumbersQuantity(numbers):
        oddNumbersQuantity = 0
        for number in numbers:
            if (number % 2 != 0):
                oddNumbersQuantity += 1
        return oddNumbersQuantity


main = Main()
main.Run()
