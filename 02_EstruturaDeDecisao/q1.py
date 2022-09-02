from re import I


class Main:
    def Run(self):
        num1 = float(input('Insert a number: '))
        num2 = float(input('Insert another number: '))

        print('The bigger number is {}.'
             .format(self.ReturnTheBiggerNumber(num1, num2)))

    @staticmethod
    def ReturnTheBiggerNumber(num1, num2):
        if (num1 > num2):
            return num1
        else:
            return num2

main = Main()
main.Run()