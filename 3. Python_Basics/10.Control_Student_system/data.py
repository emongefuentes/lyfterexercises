import csv


def export_cvs_data(new_list):
    if not new_list:
        print("The list is empty")
    else:    
        with open("students_csv.csv", 'w', encoding='utf-8', newline='') as file:
            headers = new_list[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(new_list)
            
        
def import_csv_data(list_to_import):
    with open('students_csv.csv', "r", newline='')as file:
        read_file = csv.DictReader(file)
        for item in read_file:
            list_to_import.append(item)
                
    for student in list_to_import: 
        student["spanish"] = int(student["spanish"])           
        student["english"] = int(student["english"]) 
        student["social_studies"] = int(student["social_studies"]) 
        student["science"] = int(student["science"]) 
        student["average"] = float(student["average"]) 
    print("A CSV file has been imported. ")    

    return list_to_import
    