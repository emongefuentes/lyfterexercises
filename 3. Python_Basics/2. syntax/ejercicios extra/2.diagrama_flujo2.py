print("Suma de numero 30")

number_1 = int(input("Ingrse el primer numero: "))
number_2 = int(input("Ingrse el segundo numero: "))
number_3 = int(input("Ingrse el tercero numero: "))

if number_1 == 30 or number_2 == 30 or number_3 == 30:
    print("correcto")
else:
    total_sum = number_1 + number_2 + number_3
    if total_sum == 30:
        print(f"Correcto {number_1} + {number_2} + {number_3} es igual a {total_sum}")
    else:
        print("Incorrecto, no hay ningun numero 30, y la suma de ellos tampoco es 30")        