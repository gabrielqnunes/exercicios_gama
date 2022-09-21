from os import system
from statistics import mean


class Main:
    @classmethod
    def run(self):
        average_scores = self.set_average_scores()
        approved_scores = self.get_scores_greater_seven(average_scores)
        print('{} students got score grater than or equal seven.'.format(
            len(approved_scores)
        ))

    @staticmethod
    def set_average_scores() -> list:
        average_scores = []
        for i in range(1, 11):
            scores = []
            system('clear')
            print('STUDENT {}'.format(i))
            for l in range(1, 5):
                score = Input.positive_float(
                    'Insert the score for exam {}: '.format(l))
                scores.append(score)
            average_scores.append(mean(scores))
        return average_scores

    @staticmethod
    def get_scores_greater_seven(scores: list) -> list:
        scores_greater_seven = []
        for score in scores:
            if score >= 7:
                scores_greater_seven.append(score)
        return scores_greater_seven


class Input:
    @staticmethod
    def positive_float(message: str) -> float:
        user_input = -1
        while user_input < 0:
            try:
                user_input = float(input(message))
            except Exception:
                user_input = -1
            if user_input < 0:
                print('Input must be a float number greater than 0.')
        return user_input


main = Main()
main.run()
