class Main:
    def Run(self):
        fibonacciList = self.CalculateFibonacciOverFiveHundred()

        print(fibonacciList)

    @staticmethod
    def CalculateFibonacciOverFiveHundred():
        fibonacciList = [1, 1]
        term = 2

        while fibonacciList[term - 1] <= 500:
            beforeLastTerm = fibonacciList[term - 2]
            lastTerm = fibonacciList[term - 1]
            fibonacciList.append(beforeLastTerm + lastTerm)
            term += 1

        return fibonacciList


main = Main()
main.Run()
