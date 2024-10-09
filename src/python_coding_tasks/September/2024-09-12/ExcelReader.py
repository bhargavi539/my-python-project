import pandas as pd


def readCSV():
    df = pd.read_csv("testdata.csv")
    print(df)
    print("Reading the testdata file is done")
