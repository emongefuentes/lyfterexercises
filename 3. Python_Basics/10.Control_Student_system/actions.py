import csv

def fill_student_info(new_list):
    print("module actions")   
    while True:
        student = {}
        student["name"] = input("Enter the student name: ")
        student["section"] = input("Enter the section: ") 
        list_course = ["spanish", "english", "social_studies", "science"]
        for course in list_course:
            while True:
                try:
                    grade = int(input(f"Enter the {course} grade: "))
                except ValueError:
                    print("only numbers from 0-100")
                    continue    
                if grade >= 0 and grade < 101:
                    break
                else:
                    print("The grade must be a number between 0 - 100")
            student[course] = grade
        new_list.append(student)  
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
    
                    
def show_student_info(student_list):   
    for index in range(len(student_list)):
        print(f"\n{index+1}")
        for key, value in student_list[index].items():
            print(f"{key}: {value}")
            
            
def top_3 (new_list):
    for index in range(len(new_list)):
        total_grade = 0
        list_course = ["spanish", "english", "social_studies", "science"]
        for course in list_course:
            for key, value in new_list[index].items():
                if key == course:
                    total_grade = total_grade + value
        average = total_grade / 4    
        new_list[index]["average"] = average

    def order_3(diccionary):
            return diccionary["average"]        
    top_three = sorted(new_list, key=order_3, reverse=True)[:3]  
    for index in range(len(top_three)):
        print(f"{top_three[index]["name"]}: {top_three[index]["average"]}")
        
        
def show_average(new_list):
    for index in range(len(new_list)):
        total_grade = 0
        list_course = ["spanish", "english", "social_studies", "science"]
        for course in list_course:
            for key, value in new_list[index].items():
                if key == course:
                    total_grade = total_grade + value
            average = total_grade / 4    
            new_list[index]["average"] = average
    print("\nStudent | Average")            
    for index in range(len(new_list)):
        print(f"{new_list[index]["name"]}:      {new_list[index]["average"]}")
        
        

        
                
        
        
        
        

    
        
                    
