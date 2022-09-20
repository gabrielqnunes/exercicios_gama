from os import system
from statistics import mean


class Main:
    @classmethod
    def run(self):
        exam_template = self.get_exam_template()
        notes = self.handle_exam_input(exam_template)
        self.handle_result_print(notes)

    @staticmethod
    def get_exam_template() -> list:
        exam_template = ['A', 'B', 'C', 'D', 'E']
        return exam_template

    @staticmethod
    def handle_exam_input(exam_template: list) -> list:
        student = 1
        note = 0
        notes = []
        question_answer = None
        is_running = True
        while is_running:
            system('clear')
            print(40 * '=')
            print('||{:^36}||'.format('CORRECTION'))
            print(40 * '=')
            print('||{:^36}||'.format(
                'STUDENT: {}'.format(student)
            ))
            print(40 * '=')
            for i in range(5):
                question_answer = Input.handle_exam_question(
                    'QUESTION {}: '.format(i + 1)
                ).upper()
                if question_answer == exam_template[i]:
                    note += 1
            notes.append(note)
            note = 0
            student += 1
            continue_to_next = Input.handle_yes_or_no(
                'Do you want to correct another exam? (Y/N) ')
            is_running = continue_to_next
        return notes

    @staticmethod
    def handle_result_print(notes: list) -> None:
        system('clear')
        print(40 * '=')
        print('||{:^36}||'.format('RESULTS'))
        print(40 * '=')
        print('||{:^25}|{:^10}||'.format(
            'GREATEST NOTE ',
            max(notes)
        ))
        print('||{:^25}|{:^10}||'.format(
            'LOWEST NOTE',
            min(notes)
        ))
        print('||{:^25}|{:^10}||'.format(
            'AVERAGE NOTE',
            mean(notes)
        ))
        print(40 * '=')


class Input:
    @staticmethod
    def handle_exam_question(message: str) -> str:
        user_input = None
        while user_input not in ['A', 'B', 'C', 'D', 'E']:
            try:
                user_input = input(message).upper()
            except Exception:
                user_input = None
            if user_input not in ['A', 'B', 'C', 'D', 'E']:
                print('The input must be: A, B, C, D or E.')
        return user_input

    @staticmethod
    def handle_yes_or_no(message: str) -> bool:
        user_input = None
        while user_input not in ['Y', 'N', 'YES', 'NO']:
            try:
                user_input = input(message).upper()
            except Exception:
                user_input = None
            if user_input not in ['Y', 'N', 'YES', 'NO']:
                print('The input must be Y or N.')
        if user_input in ['Y', 'YES']:
            user_input = True
        else:
            user_input = False
        return user_input


main = Main()
main.run()
