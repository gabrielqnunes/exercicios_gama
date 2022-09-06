class Main:
    def Run(self):
        initialNumber = int(input('Insert a number: '))
        endNumber = int(
            input('Insert a number bigger than the number before: '))

        print('The integers between {} and {} are:'
              .format(initialNumber, endNumber))

        for number in range(initialNumber + 1, endNumber):
            print(number)


main = Main()
main.Run()
