class Main:
    @classmethod
    def run(self):
        characters = self.input_characters()
        self.print_consonants(characters)

    @staticmethod
    def input_characters() -> list:
        characters_list = []
        for i in range(1, 11):
            character = Input.character('Insert the {} character: '.format(i))
            characters_list.append(character)
        return characters_list

    @staticmethod
    def print_consonants(characters: list) -> None:
        consonants = []
        vocals = ['a', 'e', 'i', 'o', 'u']
        for character in characters:
            if character not in vocals:
                consonants.append(character)

        print('The inserted consonants are: ')
        print(consonants)


class Input:
    @staticmethod
    def character(message: str) -> str:
        user_input = ''
        number_exception = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        while len(user_input) != 1 or user_input in number_exception:
            try:
                user_input = str(input(message)).strip().lower()
            except Exception:
                user_input = ''
            if len(user_input) != 1 or user_input in number_exception:
                print('Input must a single letter.')
        return user_input


main = Main()
main.run()
