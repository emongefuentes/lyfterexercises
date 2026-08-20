def read_txt (songs):
    with open(songs, 'r', encoding='utf-8') as file:
        unordered_list = [line.strip() for line in file]
        return unordered_list
    
    
def order_list (items):        
    items.sort()
    return items


def create_new_txt (items):    
    with open('order_songs.txt', 'w', encoding='utf-8') as order_list:
        for line in items:
            order_list.write("\n" + line)
            

def read_new_order_list(text):
    with open(text, 'r', encoding='utf-8') as file:
        readsongs = file.read()
        print(readsongs)  
        
       

def main():
    new_list = order_list(read_txt('canciones.txt'))
    create_new_txt(new_list)
    read_new_order_list('order_songs.txt')
        

if __name__ == "__main__":
    main()