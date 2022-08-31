class Main():
    def Run(self):
        fileSize = float(input('Insert the file size in MBs: '))
        internetSpeed = float(input('Insert the internet download speed in Mbps: '))

        print("It'll take {} minute(s) do download the file."
             .format(self.CalculateDonwloadTimeInMin(fileSize, internetSpeed)))


    @staticmethod
    def CalculateDonwloadTimeInMin(fileSize, internetSpeed):
        return  round(fileSize / internetSpeed / 60, 2)

main = Main()
main.Run()