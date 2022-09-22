
def integer_number_positive(message: str) -> int:
    user_input = -1
    while user_input < 0:
        try:
            user_input = int(input(message))
        except Exception:
            user_input = -1
        if user_input < 0:
            print('Input must be an integer number greater than 0.')
    return user_input


def float_number_positive(message: str) -> float:
    user_input = -1
    while user_input < 0:
        try:
            user_input = float(input(message))
        except Exception:
            user_input = -1
        if user_input < 0:
            print('Input must be a float number grater than 0.')
    return user_input
