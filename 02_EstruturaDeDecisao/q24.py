class Main:
    def Run(self):
        number1 = float(input('Insert the first number: '))
        number2 = float(input('Insert the second number: '))
        operationSymbol = input('Insert the operation symbol (+, -, *, /): ')

        operationResult = self.HandleOperation(
            number1, number2, operationSymbol)

        self.HandleResultPropertiesMessage(operationResult)

    @staticmethod
    def HandleOperation(number1, number2, operationSymbol):
        if (operationSymbol == '+'):
            return number1 + number2
        elif (operationSymbol == '-'):
            return number1 - number2
        elif (operationSymbol == '*'):
            return number1 * number2
        elif (operationSymbol == '/'):
            return number1 / number2
        else:
            return 'Invalid parameters'

    @staticmethod
    def HandleResultPropertiesMessage(number):
        print('The number {} is:'.format(number))
        if (number % 2 == 0):
            print('- Even')
        else:
            print('- Odd')

        if (number > 0):
            print('- Positive')
        else:
            print('- Negative')

        if (float(number) == int(number)):
            print('- Integer')
        else:
            print('- Float')


main = Main()
main.Run()
