def accept_list_of_numbers():
    my_list = numbers = [1, 4, 6, 7, 13, 9, 67] 
    return my_list
    
    
def check_if_the_number_is_prime_or_not (my_list):
    prime_numbers_list = []                        #Esta bien haber colocado la creacion de la lista como local ?
    for num in my_list:
        mayor_num = num
        count = 0
        count_of_results = 0 
        while count < mayor_num: 
            count += 1
            result = num % count
            if result == 0:
                count_of_results = count_of_results + 1 

        if count_of_results < 3 and count_of_results > 1:
            prime_numbers_list.append(num) 
    print(prime_numbers_list)  
    return prime_numbers_list       #Mi duda aqui, es que dice retorne, entonces ignoro si debe usar el return para devolver el valor, llamandolo desde alguna otra funcion. o Solo show el cartel con los numeros primos. 
    
    
accept_list_of_numbers()
check_if_the_number_is_prime_or_not(accept_list_of_numbers())              
                