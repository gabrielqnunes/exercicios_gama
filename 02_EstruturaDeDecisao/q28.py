class Main:
    def Run(self):
        meatType = int(input('''
        1. Double filet
        2. Alcatra
        3. Picanha
        Insert the meat type: 
        '''))
        quantity = float(input('''
        Insert the quantity in Kg: 
        '''))
        paymentType = int(input('''
        1. In Cash
        2. Credit Card
        3. Credit Card Tabajaras
        Insert the payment type: 
        '''))

        price = self.CalculatePrice(meatType, quantity)
        priceWithDiscount = 0

        if (paymentType == 3):
            priceWithDiscount = price * 0.95

        print('''
        ============================
                FISCAL NOTE
        ============================
        Meat type       : {}
        Quantity in Kg  : {}
        Price           : AU${:.2f}
        Payment type    : {}
        Discount        : AU${:.2f}
        =============================
        Total           : AU${:.2f}
        =============================
        '''.format(meatType, quantity, price, paymentType, price - priceWithDiscount, priceWithDiscount))

    @staticmethod
    def CalculatePrice(meatType, quantity):
        finalPrice = 0

        if (quantity <= 5):
            if (meatType == 1):
                finalPrice = quantity * 4.9
            elif (meatType == 2):
                finalPrice = quantity * 5.9
            else:
                finalPrice = quantity * 6.9
        else:
            if (meatType == 1):
                finalPrice = quantity * 5.8
            elif (meatType == 2):
                finalPrice = quantity * 6.8
            else:
                finalPrice = quantity * 7.8

        return finalPrice


main = Main()
main.Run()
