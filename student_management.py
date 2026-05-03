students = []

def add_student():
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    
    student = {"id": id, "name": name, "age": age}
    students.append(student)
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("No records found!\n")
        return
    
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}")
    print()

def search_student():
    id = input("Enter ID to search: ")
    
    for s in students:
        if s["id"] == id:
            print(f"Found: {s}")
            return
    print("❌ Student not found!\n")

def delete_student():
    id = input("Enter ID to delete: ")
    
    for s in students:
        if s["id"] == id:
            students.remove(s)
            print("🗑️ Deleted successfully!\n")
            return
    print("❌ Student not found!\n")

def update_student():
    id = input("Enter ID to update: ")
    
    for s in students:
        if s["id"] == id:
            s["name"] = input("Enter new name: ")
            s["age"] = input("Enter new age: ")
            print("✏️ Updated successfully!\n")
            return
    print("❌ Student not found!\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        update_student()
    elif choice == "6":
        break
    else:
        print("Invalid choice!\n")