class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"name: {self.first_name}\nsurname: {self.last_name}\nage: {self.age}\ngender: {self.gender}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}\nrecord book: {self.record_book}\n"


class Overflow(ValueError):
    def __str__(self):
        return "Группа вже наповнена"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise Overflow

    def delete_student(self, last_name):
        if self.find_student(last_name) in self.group:
            self.group.remove(self.find_student(last_name))

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f"{student.__str__()}\n"
        return f'Number:{self.number}\n\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
for i in range(11):
    try:
        gr.add_student(Student('Male', 30, 'Steve', 'Jobs', 'AN142'))
    except Overflow as a:
        print(a)
print(len(gr.group))
print(gr)
print("OK")
