class Main:
    def Run(self):
        number = float(input('Insert a number: '))

        if (float(number) == int(number)):
            print('The number {} is integer.'.format(int(number)))
        else:
            print('The number {} is float.'.format(number))


main = Main()
main.Run()
