def found_caracter(text, caracter):
    
    count = 0
    for letter in text:
        if letter == caracter:
            count = count + 1
            
    print(f"We have found the letter '{choice}' {count} times.")    
    

choice = input("Type the character you want to search for: ")
found_caracter("programacion", choice)    