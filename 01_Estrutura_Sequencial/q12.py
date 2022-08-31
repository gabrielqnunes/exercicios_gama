height = float(input('Insert your height: '))

def CalculateIdealWeight(height):
    return (72.7 * height) - 58

idealWeight = CalculateIdealWeight(height)

print('Your ideal weight is {}'.format(idealWeight))