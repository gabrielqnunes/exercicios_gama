class Main:
    def Run(self):
        count = self.HandleQuestions()

        self.HandlePersonClassificationMessage(count)

    @staticmethod
    def HandleQuestions():
        count = 0
        answer = ''

        print('Answer the questions with YES / NO:')
        answer = input('Did you call the victim?\n')
        count += 1 if (answer.upper() == 'YES') else False

        answer = input('Have you been in the crime scene?\n')
        count += 1 if (answer.upper() == 'YES') else False

        answer = input('Do you live near the victim?\n')
        count += 1 if (answer.upper() == 'YES') else False

        answer = input('Did you owe to the victim?\n')
        count += 1 if (answer.upper() == 'YES') else False

        answer = input('Did you work with the victim?\n')
        count += 1 if (answer.upper() == 'YES') else False

        return count

    @staticmethod
    def HandlePersonClassificationMessage(count):
        if (count == 2):
            print('You are a suspect.')
        elif (count == 3 or count == 4):
            print('You are a accomplice.')
        elif (count == 5):
            print('You are the murderer.')
        else:
            print('You are innocent')


main = Main()
main.Run()
