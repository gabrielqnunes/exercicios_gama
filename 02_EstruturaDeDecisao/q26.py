class Main:
    def Run(self):
        fuelType = input(
            'What fuel do you desire? (G - Gasoline / A - Alcohol)\n')

        quantity = float(input('How many liters do you want?\n'))

        price = self.CalculateFuelPrice(fuelType, quantity)

        print('The price will be {:.2f}.'.format(price))

    @staticmethod
    def CalculateFuelPrice(fuelType, quantity):
        gasolinePrice = 2.5
        alcoholPrice = 1.9

        if (fuelType.upper() == 'G'):
            return gasolinePrice * 0.96 * quantity if (quantity <= 20) else gasolinePrice * 0.94 * quantity

        if (fuelType.upper() == 'A'):
            return alcoholPrice * 0.97 * quantity if (quantity <= 20) else alcoholPrice * 0.95 * quantity


main = Main()
main.Run()
