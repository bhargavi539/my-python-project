import pytest
import pandas as pd
import csv

class Test_CRUD:
    def test_read_csv_file_with_pandas(self):
        data_file = pd.read_csv('my-python-project/src/python_coding_tasks/October/2024-10-10/userdata.csv')
        print(data_file)


    def test_read_csv_file_with_cvs(self):
        with open('my-python-project/src/python_coding_tasks/October/2024-10-10/userdata.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])