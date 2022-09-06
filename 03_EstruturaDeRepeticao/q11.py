class Main:
    def Run(self):
        numbers = []
        initialNumber = int(input('Insert a number: '))
        endNumber = int(
            input('Insert a number bigger than the number before: '))

        print('The integers between {} and {} are:'
              .format(initialNumber, endNumber))

        for number in range(initialNumber + 1, endNumber):
            numbers.append(number)
            print(number)

        print('The sum of all these numbers is {}.'.format(sum(numbers)))


main = Main()
main.Run()
