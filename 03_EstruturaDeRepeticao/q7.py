class Main:
    def Run(self):
        numbers = []

        for count in range(5):
            number = float(input('Insert a number: '))

            numbers.append(number)

        print('The biggest number inserted is {}.'.format(max(numbers)))


main = Main()
main.Run()
