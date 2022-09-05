class Main:
    def Run(self):
        number = float(input('Insert a number: '))

        if (number % 2 == 1):
            print('The number {} is odd.'.format(number))
        else:
            print('The number {} is even.'.format(number))


main = Main()
main.Run()
