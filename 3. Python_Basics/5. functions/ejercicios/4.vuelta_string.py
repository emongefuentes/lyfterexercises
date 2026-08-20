string_list = "Hola mundo"


def reverse_text(text):
    value = ""
    for letter in range(len(text)-1,-1,-1):
        value = value + text[letter]   #esto lo redescubri por algo que me pasó en uno de los siguientes ejercicios, ya que se volteaba el orden de las palabras.
    print(value)
        
          
reverse_text(string_list)        