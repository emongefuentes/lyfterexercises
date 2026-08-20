#Lo hice de este modo, con la variable global para el numero.


def show_words_depends_of_the_number(list, number):
    
    new_list = []
    for word in list:
        saved_word = word
        count_letter = 0 
        
        for letter in saved_word:
            count_letter += 1
        
        if count_letter > number:
            new_list.append(saved_word)
         
    return new_list    
           
number = int(input("Enter the minimum number of letters in the word: "))


print(show_words_depends_of_the_number(["cielo", "casa", "sol", "maravilloso", "dia"], number))    