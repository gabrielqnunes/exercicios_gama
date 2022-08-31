class Main:
    def Run(self):
        height = float(input('Insert your height: '))
        gender = input('Insert your gender (M/F): ')

        idealWeight = self.CalculateIdealWeight(height, gender)

        print('Your ideal weight is {}'.format(idealWeight))

    @staticmethod
    def CalculateIdealWeight(height, gender):
        if (gender == 'M'):
            return (72.7 * height) - 58
        elif (gender == 'F'): 
            return(62.1 * height) - 44.7
        else:
            return 0
            
main = Main()
main.Run()
