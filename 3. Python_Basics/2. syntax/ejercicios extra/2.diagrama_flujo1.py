import random

print("Numero secreto")

secret_number = random.randint(1, 10)
# print(secret_number)
guess_number = int(input("Adivine el numero secreto: "))

while guess_number != secret_number:
    guess_number = int(input("Adivine el numero secreto: "))

print(f"Correcto el numero es el {secret_number}")