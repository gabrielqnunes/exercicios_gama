class Main:
    def Run(self):
        votersQuantity = int(input('Insert how many voters will vote: '))

        election = self.HandleVotesInput(votersQuantity)
        winner = self.GetWinner(election)
        self.HandleResultMessage(winner)

    @staticmethod
    def HandleVotesInput(votersQuantity):
        election = {
            "candidates": [
                {"number": 1, "name": "Fulanus Primeirus", "votes": 0},
                {"number": 2, "name": "Ciclanus Segundus", "votes": 0},
                {"number": 3, "name": "Triclanus Terceirus", "votes": 0}
            ]
        }
        for voter in range(1, votersQuantity + 1):
            print('=================================')
            print('========== DESCRIPTION ==========')
            print('=================================')
            print('||Candidates:                  ||')
            print('||(1) Fulanus Primeirus        ||')
            print('||(2) Ciclanus Segundus        ||')
            print('||(3) Triclanus Terceirus      ||')
            print('=================================')
            print('|| VOTER {}                     ||'.format(voter))
            number = int(input('   VOTE: '))
            election["candidates"][number - 1]["votes"] += 1

        return election

    @staticmethod
    def GetWinner(election):
        biggestScore = 0
        winner = ''
        for candidate in election["candidates"]:
            if (candidate["votes"] > biggestScore):
                winner = candidate["name"]
                biggestScore = candidate["votes"]
        return winner

    @staticmethod
    def HandleResultMessage(winner):
        print('{} win the election.'.format(winner))


main = Main()
main.Run()
