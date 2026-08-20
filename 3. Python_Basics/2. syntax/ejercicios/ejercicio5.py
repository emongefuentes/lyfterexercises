

grade_counter = 1
current_grade = 0
approved_count = 0
failed_count = 0
approved_average = 0
failed_average = 0
total_grades = 0

current_grades = int(input("Ingrese el total de notas a registrar: "))

while grade_counter <= current_grades:
    grade_counter = grade_counter + 1
    current_grade = int(input("Ingrese nota actual: "))
    if current_grade < 70:
        failed_count = failed_count + 1
        failed_average = failed_average + current_grade
    else:
        approved_count = approved_count + 1
        approved_average = approved_average + current_grade
    
    total_grades = total_grades + (current_grade / current_grades)


if failed_average > 0 :   #entiendo que el cambio seria en esta linea
    failed_average = failed_average / failed_count
else:
    print("Promedio de notas desaprobadas: No hay notas desaprobadas ")

if approved_average > 0: #entiendo que el cambio seria en esta linea
    approved_average = approved_average / approved_count 
else:
    print("No hay notas aprobadas ")  #entiendo que el cambio seria en esta linea 
    
print(f"El estudiante tiene esta cantidad de notas aprobadas: {approved_count}")
print(f"Este es el promedio de notas aprobadas: {approved_average} ")

print(f"El estudiante tiene esta cantidad de notas desaprobadas: {failed_count} ")
print(f"Este es el promedio de notas desaprobadas: {failed_average}")


print(f"Este es el promedio total de notas {total_grades}")
        