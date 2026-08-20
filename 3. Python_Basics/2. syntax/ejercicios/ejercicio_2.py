#Cree un programa que le pida al usuario su nombre, 
# apellido, y edad, y muestre si es un bebé, niño, 
# preadolescente, adolescente, adulto joven, adulto,
# o adulto mayor.

# Bebé:              0 a 2 años
# Niño:              3 a 10 años
# Preadolescente:    11 a 12 años
# Adolescente:       13 a 17 años
# Adulto joven:      18 a 29 años
# Adulto:            30 a 59 años
# Adulto mayor:      60 años o más

print("Ejercicio 2, Edad del usuario")

name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if age <= 2:
    print(f"{name} {last_name} es un bebé de {age} de edad")

elif age >= 3 and age < 10:
    print(f"{name} {last_name} es un niño de {age} de edad")  

elif age >=10 and age < 12:
    print(f"{name} {last_name} es un preadolescente de {age} de edad")  

elif age >=12 and age < 17:
    print(f"{name} {last_name} es un adolescente de {age} de edad")  

elif age >=17 and age < 29:
    print(f"{name} {last_name} es un adulto joven de {age} de edad")  

elif age >=29 and age <= 59:
    print(f"{name} {last_name} es un adulto de {age} de edad")  

else:
    print(f"{name} {last_name} es un adulto mayor de {age} de edad")             
            