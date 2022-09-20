class Main:
    @classmethod
    def run(self):
        election_table = self.get_election_table()
        self.print_election_table(election_table)
        election_table = self.handle_input_votes(election_table)
        self.print_election_result(election_table)

    @staticmethod
    def handle_input_votes(election_table: list) -> list:
        user_vote = None
        voter = 1
        print('Insert 0 to (EXIT).')
        while user_vote != 0:
            user_vote = Input.handle_int_0_to_6(
                '[VOTER {}] Insert your vote: '.format(voter))
            voter += 1
            for candidate in election_table:
                if user_vote == candidate["id"]:
                    candidate["votes"] += 1
                    break
        return election_table

    @staticmethod
    def print_election_result(election_table: list) -> None:
        total_votes = 0
        null_votes = next(
            candidate["votes"] for candidate in election_table if candidate["candidate"].upper() == 'NULL VOTE')
        blank_votes = next(
            candidate["votes"] for candidate in election_table if candidate["candidate"].upper() == 'BLANK VOTE')

        print(60 * '=')
        print('||{:^56}||'.format('RESULT'))
        print(60 * '=')
        print('||{:^30}|{:^25}||'.format(
            'NAME', 'VOTES'
        ))
        print(60 * '=')
        for candidate in election_table:
            print('||{:^30}|{:^25}||'.format(
                candidate["candidate"], candidate["votes"]
            ))
            total_votes += candidate["votes"]
        print(60 * '=')
        print('||{:^56}||'.format(
            '% NULL VOTES: {:.2f}%'.format(null_votes * 100 / total_votes)
        ))
        print('||{:^56}||'.format(
            '% BLANK VOTES: {:.2f}%'.format(blank_votes * 100 / total_votes)
        ))
        print(60 * '=')

    @staticmethod
    def get_election_table() -> list:
        election_table = [
            {
                "id": 1,
                "candidate": 'Fulanus Ciclanus',
                "votes": 0
            },
            {
                "id": 2,
                "candidate": 'Ciclanus Segundus',
                "votes": 0
            },
            {
                "id": 3,
                "candidate": 'Trilanus Trilungus',
                "votes": 0
            },
            {
                "id": 4,
                "candidate": 'Quadranus Quadrunus',
                "votes": 0
            },
            {
                "id": 5,
                "candidate": 'Null Vote',
                "votes": 0
            },
            {
                "id": 6,
                "candidate": 'Blank Vote',
                "votes": 0
            }
        ]
        return election_table

    @staticmethod
    def print_election_table(election_table: list) -> None:
        print(60 * '=')
        print('||{:^56}||'.format('ELECTION TABLE'))
        print(60 * '=')
        for candidate in election_table:
            print('||{:^15}|{:^40}||'.format(
                '({})'.format(candidate["id"]), candidate["candidate"]
            ))
        print(60 * '=')


class Input:
    @staticmethod
    def handle_int_0_to_6(message: str) -> int:
        user_input = None
        while user_input not in range(7):
            try:
                user_input = int(input(message))
            except Exception:
                user_input = None
            if user_input not in range(7):
                print('Input must be an integer number between 0 and 6.')
        return user_input


main = Main()
main.run()
