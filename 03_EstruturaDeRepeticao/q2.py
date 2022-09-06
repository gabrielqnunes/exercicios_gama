class Main:
    def Run(self):
        username = ''
        password = ''
        isFirstIteration = True

        while (username == password):
            if (not isFirstIteration):
                print('Username cannot be equal to password.')

            username = input('Username: ')
            password = input('Password: ')

            isFirstIteration = False


main = Main()
main.Run()
