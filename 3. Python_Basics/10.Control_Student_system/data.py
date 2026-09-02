import csv


def export_cvs_data(new_list):
    with open("students_csv.csv", 'w', encoding='utf-8', newline='') as file:
        headers = new_list[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(new_list)
        
        
def import_csv_data():
    try:
        with open('students_csv.csv', "r", newline='')as file:
            read_file = csv.DictReader(file)
            
            for item in read_file:
                print(item)
            
            
    except FileNotFoundError as e:
        print(f"Error: {e}")            
       