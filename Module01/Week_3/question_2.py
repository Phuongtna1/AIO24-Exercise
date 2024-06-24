from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name=name, yob=yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name=name, yob=yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name=name, yob=yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__list_people = []

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        c = 0
        for p in self.__list_people:
            if type(p) is Doctor:
                c += 1
        return c

    def sort_age(self):
        self.__list_people.sort(key=lambda p: p.get_yob(), reverse=True)

    def compute_average(self):
        c = 0
        sum_year = 0
        for p in self.__list_people:
            if type(p) is Teacher:
                c += 1
                sum_year += p.get_yob()
        return sum_year/c


# Examples
# 2(a)
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()
# output
# >> Student - Name: studentA - YoB: 2010 - Grade: 7

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()
# output
# >> Teacher - Name: teacherA - YoB: 1969 - Subject: Math

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()
# output
# >> Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists

# 2(b)
print()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# output
# >> Ward Name: Ward1
# Student - Name: studentA - YoB: 2010 - Grade: 7
# Teacher - Name: teacherA - YoB: 1969 - Subject: Math
# Teacher - Name: teacherB - YoB: 1995 - Subject: History
# Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists
# Doctor - Name: doctorB - YoB: 1975 - Specialist: Cardiologists

# 2(c)
print(f"\nNumber of doctors: {ward1.count_doctor()}")

# output
# >> Number of doctors: 2

# 2(d)
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

# output
# >> After sorting Age of Ward1 people
# Ward Name: Ward1
# Student - Name: studentA - YoB: 2010 - Grade: 7
# Teacher - Name: teacherB - YoB: 1995 - Subject: History
# Doctor - Name: doctorB - YoB: 1975 - Specialist: Cardiologists
# Teacher - Name: teacherA - YoB: 1969 - Subject: Math
# Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists
