class Circle:
    radius = int(input("Enter the radius: "))
    pi = 3.14
    
    def get_area(self):
         area_calculus = Circle.pi * (Circle.radius*Circle.radius)
         print(f"The area is: {area_calculus}")
         
new_circle = Circle()
new_circle.get_area()
