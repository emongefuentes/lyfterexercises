print("Tiempo en segundos")

time_in_seconds = int(input("Ingrese el tiempo en segundos: "))
if time_in_seconds < 600:
    calculate_time = 600 - time_in_seconds
    print(f"Falta {calculate_time} segundos para los 10 minutos")
elif time_in_seconds > 600:
    print("Mayor")
else:
    print("igual")
    
    
            