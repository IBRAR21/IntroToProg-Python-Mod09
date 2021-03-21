# ---------------------------------------------------------- #
# Title: Test Harness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# IBRAR, 3.21.2021, Created module for Assignment 09 from Listing 10
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Person as P, Employee as E
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test person object from data module
objP1 = P("Bob", "Smith")
objP2 = P("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test employee object from data module
objE1 = E(1, "Bob", "Smith")
objE2 = E(2, "Sue", "Jones")
lstTable = [objE1, objE2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(E(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())

