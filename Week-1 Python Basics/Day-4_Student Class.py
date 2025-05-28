class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"\nName: {self.name}, \nAge: {self.age},\n Grade: {self.grade}\n")

    def is_passing(self):
        return self.grade >= 50

    def update_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.grade = new_grade
        else:
            print("Invalid grade. Please enter a value between 0 and 100.")

    def __enter__(self):
        print(f"Entering context for student: {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exiting context for student: {self.name}")

    def __dir__(self):
        return super().__dir__() + ['name', 'age', 'grade', 'is_passing', 'update_grade', 'display_info']

if __name__ == "__main__":
    students = []
    while True:
        print("\n1. Add Student\n2. Display All Students\n3. Update Student Grade\n4. Check Passing Status\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            try:
                age = int(input("Enter age: "))
                grade = int(input("Enter grade (0-100): "))
                students.append(Student(name, age, grade))
                print("Student added.")
            except ValueError:
                print("Invalid input. Age and grade must be numbers.")
        elif choice == "2":
            if not students:
                print("No students to display.")
            for s in students:
                s.display_info()
        elif choice == "3":
            name = input("Enter student name to update grade: ")
            found = False
            for s in students:
                if s.name == name:
                    try:
                        new_grade = int(input("Enter new grade (0-100): "))
                        s.update_grade(new_grade)
                        print("Grade updated.")
                    except ValueError:
                        print("Invalid input. Grade must be a number.")
                    found = True
                    break
            if not found:
                print("Student not found.")
        elif choice == "4":
            name = input("Enter student name to check passing status: ")
            found = False
            for s in students:
                if s.name == name:
                    print(f"{s.name} is {'passing' if s.is_passing() else 'not passing'}.")
                    found = True
                    break
            if not found:
                print("Student not found.")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")