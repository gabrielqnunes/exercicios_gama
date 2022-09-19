from datetime import date


class Main:
    @classmethod
    def run(self):
        initial_salary = self.handle_input_salary(
            "Insert the employee's initial salary: AU$")
        start_year = self.handle_input_date(
            "Insert what year the employee starts working: ")
        current_salary = self.calculate_current_salary(
            initial_salary, start_year)
        print("The emplyee's current salary is AU$ {:.2f}.".format(
            current_salary))

    @staticmethod
    def handle_input_salary(message):
        user_input = 0

        while user_input <= 0:
            try:
                user_input = int(input(message).replace(',', '.'))
            except Exception:
                user_input = 0

            if user_input <= 0:
                print('The input must be a number greater than 0.')

        return user_input

    @staticmethod
    def handle_input_date(message):
        current_year = date.today().year
        year = 0

        while year not in range(1950, current_year + 1):
            try:
                year = int(input(message))
            except Exception:
                year = 0

            if year not in range(1950, current_year + 1):
                print('Year must be a integer between 1950 and {}.'.format(
                    current_year))

        return year

    @staticmethod
    def calculate_current_salary(initial_salary, start_year):
        current_year = date.today().year
        current_salary = initial_salary
        count = 0

        while count < current_year - start_year:
            current_salary = current_salary + \
                current_salary * (.015 * (2 ** count))
            count += 1

        return current_salary


main = Main()
main.run()
