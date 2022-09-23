from rich.console import Console

console = Console()


def integer_number_positive(message: str) -> int:
    user_input = -1
    while user_input < 0:
        try:
            user_input = int(console.input(message + ' '))
        except Exception:
            user_input = -1
        if user_input < 0:
            console.print('Input must be an integer number [underline]greater than 0[/underline].',
                          style='bright_red',
                          highlight=False
                          )
            print('\033[A\033[A')
            print('\033[A{:100}\033[A')
        print(50 * ' ', end='\r')

    return user_input


def float_number_positive(message: str) -> float:
    user_input = -1
    while user_input < 0:
        try:
            user_input = float(console.input(message + ' '))
        except Exception:
            user_input = -1
        if user_input < 0:
            console.print('Input must be a float number [underline]greater than 0[/underline].',
                          style='bright_red',
                          highlight=False
                          )
            print('\033[A\033[A')
            print('\033[A{:100}\033[A')
        print(50 * ' ', end='\r')

    return user_input
