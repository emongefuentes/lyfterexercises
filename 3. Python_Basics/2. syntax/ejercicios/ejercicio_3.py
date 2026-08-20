# Cree un programa con un numero 
# secreto del 1 al 10. El programa no 
# debe cerrarse hasta que el usuario 
# adivine el numero.
import random

print ("Numero Random")

secret_number = random.randint(1, 10)
user_guess = int(input("Ingrese el numero secreto: "))
#print(numero_random)


while user_guess != secret_number:
    user_guess = int(input("Ingrese el numero secreto: "))

print(f"Excelente el numero es: {user_guess}") 

   