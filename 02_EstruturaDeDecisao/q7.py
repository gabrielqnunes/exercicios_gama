class Main:
    def Run(self):
        number1 = float(input('Insert the first number: '))
        number2 = float(input('Insert the second number: '))
        number3 = float(input('Insert the third number: '))

        print('The bigger number is {}.'
              .format(self.ReturnBigger(number1, number2, number3)))

        print('The smaller number is {}.'
              .format(self.ReturnSmaller(number1, number2, number3)))

    @staticmethod
    def ReturnBigger(number1, number2, number3):

        if (number1 >= number2 and number1 >= number3):
            return number1
        elif (number2 >= number1 and number2 >= number3):
            return number2
        else:
            return number3

    @staticmethod
    def ReturnSmaller(number1, number2, number3):
        if (number1 <= number2 and number1 <= number3):
            return number1
        elif (number2 <= number1 and number2 <= number3):
            return number2
        else:
            return number3


main = Main()
main.Run()
