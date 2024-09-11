# try, except and finally
# file
import os
try:
    current_file_path = os.getcwd() # This method gives the path of current working directory
    print(current_file_path)
    file = open(current_file_path+"/sample.txt",'r')
    print(file.read())
except FileNotFoundError as fnf:
    print("File not found, Check the filepath or create a new file ",fnf)
finally:
    try:
        print(" try block inside finally")
        file.close()
    except NameError as ne:
        print("file doesn't exist",ne)