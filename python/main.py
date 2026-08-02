# ===========================================
# 1. VARIABLES
# ===========================================

school_name = "Python Academy"
passing_grade = 70


# ===========================================
# 2. DATA TYPES
# ===========================================

# String
student_name = "Alice"

# Integer
student_age = 20

# Float
student_grade = 85.5

# Boolean
is_student = True

# List
subjects = ["Math", "Science", "English"]

# Tuple
school_location = ("London", "UK")

# Dictionary
student = {
    "name": student_name,
    "age": student_age,
    "grade": student_grade
}


# ===========================================
# 3. FUNCTIONS
# ===========================================

def print_student(student):
    print("\n----- Student Information -----")
    print("Name :", student["name"])
    print("Age  :", student["age"])
    print("Grade:", student["grade"])


def passed(grade):
    return grade >= passing_grade


def print_subjects(subjects):
    print("\nSubjects:")

    for subject in subjects:
        print("-", subject)


# ===========================================
# 4. CLASS
# ===========================================

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"\nHello! My name is {self.name}.")
        print(f"I am {self.age} years old.")

    def show_grade(self):
        print(f"My grade is {self.grade}")

    def has_passed(self):

        if self.grade >= passing_grade:
            print("Status: Passed")
        else:
            print("Status: Failed")


# ===========================================
# 5. MAIN PROGRAM
# ===========================================

print("Welcome to", school_name)

print_student(student)

print_subjects(subjects)


# if / else
print("\nChecking grade...")

if passed(student_grade):
    print("Congratulations! You passed.")
else:
    print("Sorry, you failed.")


# for loop
print("\nNumbers:")

for number in range(1, 6):
    print(number)


# while loop
print("\nCountdown:")

count = 3

while count > 0:
    print(count)
    count -= 1

print("Go!")


# Create an object
student1 = Student("Alice", 20, 85.5)

student1.introduce()
student1.show_grade()
student1.has_passed()