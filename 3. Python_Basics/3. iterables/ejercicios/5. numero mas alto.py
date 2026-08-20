print("Lista de numeros y uno mayor")
counter = 0
list_of_numbers = []
while counter < 10: 
    number = int(input("ingrese 10 numeros: "))
    list_of_numbers.append(number)
    counter += 1
    
print(list_of_numbers)  

max_number = 0
for num in range(0, len(list_of_numbers)):
    if list_of_numbers[num] > max_number:
        max_number = list_of_numbers[num]
print(f"{list_of_numbers}. El numero mayor es: {max_number} ")  


    
    