class Main:
    def Run(self):
        score1 = float(input("Insert the first student's score: "))
        score2 = float(input("Insert the second student's score: "))

        average = self.CalculateAverage(score1, score2) 

        print('The student {}.'.format(self.StudentsFinalResult(average)))

    @staticmethod
    def CalculateAverage(score1, score2):
        return (score1 + score2) / 2
    
    @staticmethod
    def StudentsFinalResult(finalResult):
        if (finalResult == 10):
            return 'pass with merit'
        elif (finalResult >= 7):
            return 'pass'
        else:
            return 'fail'

main = Main()
main.Run()