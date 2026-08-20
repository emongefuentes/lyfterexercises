def reading_lowercase_letters (text):
    with open(text, 'r', encoding='utf-8') as file:
        content = file.read()
        upper_content = content.upper()
        print(upper_content)
        return upper_content
        
        
def write_text(text):
    with open("upper_text.txt", 'w', encoding='utf-8') as file:
        file.write(text)
        

def main():
    one_content = reading_lowercase_letters('minusculas.txt')
    write_text(one_content)



if __name__ == "__main__":
    main()
    
        