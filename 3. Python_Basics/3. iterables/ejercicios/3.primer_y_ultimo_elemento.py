print("Intercambio de numeros. ")

my_list = [1,2,3,4,5,6,7,8,9]
change_item = my_list.pop(0)
second_change_item = my_list.pop()
my_list.append(change_item)
my_list.insert(0, second_change_item)

print(my_list)
    


