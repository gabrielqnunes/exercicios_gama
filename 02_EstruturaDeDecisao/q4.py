class Main:
    def Run(self):
        letter = input('Insert a letter: ')

        print('The inserted letter is {}.'
            .format(self.VowelOrConsonant(letter)))

    @staticmethod
    def VowelOrConsonant(letter):
        if(letter in 'aeiou'):
            return 'a vowel'
        else:
            return 'a consonant'

main = Main()
main.Run()