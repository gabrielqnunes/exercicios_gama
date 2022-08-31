class Main:
    def Run(self):
        fishWeight = float(input("What's the fish weight? "))
        penalty = self.CalculatePenalty(fishWeight)

        print('The penalty that must to be paid is R$ {}'.format(penalty))

    @staticmethod
    def CalculatePenalty(fishWeight):
        if (fishWeight <= 50):
            return float(0);
        else:
            return float((fishWeight - 50) * 4)

main = Main()
main.Run()