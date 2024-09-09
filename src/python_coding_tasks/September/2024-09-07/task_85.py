from abc import ABC, abstractmethod


class ExcelReader:

    @abstractmethod
    def readfromExcel(self):
        pass


class Browser(ExcelReader):

    @abstractmethod
    def startBrowser(self):
        pass

    def stopBrowser(self):
        pass


class TestCase1(Browser):

    def startBrowser(self):
        print("Starting Browser")

    def stopBrowser(self):
        print("Stopping Browser")

    def readfromExcel(self):
        print("Read from excel is ready")

    def runTestCase1(self):
        self.startBrowser()
        self.readfromExcel()
        self.stopBrowser()


tc1 = TestCase1()
tc1.runTestCase1()
