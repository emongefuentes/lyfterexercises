print("Precio productor")

product_price = int(input("Ingrese el precio del producto: "))
if product_price >= 100:
    discount = product_price * 10 / 100
    product_price = product_price - discount
    print(f"El precio del producto es {product_price}")
else:
    discount = product_price * 2 / 100
    product_price = product_price - discount
    print(f"El precio del producto es {product_price}")   