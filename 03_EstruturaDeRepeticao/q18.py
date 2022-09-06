class Main:
    def Run(self):
        numbersInput = input('Insert a list of numbers: ')
        numbers = numbersInput.split()
        for index in range(len(numbers)):
            numbers[index] = int(numbers[index])

        print('The lowest number is {}.'.format(min(numbers)))
        print('The biggest number is {}.'.format(max(numbers)))
        print('The sum of all numbers is {}.'.format(sum(numbers)))


main = Main()
main.Run()
