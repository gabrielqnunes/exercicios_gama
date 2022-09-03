class Main:
    def Run(self):
        salary = float(input("Insert the employee's salary: "))

        self.ManageSalaryIncrease(salary)

    @staticmethod
    def ManageSalaryIncrease(salary):

        increasePercentual = 0
        increasedValue = 0
        newSalary = 0

        if (salary <= 280):
            increasePercentual = 20
            newSalary = salary * 1.2
            increasedValue = newSalary - salary
        elif (salary > 280 and salary <= 700):
            increasePercentual = 15
            newSalary = salary * 1.15
            increasedValue = newSalary - salary
        elif (salary > 700 and salary <= 1500):
            increasePercentual = 10
            newSalary = salary * 1.1
            increasedValue = newSalary - salary
        else:
            increasePercentual = 5
            newSalary = salary * 1.05
            increasedValue = newSalary - salary

        print('Current salary: {}'.format(salary))
        print('Increase percentual: {}'.format(increasePercentual))
        print('Increased value: {}'.format(increasedValue))
        print('New salary: {}'.format(newSalary))


main = Main()
main.Run()
