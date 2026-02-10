class Student:
    college_name = "ABC College"
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name
    @staticmethod
    def is_pass(marks):
        return "Pass" if marks >= 35 else "Fail"
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"College: {Student.college_name}")
s1 = Student("Bharath", 101)
s2 = Student("Rahul", 102)
print("Before Changing College")
s1.display()
s2.display()
Student.change_college("MRIT Engineering College")
print("After Changing College")
s1.display()
s2.display()
print(Student.is_pass(80))
print(Student.is_pass(20))