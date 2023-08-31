class Student:
    def __init__(self, name, college_id, GPA):
        self.name = name
        self.college_id = college_id
        self.GPA = GPA

    def __str__(self):
        return f'Student: {self.name}, ID: {self.college_id}, GPA: {self.GPA}'

name = input('please enter the student\'s name: ')
id = input(f'please enter the student id for {name}: ')
gpa = input(f'Please enter the GPA for {name}: ')

alex = Student(name, id, gpa)

print(alex)
