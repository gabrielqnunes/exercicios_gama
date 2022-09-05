from math import sqrt


class Main:
    def Run(self):
        a = float(input("Insert a's value: "))
        if (a == 0):
            print("The variable a can't be 0.")
            return 0

        b = float(input("Insert b's value: "))
        c = float(input("Insert c's value: "))

        delta = b ** 2 - 4 * a * c
        if (delta < 0):
            print("Delta has not a real root. Then x can't be calculated.")
            return 0

        root1 = (-b + sqrt(delta)) / 2 * a
        if (delta == 0):
            print(
                "Delta is equal to 0. Then x only can be one value. It's {:.2f}.".format(root1))
            return 0

        root2 = (-b - sqrt(delta)) / 2 * a
        if (delta > 0):
            print("Delta is a real positive number.Then x can be 2 values. They're {:.2f} and {:.2f}".format(
                root1, root2))


main = Main()
main.Run()
