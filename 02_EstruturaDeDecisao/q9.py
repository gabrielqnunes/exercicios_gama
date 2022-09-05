class Main:
    def Run(self):
        numbers = []
        numbers.append(float(input('Insert the first number: ')))
        numbers.append(float(input('Insert the second number: ')))
        numbers.append(float(input('Insert the third number: ')))

        numbers.sort(reverse=True)

        print('The numbers in descending order are {}.'.format(numbers))


main = Main()
main.Run()
