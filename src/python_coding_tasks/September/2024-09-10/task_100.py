# File appending
try:
    with open("Docs_Directory/testdata.txt",'a') as file:
        file.write(" Text appended to the file")
except FileNotFoundError as fnfe:
    print(fnfe)
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)
