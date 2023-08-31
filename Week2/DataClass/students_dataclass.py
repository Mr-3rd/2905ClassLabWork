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
