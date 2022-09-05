class Main:
    def Run(self):
        year = int(input('Insert a year: '))

        if (self.CheckLeapYear(year)):
            print('{} is a leap year.'.format(year))
        else:
            print('{} is not leap year.'.format(year))

    @staticmethod
    def CheckLeapYear(year):
        if (year % 4 == 0):
            return True
        else:
            return False


main = Main()
main.Run()
