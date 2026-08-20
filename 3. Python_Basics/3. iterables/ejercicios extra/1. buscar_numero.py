my_list = []
counter = 0 
quantity = int(input("Cuantos numeros desea ingresar? "))

while counter < quantity:
    number = int(input(f"{counter+1}. Ingrese el numero: "))
    my_list.append(number)
    counter += 1
    
print(my_list)  

option = int(input("Que numero desea buscar: "))
number_found = 0
for num in my_list:
    if num == option:
         number_found += 1
         
print(f"El numero se encuentra | {number_found} | veces en la lista")         
  