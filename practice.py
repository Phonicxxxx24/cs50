class car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, make):
        if not make :
            raise ValueError("invalid input")
        self._make = make

    def description(self):
        return f"Make: {self.make}, Model: {self.model}"
    
    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}"
    

class ElectricCar(car):
    def __init__(self, make, model, battery): # battery called automatically
        super().__init__(make, model) # calss previous data
        self.battery = battery

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model} and battery: {self.battery} kWh"

        
    
c = ElectricCar("mercedes", "Gwagon", "50")

print(c)