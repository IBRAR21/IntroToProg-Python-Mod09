# ------------------------------------------------------------------------ #
# Title: Main
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# IBRAR,3.21.2021,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules

if __name__ == "__main__":
    from DataClasses import Employee as E
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
try:
    file_name = "EmployeeData.txt"
    list_of_employees = []
    input = None
    # Load data from file into a list of employee objects when script starts
    lstFileData = Fp.read_data_from_file(file_name)
    for line in lstFileData:
        list_of_employees.append(E(line[0], line[1], line[2].strip()))
    # Show user a menu of options
    while (True):
        Eio.print_menu_items()
        # Get user's menu option choice
        input = Eio.input_menu_options()
        # Show user current data in the list of employee objects
        if input == "1":
            Eio.print_current_list_items(list_of_employees)
        # Let user add data to the list of employee objects
        elif input == "2":
            new_data = Eio.input_employee_data()
            list_of_employees.append(new_data)
            print("New employee data successfully added!")
        # let user save current data to file
        elif input == "3":
            print(Fp.save_data_to_file(file_name,list_of_employees))
        # Let user exit program
        elif input == "4":
            break
except Exception as e:
    print(e, e.__doc__, type(e), sep="\n")
# Main Body of Script  ---------------------------------------------------- #
