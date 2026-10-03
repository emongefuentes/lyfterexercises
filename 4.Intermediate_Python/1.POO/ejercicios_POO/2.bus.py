class Person():
    def __init__(self):
        print("I'm a Person")

class Bus():
    max_passengers = 10
    
    def add_passenger (self, passenger):
        my_list.append(passenger)
        
    
    def show_passengers(self, list_of_passengers):
        for index, person in enumerate(list_of_passengers):
            print(index) 
            
    def remove_passenger(self, list_of_passengers):
        list_of_passengers.pop()           



my_list = []         
while True:
    option = int(input("1)enter 2)remove: "))
    if option == 1:
        new_person = Person()
        my_bus = Bus()
        my_bus.add_passenger(new_person)
        my_bus.show_passengers(my_list)
        
    elif option == 2:
        my_bus.remove_passenger(my_list)
        my_bus.show_passengers(my_list)
    else:
        break
        
        
    
    
    