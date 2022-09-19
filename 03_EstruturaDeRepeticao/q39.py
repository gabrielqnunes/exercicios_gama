from os import system


class Main:
    @classmethod
    def run(self):
        students = self.handle_students_input()
        smaller_student = self.get_smaller_student(students)
        taller_student = self.get_taller_student(students)

        system('clear')

        print('The smaller student is {} with {}m.'.format(
            smaller_student["number"], smaller_student["height"]))

        print('The taller student is {} with {}m.'.format(
            taller_student["number"], taller_student["height"]))

    @classmethod
    def handle_students_input(self):
        students = []

        for count in range(10):
            system('clear')
            student_number = self.handle_input_int(
                "Insert the student's number: ")
            student_height = self.handle_input_positive_float(
                "Insert the student's heigth: ")
            student = {"number": student_number, "height": student_height}
            students.append(student)

        return students

    @staticmethod
    def get_taller_student(students):
        taller_student = {"height": 0}
        for student in students:
            if student["height"] > taller_student["height"]:
                taller_student = student
        return taller_student

    @staticmethod
    def get_smaller_student(students):
        smaller_student = {"height": 1000}
        for student in students:
            if student["height"] < smaller_student["height"]:
                smaller_student = student
        return smaller_student

    @staticmethod
    def handle_input_int(message):
        user_input = None
        while user_input == None:
            try:
                user_input = int(input(message))
            except Exception:
                user_input = None

            if user_input == None:
                print('Insert an integer.')
        return user_input

    @staticmethod
    def handle_input_positive_float(message):
        user_input = 0
        while user_input <= 0:
            try:
                user_input = float(input(message))
            except Exception:
                user_input = 0

            if user_input <= 0:
                print('Input must be a float grater than 0.')
        return user_input


main = Main()
main.run()
