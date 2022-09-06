class Main:
    def Run(self):
        years = 0
        populationCountryA = 80000
        populationCountryB = 200000

        while (populationCountryA < populationCountryB):
            years += 1
            populationCountryA *= 1.03
            populationCountryB *= 1.015

        print("It'll take {} years to the A contry's population be equal to the B country's population."
              .format(years))


main = Main()
main.Run()
