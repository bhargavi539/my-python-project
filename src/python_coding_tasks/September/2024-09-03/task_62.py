class Car:

    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name ",self.name)
        print("Starting a car with the make ",self.make)
        print("Starting a car with the model ",self.model)


lamborgini = Car("Lamorigini","V2","2024")
lamborgini.start_engine()

volvo = Car("Volvo","XC40","2024")
volvo.start_engine()