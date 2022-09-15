from statistics import mean


class Main:
    def run(self):
        discs_quantity = self.get_discs_quantity()
        discs_values = self.get_discs_values(discs_quantity)
        print("The disc's average value is {}.".format(mean(discs_values)))

    @staticmethod
    def get_discs_quantity():
        disc_quantity = 0
        is_first_iteration = True
        while disc_quantity <= 0:
            if not is_first_iteration:
                print("The disc's number must be bigger than 0.")

            try:
                disc_quantity = int(input('Insert how many discs you have: '))
            except Exception:
                disc_quantity = 0

            is_first_iteration = False
        return disc_quantity

    @staticmethod
    def get_discs_values(discs_quantity):
        discs_values = []
        for count in range(discs_quantity):
            disc_value = 0
            is_first_iteration = True
            while disc_value <= 0:
                if not is_first_iteration:
                    print("The disc's value must be bigger than 0.")

                try:
                    disc_value = int(
                        input("Insert the {} disc's value: ".format(count + 1)))
                except Exception:
                    disc_value = 0

                is_first_iteration = False
            discs_values.append(disc_value)
        return discs_values


main = Main()
main.run()
