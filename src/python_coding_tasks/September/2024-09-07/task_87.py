class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")


class MyDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")


class TC1:
    def runTC(self):
        ExcelReader.readExcelFile()
        MyDBConnection.readMySQLFile()


tc1 = TC1()
tc1.runTC()
