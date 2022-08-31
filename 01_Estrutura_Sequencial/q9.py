fahrenheitTemperature = float(input('Whats the temperature in Fahrenheit? '))

def ConvertFahrenheitToCelsius(fahrenheitTemperature):
    return 5 * ((fahrenheitTemperature - 32) / 9)

celsiusTemperature = ConvertFahrenheitToCelsius(fahrenheitTemperature)

print('The temperature in Celsius is {}'.format(celsiusTemperature))