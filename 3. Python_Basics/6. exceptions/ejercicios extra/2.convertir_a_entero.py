def convert_to_integer(items):
        for element in range(len(items)):
            try:
                int(items[element])
                print(f"the element has been converted: {items[element]}")
            except ValueError:
                print(f"The element: '{items[element]}' cannot be converted")
            
                    
my_list = ['4', 'hello', '10', '5.2']        
convert_to_integer(my_list)        