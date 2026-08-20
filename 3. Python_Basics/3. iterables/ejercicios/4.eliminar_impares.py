# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

# for num in my_list:
#     item = num % 2
#     if item != 0:
#         my_list[num] = "x"
        
        
# print(my_list)  

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

# for index, item in enumerate(my_list):
# 	print(f'Record {index}: {item}')     


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

for num in range(len(my_list)-1,-1,-1):
    
    if my_list[num] % 2 != 0:
        my_list.pop(num)
       
print(my_list)        
# Aqui he entendido que el borrar los elementos
# del 0 hacia adelante, o izquierda a derecha, cambia
# el tamano de la lista. Entonces salia el error 
# IndexError: pop index out of range
# IndexError: list index out of range
# por lo tanto he dado vuelta a la lista

