def enter_name():
    name = input("Enter your name: ")
    if name.isdigit():
        raise ValueError ("The name cannot be a number.")
    return name


def enter_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            return age  
        except ValueError as e:
            print(f"1. Error {e}")   
    
        
def show_info(name, age):
    print(f"Hello {name}, your age is {age}.")   
    

show_info(enter_age(), enter_name())


    
    
