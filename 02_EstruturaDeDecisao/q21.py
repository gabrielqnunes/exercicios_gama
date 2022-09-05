class Main:
    def Run(self):
        value = int(input('How much cash do you want to withdraw? '))

        if (value < 10 or value > 600):
            print('The value must be over 10 and below 600.')
            return

        hundredBankNotes = value // 100
        remainingValue = value % 100
        fifthBankNotes = remainingValue // 50
        remainingValue = remainingValue % 50
        tenBankNotes = remainingValue // 10
        remainingValue = remainingValue % 10
        fiveBankNotes = remainingValue // 5
        remainingValue = remainingValue % 5
        oneBankNotes = remainingValue

        print('''
        {} of hundred bank notes,
        {} of fifth bank notes,
        {} of ten bank notes,
        {} of five bank notes,
        {} of one bank notes
        '''.format(hundredBankNotes, fifthBankNotes, tenBankNotes, fiveBankNotes, oneBankNotes))


main = Main()
main.Run()
