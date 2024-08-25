import csv

class Student:
    def __init__(self, student_id, name, electives):
        self.student_id = student_id
        self.name = name
        self.electives = electives

class Faculty:
    def __init__(self, faculty_id, name, specialization, subjects):
        self.faculty_id = faculty_id
        self.name = name
        self.specialization = specialization
        self.subjects = subjects

class University:
    def __init__(self):
        self.students = []
        self.faculties = []

    def load_students(self):
        with open('student.csv', mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student_id = row['ï»¿Student ID']
                name = row['Name']
                electives = []
                for i in range(5):
                    elective = row[f'Elective {i+1}']
                    if elective:
                        electives.append((elective, row[f'Elective {i+1} Class Number']))
                self.students.append(Student(student_id, name, electives))

    def load_faculties(self):
        with open('faculty.csv',mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                faculty_id = row['ï»¿ID']
                name = row['Name']
                specialization = row['Specialization']
                subjects = []
                for i in range(3):
                    subject = row[f'Subject {i+1}']
                    if subject:
                        subjects.append((subject, row[f'Subject {i+1} Class Number']))
                self.faculties.append(Faculty(faculty_id, name, specialization, subjects))

    def get_faculty_details(self, faculty_id):
        for faculty in self.faculties:
            if faculty.faculty_id == faculty_id:
                return faculty
        return None

    def get_student_details(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def get_class_size(self, faculty_id):
        faculty = self.get_faculty_details(faculty_id)
        if faculty:
            class_sizes = {}
            for subject, class_number in faculty.subjects:
                class_sizes[subject] = 0
                for student in self.students:
                    for elective, elective_class_number in student.electives:
                        if elective == subject and elective_class_number == class_number:
                            class_sizes[subject] += 1
            return class_sizes
        return None

    def get_student_list(self, faculty_id):
        faculty = self.get_faculty_details(faculty_id)
        if faculty:
            student_list = {}
            for subject, class_number in faculty.subjects:
                student_list[subject] = []
                for student in self.students:
                    for elective, elective_class_number in student.electives:
                        if elective == subject and elective_class_number == class_number:
                            student_list[subject].append(student.name)
            return student_list
        return None

    def get_faculty_name(self, subject, class_number):
        for faculty in self.faculties:
            for faculty_subject, faculty_class_number in faculty.subjects:
                if faculty_subject == subject and faculty_class_number == class_number:
                    return faculty.name
        return None

def main():
    university = University()
    university.load_students()
    university.load_faculties()

    while True:
        print("1. Get class size for a faculty")
        print("2. Get student list for a faculty")
        print("3. Get student details")
        print("4. Get faculty details")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            faculty_id = input("Enter faculty ID: ")
            class_sizes = university.get_class_size(faculty_id)
            if class_sizes:
                for subject, size in class_sizes.items():
                    print(f"{subject}: {size}")
            else:
                print("Faculty not found")
        elif choice == "2":
            faculty_id = input("Enter faculty ID: ")
            student_list = university.get_student_list(faculty_id)
            if student_list:
                for subject, students in student_list.items():
                    print(f"{subject}: {', '.join(students)}")
            else:
                print("Faculty not found")
        elif choice == "3":
            student_id = input("Enter student ID: ")
            student = university.get_student_details(student_id)
            if student:
                print(f"Name: {student.name}")
                for elective, class_number in student.electives:
                    faculty_name = university.get_faculty_name(elective, class_number)
                    print(f"{elective} (Taught by {faculty_name})")
            else:
                print("Student not found")
        elif choice == "4":
            faculty_id = input("Enter faculty ID: ")
            faculty = university.get_faculty_details(faculty_id)
            if faculty:
                print(f"Name: {faculty.name}")
                print(f"Specialization: {faculty.specialization}")
                for subject, class_number in faculty.subjects:
                    print(f"{subject} (Class Number: {class_number})")
            else:
                print("Faculty not found")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
