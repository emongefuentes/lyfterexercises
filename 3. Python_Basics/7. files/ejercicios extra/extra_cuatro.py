def enter_write_text ():
    text = input("Enter a write text: ")
    return text


def verifying_file():
    try:
        with open('texto_four.txt', 'r', encoding='utf-8') as file:
            print("El texto se agrega al final del archivo sin borrar lo anterior")
            return True
    except FileNotFoundError:
        print("The file not exist")  
        return False   
    

def create_or_adding_file(option, text):
    if option == True:
        adding_text_to_the_file(text)
    else:
        create_file(text)    
        
def create_file(text):
    with open('texto_four.txt', 'w', encoding='utf-8') as file:
        file.write(text)   

        
def adding_text_to_the_file(text):
    with open('texto_four.txt', 'a', encoding='utf-8') as file:
        file.write("\n" + text)
        

def main():
    text = enter_write_text()
    choice = verifying_file()
    create_or_adding_file(choice, text)
    
if __name__ == "__main__":
    main()
        