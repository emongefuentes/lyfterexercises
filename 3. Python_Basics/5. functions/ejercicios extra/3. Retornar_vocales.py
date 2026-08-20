def only_return_vocals(text):
    vocals = "aeiouAEIOUáúóíé"
    count = 0
    for letter in text:
        for vocal in vocals:
            if letter == vocal:
                count += 1
    return count            

print(only_return_vocals("hola mundo, perro, gato, "))    