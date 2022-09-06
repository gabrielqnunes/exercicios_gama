class Main:
    def Run(self):
        self.HandleInputName()
        self.HandleInputAge()
        self.HandleInputSalary()
        self.HandleInputGender()
        self.HandleInputMaritalStatus()

    @staticmethod
    def HandleInputName():
        name = ''
        while (len(name) <= 3):
            name = input('Insert your name: ')
            if (len(name) > 3):
                return
            else:
                print('Name must have at least 4 characteres.')

    @staticmethod
    def HandleInputAge():
        age = None
        while (age not in range(0, 150)):
            age = int(input('Insert your age: '))
            if (age in range(0, 150)):
                return
            else:
                print('Age must be a integer beetwen 0 and 150.')

    @staticmethod
    def HandleInputSalary():

        salary = -1
        while (salary <= 0):
            salary = float(input('Isert your salary: '))
            if (salary > 0):
                return
            else:
                print('Salary must be bigger than 0.')

    @staticmethod
    def HandleInputGender():
        gender = ''
        while (gender.upper() not in ('F', 'M', 'A')):
            gender = input('Insert your gender: ').upper()
            if (gender in ('F', 'M', 'A')):
                return
            else:
                print('Gende must be:')
                print('F for female, M for male and A for agender.')

    @staticmethod
    def HandleInputMaritalStatus():
        maritalStatus = ''
        while (maritalStatus.upper() not in ('S', 'M', 'W', 'D')):
            maritalStatus = input('Insert your marital status: ').upper()
            if (maritalStatus.upper() in ('S', 'M', 'W', 'D')):
                return
            else:
                print('Marital status must be:')
                print('S for single, M for married, W for widowed and D for divorced.')


main = Main()
main.Run()
