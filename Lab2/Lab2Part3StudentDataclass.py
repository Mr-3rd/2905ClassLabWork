"""
Justin Third 2905, Lab 2 Q 2 8/29/2023
create an author class to build a list of published books
"""


'''
I think I'm a fan of the type of solution that works 

'''

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    college_id: int
    GPA: float

    def __str__(self):
        return f'Student: {self.name}, ID: {self.college_id}, GPA: {self.GPA}'


def main():
    alice = Student('Alice', 12, 3.9)
    bob = Student('Bob', 14, 3.7)

    print(alice)
    print(bob)


if __name__ == '__main__':
    main()
