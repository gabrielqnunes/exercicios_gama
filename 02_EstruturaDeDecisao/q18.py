from datetime import datetime


class Main:
    def Run(self):
        try:
            dateFormat = '%d/%m/%Y'
            dateString = input('Insert a date (dd/mm/yyyy): ')
            date = datetime.strptime(dateString, dateFormat)

            print('{} is a valid date.'.format(date.strftime(dateFormat)))
        except:
            print("It's not a valid date.")


main = Main()
main.Run()
