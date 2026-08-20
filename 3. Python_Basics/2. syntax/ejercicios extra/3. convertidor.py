print("Convertidor de unidades de temperatura")

celsius_temperature = int(input("Ingrese la temperatura en celsius: "))
fahrenheit = (celsius_temperature * 9/5) + 32
kelvin = celsius_temperature + 273.15

print(f"Fahrenheit: {fahrenheit}")
print(f"kelvin: {kelvin}")