class Student:
    name = None
    age = None
    student_id = None

    def student_info(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        return f"{self.name},{self.age},{self.student_id}"


student_list = []
name = input("Enter student name ")
age = int(input("Enter student age "))
student_id = int(input("Enter student id "))
stu_obj = Student()
student = stu_obj.student_info(name, age, student_id)
student_list.append(student)

for student in student_list:
    print(student)
