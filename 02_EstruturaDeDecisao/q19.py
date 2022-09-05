class Main:
    def Run(self):
        number = int(input('Insert a number: '))
        hundreds = self.HandleHundreds(number)
        number = number % 100
        tens = self.HandleTens(number)
        number = number % 10
        units = self.HandleUnits(number)

        print(hundreds, tens, units)

    @staticmethod
    def HandleHundreds(number):
        hundreds = number // 100

        if (hundreds == 0):
            return ''
        elif (hundreds == 1):
            return '1 hundred'
        else:
            return '{} hundreds'.format(hundreds)

    @staticmethod
    def HandleTens(number):
        tens = number // 10

        if (tens == 0):
            return ''
        elif (tens == 1):
            return '1 ten'
        else:
            return '{} tens'.format(tens)

    @staticmethod
    def HandleUnits(number):
        if (number == 0):
            return ''
        elif (number == 1):
            return '1 unit'
        else:
            return '{} units'.format(number)


main = Main()
main.Run()
