from statistics import mean


class Main:
    @classmethod
    def run(self):
        scores = self.handle_scores_input()
        self.handle_print_scores(scores)

    @staticmethod
    def handle_scores_input() -> list:
        scores = []
        for i in range(1, 5):
            score = Input.handle_positive_float(f'Insert the {i} score: ')
            scores.append(score)
        return scores

    @staticmethod
    def handle_print_scores(scores: list) -> None:
        print(60 * '=')
        print('||{:^56}||'.format('RESULT'))
        print(60 * '=')
        print('||{:^40}|{:^15}||'.format('EXAMS', 'SCORE'))
        print(60 * '=')
        for score in scores:
            print('||{:^40}|{:^15}||'.format(
                'EXAM {}'.format(scores.index(score) + 1),
                score
            ))
        print(60 * '=')
        print('||{:^40}|{:^15}||'.format('AVERAGE', mean(scores)))
        print(60 * '=')


class Input:
    @staticmethod
    def handle_positive_float(message: str) -> float:
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
