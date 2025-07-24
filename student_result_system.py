def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    subjects = ["Maths", "Science", "Python"]
    marks = {}

    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks[subject] = mark

    total = sum(marks.values())
    average = total / len(subjects)

    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 40:
        grade = 'D'
    else:
        grade = 'F'

    # Save to file (append mode)
    with open("students.txt", "a") as file:
        line = f"{name},{roll},{marks['Maths']},{marks['Science']},{marks['Python']},{total},{average:.2f},{grade}\n"
        file.write(line)

    print("✅ Student added and saved to file successfully!\n")


def show_all_students():
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print("No student records found.\n")
                return

            print("\n===== Student Records =====")
            for line in lines:
                name, roll, maths, science, python, total, avg, grade = line.strip().split(",")
                print("----------------------------")
                print(f"Name     : {name}")
                print(f"Roll No. : {roll}")
                print("Marks:-")
                print(f"Maths  : {maths}")
                print(f"Science: {science}")
                print(f"Python : {python}")
                print(f"Total    : {total}")
                print(f"Average  : {avg}")
                print(f"Grade    : {grade}")
            print("----------------------------")

    except FileNotFoundError:
        print("No data file found. Please add a student first.\n")


def main():
    while True:
        print("\n==== Student Result Management ====")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

