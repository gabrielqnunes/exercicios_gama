class Main:
    @classmethod
    def run(self):
        bread_price = self.get_bread_price()
        self.build_price_table(bread_price)

    @staticmethod
    def get_bread_price():

        bread_price = 0
        is_first_iteration = True
        while bread_price <= 0:
            if not is_first_iteration:
                print("The bread's price must be bigger than 0.")

            try:
                bread_price = float(input("Insert the bread's price: "))
            except Exception:
                bread_price = 0

            is_first_iteration = False
        return bread_price

    @staticmethod
    def build_price_table(bread_price):
        print('=================================')
        print('||         PRICE TABLE         ||')
        print('=================================')
        for count in range(1, 51):
            print('  {} - R$ {:.2f}'.format(count, count * bread_price))
        print('=================================')


main = Main()
main.run()
