import math

class Main:
    def Run(self):
        area = float(input('Insert the area to be painted in square meters: '))
        
        self.CalculateGallonsQuantity(area)
        
        self.CalculateCansQuantity(area)
        
        self.CalculateGallonsAndCansQuantity(area)
        
    @staticmethod
    def CalculateGallonsQuantity(area):
        paintRequired = area / 6
        paintCanQuantity = math.ceil(paintRequired / 18)
        totalPrice = paintCanQuantity * 80

        print('It will be required {} can(s) of paint.'.format(paintCanQuantity))
        print('Total price: AU$ {}'.format(totalPrice))
        
    @staticmethod
    def CalculateCansQuantity(area):
        paintRequired = area / 6
        paintCanQuantity = math.ceil(paintRequired / 3.6)
        totalPrice = paintCanQuantity * 25

        print('It will be required {} gallons(s) of paint.'.format(paintCanQuantity))
        print('Total price: AU$ {}'.format(totalPrice))

    @staticmethod
    def CalculateGallonsAndCansQuantity(area):
        paintRequired = area / 6
        paintCanQuantity = paintRequired // 18
        totalCanPrice = paintCanQuantity * 80

        paintRest = paintRequired % 18

        paintGallonQuantity = math.ceil(paintRest / 3.6)
        totalGallonPrice = paintGallonQuantity * 25

        totalPrice = totalGallonPrice + totalCanPrice

        print('It will be required {} can(s) of paint and {} gallon(s) of paint.'
            .format(paintCanQuantity, paintGallonQuantity))
        print('Total price: AU$ {}'.format(totalPrice))

main = Main()
main.Run()