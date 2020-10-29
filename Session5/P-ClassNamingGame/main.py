students = []
should_continue = True

print()
print()
print("Hello! Welcome to the Class Naming Game.")
print("We have 5 different services we provide!")
print()
print('Press "1" to enter your students into the class.')
print('Press "2" to add students to your class.')
print('Press "3" to count the number of occurences of each student in the class.')
print('Press "4" to sort the class alphabetically')
print('Press "5" to remove duplicates from the class')
print()

while should_continue:
    operation = input("Please enter in the operation you want (1, 2, 3, 4, or 5): ")
    if operation == "1":
        num_students = input("Enter the number of students in the class: ")
        for i in range(1, int(num_students)+1):
            name = input(f"Enter the name of student number {i} in the class: ")
            students.append(name)
        print()
        print(f"Here is the list with all the students in the class: {students}")
    elif operation == "2":
        new_student = input("What is the name of the student you want to add to the class? ")
        index = input("At what index in the list do you want to input this student? ")
        students.insert(int(index), new_student)
        print(f"Here is the list with the newly added index: {students}")
    elif operation == "3":
        for i in range(len(students)):
            print(f"{students.count(students[i])} people are named {students[i]} in the class")
    elif operation == "4":
        students.sort()
        print(f"Here is the sorted list: {students}")
    elif operation == "5":
        students = list(set(students))
        print(f"Here is the list of students without duplicates: {students}")
    else:
        print('Please enter a valid input! Either "1", "2", "3", "4", or "5". Thank you :) ')

    stop = input('If you would like to exit and stop the program, type "stop", otherwise press enter: ')
    if(stop == "stop"):
        should_continue = False
    
    for i in range(3):
        print()

