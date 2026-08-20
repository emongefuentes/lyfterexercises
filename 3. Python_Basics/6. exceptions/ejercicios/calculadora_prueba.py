def enter_first_number():   
    while True:
        try:
            first_number = int(input("Enter a number: "))
            return first_number
        except ValueError as e:
            print(f"warning, you must use a number {e}")
    
    
def choose_arithmetic_option():
    while True:
        try:
            arithmetic_option = int(input("""
                            
        1. Sum
        2. Rest
        3. Multiplication
        4. Division
        5. Errase result
                            
                        Choose an option: __"""))
    
            if arithmetic_option < 1 or arithmetic_option > 5:
                print("WARNING! Enter a number between 1 - 5: ")
                choose_arithmetic_option()
        except ValueError as e:
            print(f"Error [ValueError]: {e}")  
            choose_arithmetic_option() 
        return arithmetic_option
        
        
def menu(entered_number, option ):   
    counter = entered_number 
   
    while True:
        match option:
            case 1: 
                counter = sum_numbers(counter, enter_other_number())
                menu(counter, choose_arithmetic_option()) 
                # intentar corregir la recursividad con un ciclo...
            case 2:
                counter = rest_numbers(counter, enter_other_number())
                menu(counter, choose_arithmetic_option())
            case 3:
                counter = multiplication_numbers(counter, enter_other_number())
                menu(counter, choose_arithmetic_option())
            case 4:
                counter = division_numbers(counter, enter_other_number())
                menu(counter, choose_arithmetic_option())
            case 5:
                counter = 0
                print(f"The result has been errased: {counter}")
                entered_number = enter_first_number() 
                menu(entered_number, choose_arithmetic_option())
                
                   
def enter_other_number():
    while True:
        try:
            other_number = int(input("Enter other number: "))
            return other_number
        except ValueError as e:
            print(f"Warning!, you must enter a number: {e}")


def sum_numbers(current_number, second_number):
    result = current_number + second_number
    print(f"current number: {result}")
    return result


def rest_numbers(current_number, second_number):
    result = current_number - second_number
    print(f"current number: {result}")
    return result


def multiplication_numbers(current_number, second_number):
    result = current_number * second_number
    print(f"current number: {result}")
    return result


def division_numbers(current_number, second_number):
    try:
        result = current_number / second_number
        print(f"current number: {result}")
        return result
    except ZeroDivisionError as e:
        print(f"We cannot divide by 0.  Detected error: {e}")
        

def main():
    entered_number = enter_first_number() 
    menu(entered_number, choose_arithmetic_option())
    

if __name__ == '__main__':
    main()
