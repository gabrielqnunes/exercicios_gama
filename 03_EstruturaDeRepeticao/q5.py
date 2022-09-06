class Main:
    def Run(self):
        isExecuting = True
        while (isExecuting):
            self.CalculateYears()
            isExecuting = bool(
                input('Do you want to try again?'))

    def CalculateYears(self):
        years = 0
        print('===== A Country =====')
        populationCountryA = self.HandlePopulationInput()
        populationRateCountryA = self.HandlePopulationRaiseRateInput()
        print('===== B Country =====')
        populationCountryB = self.HandlePopulationInput()
        populationRateCountryB = self.HandlePopulationRaiseRateInput()

        while (populationCountryA < populationCountryB):
            years += 1
            populationCountryA *= populationRateCountryA
            populationCountryB *= populationRateCountryB

        print("It'll take {} years to the A contry's population be equal to the B country's population."
              .format(years))

    @staticmethod
    def HandlePopulationInput():
        population = 0
        while (population <= 0):
            population = int(input('Insert the population: '))
            if (population > 0):
                return population
            else:
                print('Population has to be a integer bigger than 0.')

    @staticmethod
    def HandlePopulationRaiseRateInput():
        raiseRate = 0
        while (raiseRate <= 0):
            raiseRate = (float(input('Insert the raise rate: %')) / 100) + 1
            if (raiseRate > 0):
                return raiseRate
            else:
                print('The raise rate must be float bigger than 0.')


main = Main()
main.Run()
