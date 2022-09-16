class Main:
    @classmethod
    def run(self):
        self.handle_cash_register()

    @classmethod
    def handle_cash_register(self):
        print('==============================')
        print('||       SHOPPING CART      ||')
        print('==============================')

        purchase_total = self.handle_input_products_price()

        print('==============================')
        print('||{:^26}||'.format('TOTAL: R$ {}'.format(purchase_total)))
        print('==============================')

        [total_paid, change] = self.handle_input_payment(purchase_total)

        print('==============================')
        print('||{:^26}||'.format('TOTAL PAID: R$ {}'.format(total_paid)))
        print('||{:^26}||'.format('CHANGE: R$ {}'.format(change)))
        print('==============================')

    @staticmethod
    def handle_input_products_price():
        product_number = 1
        product_price = -1
        purchase_total = 0
        is_first_iteration = True

        while product_price != 0:
            if not is_first_iteration:
                print("Product price must be greater than 0.")

            try:
                product_price = float(
                    input('Product {}: R$ '.format(product_number)))
            except Exception:
                product_price = -1

            if product_price > 0:
                product_number += 1
                purchase_total += product_price
                is_first_iteration = True
            else:
                is_first_iteration = False

        return purchase_total

    @staticmethod
    def handle_input_payment(purchase_total):

        is_first_iteration = True
        total_paid = 0
        change = 0

        while total_paid <= 0:
            if not is_first_iteration:
                print("The value paid for the client must be grater than 0.")

            try:
                total_paid = float(
                    input('Insert how much the customer paid: '))
            except Exception:
                total_paid = 0

            is_first_iteration = False

        change = total_paid - purchase_total

        return [total_paid, change]


main = Main()
main.run()
