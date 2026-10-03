import csv
import actions


def export_cvs_data(new_list):
    if not new_list:
        print("The list is empty")
    else: 
        students_dict = []
        
        for student in new_list:
            student.calculate_average()
            student_dict = {"name": student.name, 
                            "section": student.section,
                            "spanish": student.score_1,
                            "english": student.score_2,
                            "social_studies": student.score_3,
                            "science": student.score_4,
                            "average": student.average
                            
                            }
            
            students_dict.append(student_dict)
            
                   
        with open("students_csv.csv", 'w', encoding='utf-8', newline='') as file:
            headers = students_dict[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(students_dict)
            
        
def import_csv_data(list_to_import):
    try:
        with open('students_csv.csv', "r", newline='')as file:
            read_file = csv.DictReader(file)
            for item in read_file:
                new_student = actions.Student(item["name"],
                                              item["section"],
                                              int(item["spanish"]),
                                              int(item["english"]),
                                              int(item["social_studies"]),
                                              int(item["science"])
                                              )
                
                list_to_import.append(new_student)
        print("a CSV file has been imported.")                                  
                       
    except FileNotFoundError as e:
        print(f"_____The file doesn't exist___{e}")
    return list_to_import
    