class Circle:
    radius = int(input("Enter the radius: "))
    pi = 3.14
    
    def get_area(self):
         area_calculus = Circle.pi * (Circle.radius*Circle.radius)
         return area_calculus
         
new_circle = Circle()

result = new_circle.get_area()
print(f"the area is: {result}")
