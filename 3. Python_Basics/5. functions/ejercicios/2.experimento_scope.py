global_var = 45

def first_function():
    local_var = 70
    
    
def second_function():
    global_var = 66
    return global_var

# print(f'1. This is the local var inside first function: {local_var}')

result = second_function()
print(f"2. La variable global no cambia fuera de la funcion. Este retorno es una variable con el mismo nombre. {result}")

print(f"Imprimiendo global_var: {global_var}")
    

    
        