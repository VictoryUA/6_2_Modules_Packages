from convertor import temperature, distance

# Convert Celsius to Fahrenheit
celsius_temp = 20
fahrenheit_temp = temperature.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")

# Convert Fahrenheit to Celsius 
fahrenheit_temp = 68
celsius_temp = temperature.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is equal to {celsius_temp}°C")