print("""
      
      Valor mas pequeño
      -----------------
     """)

my_list = [23, 74, 9, 51, 88, 2, 65, 12, 1, 37]
smallest = my_list[0]

for num in my_list:
    if num < smallest:
        
        smallest = num
    else:
        continue
print(my_list)   
print(f"El numero menor de la lista es: {smallest}")        
        

       
    
    
    
