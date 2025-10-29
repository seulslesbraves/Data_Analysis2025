#MAGIC METHOD:
"""The special methods in PYTHON that starts and ends with double underscores"""

class Student:
    def __init__(self, name,marks,roll):
        self.name = name
        self.marks = marks
        self.roll = roll
    
    def __str__(self):
        return f"{self.name} has scored {self.marks} marks."

    # @staticmethod
    # def __len__(item):
    #     count = 0
    #     for i in item:
    #         count += 1
    #     return count

    def __len__(self):
        print(f"The length of {self.name} is {len(self.name)}")
        return len(self.name)

s1 = Student("Inez",99, 6)
print(Student)
print(s1)
print(s1.marks)

count = len(s1)
print(count)