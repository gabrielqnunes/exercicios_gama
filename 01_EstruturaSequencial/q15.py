class Main:
    def Run(self):
        salaryPerHour = float(input('Insert your salary per hour: '))
        workedHours = float(input('Insert your worked hours: '))
        salaryTotal = self.CalculateSalaryTotal(salaryPerHour, workedHours)

        print('+ Salary total: US$ {}'.format(salaryTotal))
        print('- IR (11%): US$ {}'.format(self.CalculateIR(salaryTotal)))
        print('- INSS (8%): US$ {}'.format(self.CalculateINSS(salaryTotal)))
        print('- Syndicate (5%): US$ {}'.format(self.CalculateSyndicateFee(salaryTotal)))
        print('= Received salary: US$ {}'.format(self.CalculateReceivedSalary(salaryTotal)))

    @staticmethod
    def CalculateSalaryTotal(salaryPerHour, workedHours):
        return salaryPerHour * workedHours

    @staticmethod
    def CalculateINSS(salaryTotal):
        return 0.08 * salaryTotal
    
    @staticmethod
    def CalculateSyndicateFee(salaryTotal):
        return 0.05 * salaryTotal
    
    @staticmethod
    def CalculateIR(salaryTotal):
        return 0.11 * salaryTotal

    @staticmethod
    def CalculateReceivedSalary(salaryTotal):
        return 0.76 * salaryTotal

main = Main()
main.Run()