def display_student_info(student):
    """Displays student information in a formatted way"""
    print("\nStudent Information:")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Favorite Subject: {student['subject']}")
    
    # Check if student is over or under 18
    if student['age'] >= 18:
        print("Status: Adult student")
    else:
        print("Status: Minor student")

# Main program
students = []  # List to store multiple students

for i in range(3):  # Loop for 3 students
    print(f"\nEnter details for student {i+1}:")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    subject = input("Enter your favorite subject: ")
    
    # Store data in a dictionary
    student_data = {
        'name': name,
        'age': age,
        'subject': subject
    }
    
    students.append(student_data)  # Add student to the list

# Display information for all students
for student in students:
    display_student_info(student)