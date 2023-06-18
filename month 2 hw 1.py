class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'My name is {self.fullname}, I\'m {self.age} years old. '
              f'I\'m {"" if self.is_married == "yes" else "not"} married')

class Student(Person):
    def __init__(self, fullname, age, is_married, marks: dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_mark(self):
        a = 0
        for i in self.marks.values():
            a += i
        print(f'Average mark is {round(a/len(self.marks), 2)}')


class Teacher(Person):
    salary = 15000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def add_bonus(self):
        if self.experience > 3:
            self.experience -= 3
            while self.experience != 0:
                self.salary += (self.salary*5/100)
                self.experience -= 1
            print(f'My salary is {round(self.salary, 2)}$')


s = Teacher('Tilek', 23, 'yes', 8)
s.introduce_myself()
s.add_bonus()

def create_students():
    s1 = Student('Azamat', 22, 'yes', {'math':4, 'history': 4, 'kygyz':3})
    s2 = Student('Bakyt', 25, 'yes', {'math': 5, 'history': 4, 'kyrgyz': 4})
    s3 = Student('Ulan', 21, 'no', {'math': 5, 'history': 3, 'kyrgyz': 2})
    s_list = []
    s_list.append(s1); s_list.append(s2); s_list.append(s3)
    return s_list

for i in create_students():
    i.introduce_myself()
    i.average_mark()