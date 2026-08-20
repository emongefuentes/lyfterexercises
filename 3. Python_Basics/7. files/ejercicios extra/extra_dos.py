def count_words(text):
    with open(text, 'r', encoding='utf-8') as file:
        content = file.read()
        divide_words = content.split()
        print(f"Este archivo contiene {len(divide_words)} palabras")
        
def main():
    count_words('palabras.txt')   


if __name__ == "__main__":
    main()