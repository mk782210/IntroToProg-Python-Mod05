# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Manish Khatiwada, 11/09/2026, Created Script
# ------------------------------------------------------------------------------------------ #

# Import the json
import json
from json import JSONDecodeError

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user
student_last_name: str = ''  # Holds the last name of a student entered by the user
course_name: str = ''  # Holds the name of a course entered by the user
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file
menu_choice: str = '' # Hold the choice made by the user


# When the program starts, read the file data into a list of dictionaries(table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print(f"File {FILE_NAME} not found")
    print('-----Technical Error------')
    print(e, e.__doc__, type(e), sep='\n')
    print("creating non-existent file")
    file = open(FILE_NAME, "w")
    json.dump(students, file)
    file.close()
except JSONDecodeError as e:
    print(f"File {FILE_NAME} is not valid JSON")
    print('-----Technical Error------')
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!")
    print('-----Technical Error------')
    print(e, e.__doc__, type(e), sep='\n')
finally:
    # Check if a file object exists and is still open
    if file is not None and file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
        except ValueError as e:
            print(e)
            print('-----Technical Error------')
            print(e.__doc__)
            continue
        except Exception as e:
            print("There was a non-specific error!")
            print(e, e.__doc__, type(e), sep='\n')
            continue
        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
        except ValueError as e:
            print(e)
            print('-----Technical Error------')
            print(e.__doc__)
            continue
        except Exception as e:
            print("There was a non-specific error!")
            print(e, e.__doc__, type(e), sep='\n')
            continue

        course_name = input("Please enter the name of the course: ")
        student_data = {'FirstName': student_first_name,
                        'LastName': student_last_name,
                        'CourseName': course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-"*50)

        # Show a string of comma-separated values for each row
        for student in students:
            print(f"{student['FirstName']},{student['LastName']},{student['CourseName']}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        except TypeError as e:
            print("Please check that the data is a valid JSON format")
            print('-----Technical Error------')
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print('-----Technical Error------')
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
