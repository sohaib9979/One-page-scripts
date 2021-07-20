"""
A complimentary piece of Python code,
meant to be printed on a standard A4 piece of paper
as a gift to our teacher at SoftUni.
"""
from sys import maxsize
 
 
class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{self.first_name} {self.last_name}"
 
 
class Teacher(Human):
    def __init__(self, first_name, last_name, t, e):
        Human.__init__(self, first_name, last_name)
        self.thoughtful= t
        self.educated = e
 
 
class DreamTeacher(Teacher):
    def __init__(self, first_name, last_name, t, e, b, s):
        Teacher.__init__(self, first_name, last_name, t, e)
        self.brilliant = b
        self.supportive = s
 
    def __str__(self):
        return f"Thank you for being the best, {self.first_name}!"
 
 
t, h, e, _ = map(eval, ['maxsize'] * 4)
students = {'knowledge': 0, 'inspiration': 0, 'fun': 0}

our_teacher = DreamTeacher('Ines', 'Ivanova', t=h, e=_, b=e, s=t)

while our_teacher.full_name == 'Ines Ivanova':
 
    for quality, value in students.items():
        value += 1

    try:
        print(our_teacher)
    except:
        print("Just kidding. There's no way to raise exception in this case!")

    next_lesson = eval(input())
    # TODO MORE LESSONS!
