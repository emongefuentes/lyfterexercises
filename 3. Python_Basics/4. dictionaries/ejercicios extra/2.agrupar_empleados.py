employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

departments = {}

for employee in employees:
    department = employee['department']
    
    if department not in departments:
        departments[department] = []
        
    departments[department].append(employee)    
    
print(departments)
    
    
       