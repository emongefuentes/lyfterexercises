import actions, data

def menu():
    new_list = []
    student_list = []
    while True:
        print("""
              1) Enter info student
              2) View student information
              3) View the top 3
              4) View all average grades
              5) Export CSV
              6) Import CSV
              """)
        try:
            option = int(input("Choose the option desired from 1 to 6: "))
            if option > 0 and option < 8:
                if option == 1:
                    student_list = actions.fill_student_info(new_list )
                elif option == 2:
                    actions.show_student_info(student_list)   
                elif option == 3:
                    actions.top_3(student_list) 
                elif option == 4:
                    actions.show_average(student_list)
                elif option == 5:
                    data.export_cvs_data(student_list)    
                elif option == 6:
                    imported_list = data.import_csv_data(new_list) 
                    student_list = imported_list
                    continue
                else:
                    print("The options available are 1 to 6")
        except ValueError as e:
            print(f"The option must be a number.  Error: {e}")    
            continue
        

      