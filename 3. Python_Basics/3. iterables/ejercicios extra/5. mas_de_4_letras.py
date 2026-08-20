counter = 0 
my_list = []

while counter < 5:
    word = input("Ingrese una palabra: ")
    my_list.append(word)
    counter += 1
    
new_list = []
for word in range(0, len(my_list)):
    char_quantity = 0
    for char in my_list[word]:
        char_quantity += 1
        
    if char_quantity > 4:
        new_list.append(my_list[word])
            
print(new_list)            