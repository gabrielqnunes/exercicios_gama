from statistics import mean


class Main:
    def run(self):

        classes_quantity = self.get_classes_quantity()
        students_quantities = self.get_students_quantities(classes_quantity)
        print("The student's average per class is {}.".format(
            mean(students_quantities)))

    @staticmethod
    def get_classes_quantity():
        classes_quatity = 0
        is_first_iteration = True
        while classes_quatity <= 0:
            if not is_first_iteration:
                print('Please, insert a integer bigger than 0.')
            try:
                classes_quatity = int(input('Insert the classes quantity: '))
            except Exception:
                classes_quatity = 0
            is_first_iteration = False
        return classes_quatity

    @staticmethod
    def get_students_quantities(classes_quantity):
        students_quantities = []
        for count in range(classes_quantity):
            is_first_iteration = True
            class_quantity = 0
            while class_quantity <= 0 or class_quantity > 40:
                if not is_first_iteration:
                    print("The student's quantity must be between 1 and 40.")
                try:
                    class_quantity = int(
                        input("Insert the {} class student's number: ".format(count + 1)))
                except Exception:
                    class_quantity = 0
                is_first_iteration = False
            students_quantities.append(class_quantity)
        return students_quantities


main = Main()
main.run()
