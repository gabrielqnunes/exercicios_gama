class Main:
    def Run(self):
        gender = input('Insert your gender: ')

        print('The inserted gender is {}.'
            .format(self.CheckGender(gender)))

    @staticmethod
    def CheckGender(gender):
        if (gender.upper() == 'M'):
            return 'M - Male'
        elif (gender.upper() == 'F'):
            return 'F - Female'
        else:
            return 'invalid gender'

main = Main()
main.Run()