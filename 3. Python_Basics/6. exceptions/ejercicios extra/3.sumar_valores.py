def sum_values(values):
    sum_result = 0
    for element in range(len(values)):
        
        try:
            float_number = float(values[element])
            sum_result = float_number + sum_result
            print(f"Element: '{float_number}' has been added") #lista la correction
        except ValueError:
            print(f"Element:'{values[element]}' cannot be converted") 
    print(f"Total amount: {sum_result}")               

my_list = ['10', 'manzana', '5.5', '3', 'n/a']
sum_values(my_list)    
 
    