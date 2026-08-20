def read_text (text):
    with open(text, 'r', encoding='utf-8') as file:
        content = file.read()
        clean_text = content.replace("\n", " ")
        print("__Lectura de texto__")
        return clean_text 
    
    
def new_archive(new_text):
    with open("new_archive.txt", 'w', encoding='utf-8') as file:
        file.write(new_text)
        print("__creacion de new_archive__")

if __name__ == "__main__":         
    new_info = read_text('texto_line_per_line.txt')
    new_archive(new_info)


