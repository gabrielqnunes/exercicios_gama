class Main:
    def Run(self):
        side1 = float(input("Insert the triangle's first side: "))
        side2 = float(input("insert the triangle's second side: "))
        side3 = float(input("Insert the triangle's third side: "))

        print(self.CategorizeTriangle(side1, side2, side3))

    @staticmethod
    def CategorizeTriangle(side1, side2, side3):
        if (side1 > side2 + side3) and (side2 > side1 + side3) and (side3 > side1 + side2):
            return "It's not a triangle."
        elif (side1 == side2 and side2 == side3):
            return "It's an equilateral triangle."
        elif (side1 == side2 or side2 == side3 or side1 == side3):
            return "It's an isosceles triangle."
        else:
            return "It's a scalene triangle."


main = Main()
main.Run()
