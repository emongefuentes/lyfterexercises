my_list = [3,6,0,-2,4]
negative_list = []
for num in my_list:
    if num <= 0:
        negative_list.append(num)
        
print(f"Esta es la lista de numeros negativos o 0: {negative_list}")        