class Main:
    def Run(self):
        number = int(input('Insert a number: '))
        exponent = int(input('Insert a number to be the exponent: '))

        print('{} to the power of {} is {}.'
              .format(number, exponent, self.ToThePowerOf(number, exponent)))

    @staticmethod
    def ToThePowerOf(number, exponent):
        result = number
        for count in range(exponent - 1):
            result *= number
        return result


main = Main()
main.Run()
