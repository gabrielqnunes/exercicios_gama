class Main:
    def run(self):
        self.build_price_table()

    @staticmethod
    def build_price_table():
        print('==============================')
        print('||        PRICE TABLE       ||')
        print('==============================')
        for count in range(1, 51):
            print('  {} - R$ {:.2f}'.format(count, count * 1.99))
        print('==============================')


main = Main()
main.run()
