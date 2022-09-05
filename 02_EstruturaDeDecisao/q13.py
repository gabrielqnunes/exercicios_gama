class Main:
    def Run(self):
        dayNumber = int(input('Insert a number: '))

        print(self.HandleDayOfWeek(dayNumber))

    @staticmethod
    def HandleDayOfWeek(number):
        if (number == 1):
            return 'Domingo'
        elif (number == 2):
            return 'Segunda-feira'
        elif (number == 3):
            return 'Terça-feira'
        elif (number == 4):
            return 'Quarta-feira'
        elif (number == 5):
            return 'Quinta-feira'
        elif (number == 6):
            return 'Sexta-feira'
        elif (number == 7):
            return 'Sábado'
        else:
            return "It's not a valid day."

main = Main()
main.Run()