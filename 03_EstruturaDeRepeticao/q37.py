from os import system


class Main:
    @classmethod
    def run(self):
        customers = self.register_customers()
        taller_customer = self.get_taller(customers)
        smaller_customer = self.get_smaller(customers)
        fatter_customer = self.get_fatter(customers)
        skinnier_customer = self.get_skinnier(customers)

        system('clear')
        print('The taller customer is {} with {}m.'.format(
            taller_customer["code"], taller_customer["height"]))
        print('The smallest customer is {} with {}m.'.format(
            smaller_customer["code"], smaller_customer["height"]))
        print('The fatter customer is {} with {}kg.'.format(
            fatter_customer["code"], fatter_customer["weight"]))
        print('The skinnier customer is {} with {}kg.'.format(
            skinnier_customer["code"], skinnier_customer["weight"]))

    @classmethod
    def register_customers(self):
        customers = []
        customer_code = -1

        while customer_code != 0:
            customer_height = 0
            customer_weight = 0

            system('clear')
            print(40 * '=')
            print('||{:^36}||'.format('REGISTER CUSTOMER'))
            print(40 * '=')

            while customer_code < 0:
                customer_code = self.handle_int_input(
                    'Insert your customer code: ')
                if customer_code < 0:
                    print('Customer code must be an integer greater than 0.')

            if customer_code != 0:
                while customer_height <= 0:
                    customer_height = self.handle_float_input(
                        'Insert your height: ')
                    if customer_height <= 0:
                        print('Height must be a float number grater than 0.')

                while customer_weight <= 0:
                    customer_weight = self.handle_float_input(
                        'Insert your weight: ')
                    if customer_weight <= 0:
                        print('Weight must be a float number greater than 0.')

                customer = {
                    "code": customer_code,
                    "height": customer_height,
                    "weight": customer_weight
                }
                customers.append(customer)

                customer_code = -1

        return customers

    @staticmethod
    def handle_int_input(input_text):
        user_input = None
        while user_input == None:
            try:
                user_input = int(input(input_text))
            except Exception:
                user_input = None

            if user_input == None:
                print('The input must be an integer.')

        return user_input

    @staticmethod
    def handle_float_input(input_text):
        user_input = None
        while user_input == None:
            try:
                user_input = float(input(input_text))
            except Exception:
                user_input = None

            if user_input == None:
                print('The input must be a float number.')
        return user_input

    @staticmethod
    def get_taller(customers):
        taller = {"height": 0}

        for customer in customers:
            if customer["height"] > taller["height"]:
                taller = customer

        return taller

    @staticmethod
    def get_smaller(customers):
        smaller = {"height": 1000}

        for customer in customers:
            if customer["height"] < smaller["height"]:
                smaller = customer

        return smaller

    @staticmethod
    def get_fatter(customers):
        fatter = {"weight": 0}

        for customer in customers:
            if customer["weight"] > fatter["weight"]:
                fatter = customer

        return fatter

    @staticmethod
    def get_skinnier(customers):
        skinner = {"weight": 1000}

        for customer in customers:
            if customer["weight"] < skinner["weight"]:
                skinner = customer

        return skinner


main = Main()
main.run()
