my_list = [10, 20, 30, 40, 50]
total_sum = 0
average = 0
values_over_average = []

for index in range(0, len(my_list)):
    total_sum = total_sum + my_list[index]
    average = total_sum / len(my_list)
    
for index in my_list:
    if index > average:
        values_over_average.append(index)
 
print(f"Promedio: {average}") 
print(f"Nueva lista: {values_over_average}")