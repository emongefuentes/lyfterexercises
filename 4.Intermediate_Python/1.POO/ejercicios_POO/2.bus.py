class Person():
    def __init__(self):
        print("I'm a Person")

class Bus():
    max_passengers = 10
    
    def __init__(self):
        self.passengers = []
    
    def add_passenger (self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
        else:
            print("There's no more space")    
        
    
    def show_passengers(self):
        for index, person in enumerate(self.passengers):
            print(index+1) 
            
    def remove_passenger(self):
        if self.passengers:
            self.passengers.pop()
        else:
            print("The bus is empty...")             

  
my_bus = Bus()   
  
while True:
    option = int(input("1)enter 2)remove: "))
    if option == 1:
        new_person = Person()
        my_bus.add_passenger(new_person)
        my_bus.show_passengers()
        
    elif option == 2:
        my_bus.remove_passenger()
        my_bus.show_passengers()
    else:
        break
        
        
    
    
    