class Main:
    def Run(self):
        score1 = float(input('Insert the first score: '))
        score2 = float(input('Insert the second score: '))
        scoreAverage = (score1 + score2) / 2
        scoreClassification = self.HandleScoreClassification(scoreAverage)

        print('Final score         : {}'.format(scoreAverage))
        print('Score classification: {}'
              .format(scoreClassification))
        print('Student result      : {}'.format(
            self.HandlePassOrFail(scoreClassification)))

    @staticmethod
    def HandleScoreClassification(scoreAverage):
        if (scoreAverage >= 9 and scoreAverage <= 10):
            return 'A'
        elif (scoreAverage >= 7.5 and scoreAverage < 9):
            return 'B'
        elif (scoreAverage >= 6 and scoreAverage < 7.5):
            return 'C'
        elif (scoreAverage >= 4 and scoreAverage < 6):
            return 'D'
        elif (scoreAverage >= 0 and scoreAverage < 4):
            return 'E'
        else:
            return 'Invalid score'

    @staticmethod
    def HandlePassOrFail(scoreClassification):
        if (scoreClassification in ['A', 'B', 'C']):
            return 'Pass'
        elif (scoreClassification in ['D', 'E']):
            return 'Fail'


main = Main()
main.Run()
