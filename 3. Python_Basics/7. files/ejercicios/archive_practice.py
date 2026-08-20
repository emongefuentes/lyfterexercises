def create_file ():
    with open("movies.txt", 'w', encoding='utf-8') as file:
        file.write(
            " The Matrix\n Once upon a time in hollywood\n The independence Day\n StarWars\n The lord of the Rings "
            )
        

def read_file(text):
    with open(text, 'r', encoding='utf-8')as file:
        content = file.read()
        print(content)
        
        
def read_line(text):
    with open(text, 'r', encoding='utf-8') as file:
        list = file.readlines()
        print(list[1])
            
        
        
archive_uno = create_file()
read_file("movies.txt")
read_line("movies.txt") 
