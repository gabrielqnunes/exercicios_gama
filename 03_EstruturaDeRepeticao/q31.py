class Main:
    @classmethod
    def run(self):
        self.handle_cash_register()

    @staticmethod
    def handle_cash_register():
        count = 0
        user_input = -1
        print('==============================')
        print('||       SHOPPING CART      ||')
        print('==============================')
        while user_input != 0:
            user_input = float(input('Product {}: R$ \r'.format(count)))
            count += 1


main = Main()
main.run()
