class Main:
    def Run(self):
        price1 = float(input("Insert the first product's price: "))
        price2 = float(input("Insert the second product's price:"))
        price3 = float(input("Insert the third product's price: "))

        print('The {} product is the cheaper.'
              .format(self.ReturnCheaper(price1, price2, price3)))

    @staticmethod
    def ReturnCheaper(price1, price2, price3):
        if (price1 <= price2 and price1 <= price3):
            return 'first'
        elif (price2 <= price1 and price2 <= price3):
            return 'second'
        else:
            return 'third'


main = Main()
main.Run()
