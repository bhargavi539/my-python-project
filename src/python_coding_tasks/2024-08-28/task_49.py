# Dictionary -> contains key-> values
# Keys are always unique in Dictionaries
student_info = {"name": "Oliver",
                "age": 15,
                "Address": "NYC"
                }
print(student_info)
print(student_info["name"])

student_info["age"] = int(input("Enter student's age: "))
print(student_info)