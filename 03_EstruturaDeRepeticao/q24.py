from statistics import fmean


class Main:
    def Run(self):
        scoresQuantity = int(
            input('Insert how many scores you want to input: '))

        scores = self.HandleScoresInput(scoresQuantity)
        scoresMean = fmean(scores)

        print("The scores's mean is {}.".format(scoresMean))

    @staticmethod
    def HandleScoresInput(scoresQuantity):
        scores = []

        for count in range(1, scoresQuantity + 1):
            score = float(input('Insert the score {}: '.format(count)))
            scores.append(score)

        return scores


main = Main()
main.Run()
