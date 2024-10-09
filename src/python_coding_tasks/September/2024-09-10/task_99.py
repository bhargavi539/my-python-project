# File Handling

"""file = open("D:/QA_Courses/Python_automation_course/my-python-project/src/python_coding_tasks/September/2024-09-10/Docs_Directory/textforfilehandlingconcepts.txt",'r')
content = file.read()
print(content)"""

import os

absolute_file_path = os.path.join("D:/QA_Courses/Python_automation_course/my-python-project/src/python_coding_tasks"
                                  "/September/2024-09-10/Docs_Directory","textforfilehandlingconcepts.txt")

file = open(absolute_file_path,'r')
content = file.read()
print(content)

