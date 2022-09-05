class Main:
    def Run(self):
        score1 = float(input("Insert the student's first score: "))
        score2 = float(input("Insert the student's second score: "))
        score3 = float(input("Insert the student's third score: "))

        finalScore = (score1 + score2 + score3) / 3

        self.HandleResultMessage(finalScore)

    @staticmethod
    def HandleResultMessage(finalScore):
        if (finalScore == 10):
            print('''
            Student's score: {}
            Result         : Pass with honor
            '''.format(finalScore))
        elif (finalScore >= 7 and finalScore < 10):
            print('''
            Student's score: {}
            Result         : Pass
            '''.format(finalScore))
        else:
            print('''
            Student's score: {}
            Result        : Fail
            '''.format(finalScore))


main = Main()
main.Run()
