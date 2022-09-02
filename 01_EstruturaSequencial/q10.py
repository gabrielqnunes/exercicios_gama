celsiusTemperature = float(input('What is the temperature in Celsius? '))

def CelsiusToFahrenheit(celsiusTemperature):
    return celsiusTemperature * 1.8 + 32

fahrenheitTemperature = CelsiusToFahrenheit(celsiusTemperature)

print('The temperature in Fahrenheit is {}'.format(fahrenheitTemperature))