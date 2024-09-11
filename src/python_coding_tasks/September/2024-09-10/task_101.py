# Reading content from the file

with open("Docs_Directory/testdata.txt",'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line,end="****")