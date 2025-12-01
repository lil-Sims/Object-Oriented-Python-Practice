import re

class Student:
    def __init__(self, name, email, grades=None):
        self.name = name
        self.email = email
        self.grades = grades if grades else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")
        print("-" * 30)

    def grades_tuple(self):
        return tuple(self.grades)

student1 = Student("Alice", "alice@example.com", [85, 90])
student2 = Student("Bob", "bob@example.com", [70, 75])
student3 = Student("Charlie", "charlie@example.com", [95, 88])

for s in [student1, student2, student3]:
    s.add_grade(100)
    s.add_grade(82)

# Display info
student1.display_info()
student2.display_info()
student3.display_info()

student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

def get_student_by_email(email):
    return student_dict.get(email, None)

lookup = get_student_by_email("bob@example.com")
if lookup:
    lookup.display_info()

all_grades = set()
for s in student_dict.values():
    all_grades.update(s.grades)
print("Unique Grades Across All Students:", all_grades)
print("-" * 30)

grades_tuple = student1.grades_tuple()
print("Grades Tuple for Alice:", grades_tuple)

try:
    grades_tuple[0] = 99
except TypeError as e:
    print("Tuples are immutable:", e)
print("-" * 30)

for s in [student1, student2, student3]:
    s.grades.pop() 
    print(f"{s.name}'s first grade: {s.grades[0]}")
    print(f"{s.name}'s last grade: {s.grades[-1]}")
    print(f"{s.name} has {len(s.grades)} grades")
    print("-" * 30)

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

for s in [student1, student2, student3]:
    if re.match(email_pattern, s.email):
        print(f"{s.email} is valid")
    else:
        print(f"{s.email} is invalid")

count_above_90 = sum(1 for s in [student1, student2, student3] for g in s.grades if g > 90)
print("Number of grades above 90 across all students:", count_above_90)
