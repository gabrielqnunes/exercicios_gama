n = 3.1415
radius = float(input('Insert the circle radius: '))

def CalculateCircleArea(radius):
    return n * radius**2

area = CalculateCircleArea(radius)

print('The circle area is {}'.format(area))