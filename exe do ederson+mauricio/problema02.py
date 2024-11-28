class Veiculo:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def fuel_type(self):
        self.type=input("What type of fuel ? ")
        print(self.type)
    def passenger_capacity(self):
        self.capacity=input("Number of passengers ? ")
        print(self.capacity)

