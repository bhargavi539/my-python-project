# One more example on Abstraction

from abc import ABC, abstractmethod


class GearBox(ABC):

    @abstractmethod
    def setGear(self):
        pass


class Engine(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Engine,GearBox):

    def start_engine(self):
        print("Starting the engine")

    def stop_engine(self):
        print("Stopping the engine")

    def setGear(self):
        print("Gear setup is ready to use")

    def drive(self):
        self.start_engine()
        self.setGear()
        self.stop_engine()


audi = Car()
audi.drive()
