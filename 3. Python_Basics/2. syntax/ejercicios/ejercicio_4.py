# Cree un programa que le pida 
# tres números al usuario 
# y muestre el mayor.


number_1 = int(input("Ingrese el primero numero: "))
number_2 = int(input("Ingrese el segundo numero: "))
number_3 = int(input("Ingrese el tercero numero: "))
max_number = 0

if number_1 > number_2:
    max_number = number_1
else:
    max_number = number_2            
if max_number < number_3:
    max_number = number_3 
    
print(f"El numero mayor de los 3 es: {max_number}")    