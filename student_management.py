students = []

def addStudent():
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    data = {
        "id": id,
        "name": name,
        "age": age
    }

    students.append(data)
    print("Student added!\n")


def showStudents():
    if len(students) == 0:
        print("No students found\n")
    else:
        for i in students:
            print("ID:", i["id"], "Name:", i["name"], "Age:", i["age"])
        print()


def searchStudent():
    sid = input("Enter ID: ")

    found = False
    for i in students:
        if i["id"] == sid:
            print("Student found:", i)
            found = True

    if not found:
        print("Not found\n")


def deleteStudent():
    sid = input("Enter ID to delete: ")

    for i in students:
        if i["id"] == sid:
            students.remove(i)
            print("Deleted\n")
            return

    print("Student not found\n")


def updateStudent():
    sid = input("Enter ID to update: ")

    for i in students:
        if i["id"] == sid:
            newName = input("New name: ")
            newAge = input("New age: ")

            i["name"] = newName
            i["age"] = newAge

            print("Updated\n")
            return

    print("Not found\n")


while True:
    print("1.Add")
    print("2.Show")
    print("3.Search")
    print("4.Delete")
    print("5.Update")
    print("6.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        addStudent()
    elif ch == "2":
        showStudents()
    elif ch == "3":
        searchStudent()
    elif ch == "4":
        deleteStudent()
    elif ch == "5":
        updateStudent()
    elif ch == "6":
        break
    else:
        print("Wrong choice\n")
