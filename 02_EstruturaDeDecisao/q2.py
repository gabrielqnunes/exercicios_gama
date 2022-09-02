class Main:
    def Run(self):
        number = float(input('Insert a number: '))

        print('The inserted number is {}.'
             .format(self.IsPositiveOrNegative(number)))

    @staticmethod
    def IsPositiveOrNegative(number):
        if(number >= 0):
            return 'positive'
        else:
            return 'negative'

main = Main()
main.Run()