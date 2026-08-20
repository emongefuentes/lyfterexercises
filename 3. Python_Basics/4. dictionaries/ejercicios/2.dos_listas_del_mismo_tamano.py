list_a = ["first_name", "last_name", "role"]
list_b = ["Edgar", "Monge", "Software Developer"]

dictionary = {}

for index in range(len(list_a)):      #aqui utilizo el index como guia para recorrer a su vez la segunda lista
    dictionary[list_a[index]] = list_b[index]
    
print(dictionary)    