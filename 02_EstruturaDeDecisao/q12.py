class Main:
    def Run(self):
        labourValue = float(input('Insert your labour value: '))
        workedHours = float(input('Insert your worked hours in the last month: '))
        salary = labourValue * workedHours

        self.HandleTaxValues(salary)

    def HandleTaxValues(self, salary):
        IR = self.CalculateIncomeTax(salary)
        INSS = salary * 0.1
        FGTS = salary * 0.11

        print('Gross salary         : AU$ {:.2f}'.format(salary))
        print('(-) Income tax (5%)  : AU$ {:.2f}'.format(IR))
        print('(-) INSS (10%)       : AU$ {:.2f}'.format(INSS))
        print('FGTS (11%)           : AU$ {:.2f}'.format(FGTS))
        print('Discounts total      : AU$ {:.2f}'.format(IR + INSS))
        print('Net salary           : AU$ {:.2f}'.format(salary - INSS - IR))
    
    @staticmethod
    def CalculateIncomeTax(salary):

        if (salary <= 900):
            return 0
        elif (salary > 900 and salary <= 1500):
            return salary * 0.05
        elif (salary > 1500 and salary <= 2500):
            return salary * 0.1
        else:
            return salary * 0.2

main = Main()
main.Run()