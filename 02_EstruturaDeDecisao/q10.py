class Main:
    def Run(self):
        shift = input('What shift are you studying? ')

        print('{}, mister/miss(es)!'
              .format(self.ManageShiftMessage(shift)))

    @staticmethod
    def ManageShiftMessage(shift):
        if (shift.upper() == 'M'):
            return 'Good morning'
        elif (shift.upper() == 'A'):
            return 'Good afternoon'
        elif (shift.upper() == 'N'):
            return 'Good night'
        else:
            return 'Hello'


main = Main()
main.Run()
