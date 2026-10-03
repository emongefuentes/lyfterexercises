import csv

# def fill_student_info(new_list):
class Student():
    def __init__(self,name, section, score_1, score_2, score_3, score_4):
        self.name = name
        self.section = section
        self.score_1 = score_1
        self.score_2 = score_2
        self.score_3 = score_3
        self.score_4 = score_4
        
        
    print("module actions")   
    
    def create_student(new_list):
        while True:
            
            name = input("Enter the student name: ")
            section = input("Enter the section: ") 
            score_1 = int(input("Enter the spanish grade: "))
            score_2 = int(input("Enter the english grade: "))
            score_3 = int(input("Enter the social studies grade: "))
            score_4 = int(input("Enter the science grade: "))
            
            new_student = Student(name,section, score_1, score_2, score_3, score_4)
            new_list.append(new_student)
            
            while True:
                try:        
                    option = int(input("would you like to add a new student? 1/Yes 2/No "))
                    if option == 1:
                        break
                    elif option == 2:
                        return new_list
                    else: 
                        print("choose only 1 or 2")
                except ValueError:
                    print("Only numbers")
                    
    def calculate_average(self):   
        total = self.score_1 + self.score_2 + self.score_3 + self.score_4
        average = total / 4
        self.average = average #aqui agrega el average al student..
        
                    
                    
def show_student_info(student_list):
    for student in student_list: 
        print(student.name)
        print(student.section )
        print(student.score_1 )
        print(student.score_2 )
        print(student.score_3 )
        print(student.score_4 )
        
def get_average(student):
    return student.average        


def top_3 (student_list):
    for student in student_list:
        student.calculate_average() 
    
    ordered_students =sorted(student_list, key=get_average, reverse=True)[:3]
    
    for student in ordered_students:
        print(f" {student.name}: {student.average}")      
        
        
def show_average(new_list):
    for student in new_list: 
        total = student.score_1 + student.score_2 + student.score_3 + student.score_4
        average = total / 4
        print(f"The {student.name}'s average is: {average}")
        
        

        
                
        
        
        
        

    
        
                    
