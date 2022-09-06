from statistics import mean


class Main:
    def Run(self):
        numbers = []

        for count in range(5):
            number = float(input('Insert a number: '))
            numbers.append(number)

        print('The sum of the inserted numbers is {:.2f}.'.format(
            sum(numbers)))
        print('The mean of the inserted numbers is {:.2f}.'.format(
            mean(numbers)))


main = Main()
main.Run()
