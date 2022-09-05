from typing import final


class Main:
    def Run(self):
        strawberryQuantity = float(
            input('Insert the strawberry quantity in Kg: '))
        appleQuantity = float(input('Insert the apples quantity in Kg: '))

        finalPrice = self.CalculatePrice(strawberryQuantity, appleQuantity)

        print('The value to be paid will be AU${}.'.format(finalPrice))

    @staticmethod
    def CalculatePrice(strawberryQuantity, appleQuantity):
        strawberryPrice = 0
        applePrice = 0

        if (strawberryQuantity <= 5):
            strawberryPrice = 2.5 * strawberryQuantity
        else:
            strawberryPrice = 2.2 * strawberryQuantity

        if (appleQuantity <= 5):
            applePrice = 1.8 * appleQuantity
        else:
            applePrice = 1.5 * appleQuantity

        finalPrice = applePrice + strawberryPrice

        if (finalPrice > 25):
            return finalPrice * 0.9
        else:
            return finalPrice


main = Main()
main.Run()
