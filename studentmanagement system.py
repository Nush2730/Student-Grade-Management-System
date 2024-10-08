#create an empty dictionary
import pandas as pd

student_grades ={ }

def add_student(name,grade):
    student_grades[name]=grade
    print(f"Addded{name} with {grade}")
    
   #update the students grade
def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} with marks are updates")
    else:
        print(f"{name} was not found")
    
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} was deleted")
    else:
        print(f"{name} not found")
      
def display_all_students():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name}:{grade}")
         
        else:
            print("no student found")                             

def main():
    while True:
        print('\n Student grade management system')
        print("1.Add Student")
        print("2.Update student")
        print("3.Delete student")
        print("4.View student")
        print("5.Exit")
        
        choice =int(input("Enter your choice:"))
        if choice == 1:
            name = input("Enter student name :")
            grade = int(input("Enter student grade:"))
            add_student(name,grade)
            
        elif choice == 2:
            name = input("Enter student name :")
            grade = int(input("Enter student grade:"))  
            update_student(name,grade)
            
        elif choice == 3:
            name = input("Enter student name :")
            delete_student(name)
          
        elif choice == 4:
            display_all_students()
         
        elif choice == 5:
            print("exit the program")
            break        
        else:
            print("Invalid choice")
            
        
        
        