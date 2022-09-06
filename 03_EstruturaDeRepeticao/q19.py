class Main:
    def Run(self):
        numbersInput = None
        numbers = None
        isValidated = False
        isFirstIteration = True

        while (not isValidated):
            if (not isFirstIteration):
                print('The numbers must be between 0 and 1000.')

            isFirstIteration = False
            isValidated = True

            numbersInput = input('Insert a list of numbers: ')
            numbers = numbersInput.split()
            for index in range(len(numbers)):
                numbers[index] = int(numbers[index])
                if numbers[index] < 0 or numbers[index] > 1000:
                    isValidated = False

        print('The lowest number is {}.'.format(min(numbers)))
        print('The biggest number is {}.'.format(max(numbers)))
        print('The sum of all numbers is {}.'.format(sum(numbers)))


main = Main()
main.Run()
