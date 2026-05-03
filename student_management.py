students = []

def add_student():
    print("\n--- Add New Student ---")
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    student = {"id": sid, "name": name, "age": age}
    students.append(student)

    print("Student added successfully!\n")


def show_students():
    print("\n--- Student List ---")
    if not students:
        print("No students found.\n")
        return

    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']}")
    print()


def search_student():
    print("\n--- Search Student ---")
    sid = input("Enter ID to search: ")

    for s in students:
        if s["id"] == sid:
            print(f"Found: {s}\n")
            return

    print("Student not found.\n")


def delete_student():
    print("\n--- Delete Student ---")
    sid = input("Enter ID to delete: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def update_student():
    print("\n--- Update Student ---")
    sid = input("Enter ID to update: ")

    for s in students:
        if s["id"] == sid:
            s["name"] = input("Enter new name: ")
            s["age"] = input("Enter new age: ")
            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


# Main Loop
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        update_student()
    elif choice == "6":
        print("Exiting... Bye")
        break
    else:
        print("Invalid choice, try again.\n")
