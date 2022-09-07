from statistics import mean


class Main:
    def Run(self):
        peopleQuantity = int(input('Insert how many people will be sign up: '))
        ages = self.HandlePeopleInput(peopleQuantity)
        self.HandleResultMessage(mean(ages))

    @staticmethod
    def HandlePeopleInput(peopleQuantity):
        ages = []

        for person in range(1, peopleQuantity + 1):
            age = -1
            while (age < 0):
                age = int(input('Insert the person {} age: '.format(person)))
            ages.append(age)

        return ages

    @staticmethod
    def HandleResultMessage(agesMean):
        if (agesMean >= 0 and agesMean <= 25):
            print('The class is young.')
        elif (agesMean > 25 and agesMean <= 60):
            print('The class is grown up.')
        else:
            print('The class is elderly.')


main = Main()
main.Run()
