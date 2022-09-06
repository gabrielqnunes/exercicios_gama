class Main:
    def Run(self):
        term = int(input('Insert the Fibonacci term you desire: '))

        fibonacciSequence = self.CalculateFibonacci(term)

        print('The Fibonacci sequence for the term {} is:'.format(term))
        print(fibonacciSequence)

    @staticmethod
    def CalculateFibonacci(term):
        fibonacciSequence = [1, 1]

        for position in range(2, term):
            beforeLastTerm = fibonacciSequence[position - 2]
            lastTerm = fibonacciSequence[position - 1]
            fibonacciSequence.append(beforeLastTerm + lastTerm)

        return fibonacciSequence


main = Main()
main.Run()
