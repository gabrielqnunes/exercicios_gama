class Main:
    def Run(self):
        score = -1
        isFirstIteration = True

        while (score < 0 or score > 10):
            if (not isFirstIteration):
                print('The score {} is invalid.'.format(score))
            score = float(input("Insert the student's score: "))
            isFirstIteration = False

        print('The score {} is valid.'.format(score))


main = Main()
main.Run()
