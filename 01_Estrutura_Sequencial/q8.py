salaryPerHour = float(input('How much do you gain per hour? '))
workedHours = int(input('How much hours did you work this month? '))

def CalculateSalary(salaryPerHour, workedHours):
    return salaryPerHour * workedHours

totalSalary = CalculateSalary(salaryPerHour, workedHours)

print('Your salary is US${}'.format(totalSalary))
