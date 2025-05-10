class Engine:
    def __init__(self, type_of_engine):
        self.type_of_engine = type_of_engine
    
    def start_engine(self):
        return f"The {self.type_of_engine} engine has started."

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition: Engine is a part of Car
    
    def start_car(self):
        print(f"Starting the {self.model} car...")
        print(self.engine.start_engine())  # Accessing Engine's method

# Example usage
engine1 = Engine("V8")
car1 = Car("Mustang", engine1)
car1.start_car()
