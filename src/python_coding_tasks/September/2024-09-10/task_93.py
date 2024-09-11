import os

print(os.name)
print(os.getcwd())
# os.chdir("D:/QA_Courses/Python_automation_course/my-python-project/src/python_coding_tasks/hw_tasks")
# print((os.getcwd()))
# os.mkdir('newdirectory')
# os.mkdir('D:/QA_Courses/Python_automation_course/my-python-project/src/python_coding_tasks/September/2024-09-12')
# print(os.listdir('D:/QA_Courses/Python_automation_course/my-python-project/src/python_coding_tasks/September/2024-09-10'))
# os.chdir('D:/QA_Courses/Python_automation_course/my-python-project/src/python_coding_tasks/hw_tasks')

"""os.listdir('.')
for file in os.listdir():
    print(file)"""

# os.rmdir('newdirectory')
# os.remove('sample.txt')
print("**********************")
# os.chdir('D:/QA_Courses/Python_automation_course/my-python-project/src/python_coding_tasks/September')
# print(os.getcwd())
# os.rmdir('2024-09-12')
full_path = os.path.join("D:/QA_Courses/Python_automation_course/my-python-project/src/python_coding_tasks/September/2024-09-10","file1.txt")
print("full path is: ",full_path)

print(os.path.isfile('sample.txt'))
print(os.path.isdir('2024-09-10'))
print(os.path.exists('sample.txt'))
