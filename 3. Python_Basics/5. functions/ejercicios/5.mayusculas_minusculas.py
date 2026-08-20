word = "I love Nación Sushi"


def upper_lower_counting(text):
    lower_letter = 0 
    upper_letter = 0

    for letter in text:
        if letter.islower():
            lower_letter = lower_letter + 1 
        if letter.isupper(): 
            upper_letter = upper_letter + 1
            
    print(f"There’s {upper_letter} upper cases and {lower_letter} lower cases")    
    
    
upper_lower_counting(word)        