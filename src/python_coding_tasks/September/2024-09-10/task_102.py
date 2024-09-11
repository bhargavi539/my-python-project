import csv
with open("Docs_Directory/exceldata.csv",'r') as csvfile:
    reader = csv.reader(csvfile)
    print(type(reader))
    for col in reader:
        print(col[0],col[1], sep='|')