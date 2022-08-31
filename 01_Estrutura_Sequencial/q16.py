import math

class Main:
    def Run(self):
        area = float(input('Insert the area to be painted in square meters: '))
        paintRequired = area / 3
        paintCanQuantity = math.ceil(paintRequired / 18)
        totalPrice = paintCanQuantity * 80

        print('It will be required {} can(s) of paint.'.format(paintCanQuantity))
        print('Total price: AU$ {}'.format(totalPrice))

main = Main()
main.Run()