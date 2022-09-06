class Main:
    def Run(self):
        number = int(input('Insert a number: '))

        print('The multiplication table for {} is:'.format(number))

        for count in range(1, 11):
            print('{} * {} = {}'.format(number, count, number * count))


main = Main()
main.Run()
