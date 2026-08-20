products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

total_per_category = {}

for product in products:
    #print(product["category"])
    category = product['category']
    price = product['price']
    
    if category not in total_per_category:
        total_per_category[category] = 0
    
    total_per_category[category] = total_per_category[category] + price    
        
print(total_per_category)        
    