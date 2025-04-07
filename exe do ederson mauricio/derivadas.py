from problema02 import Veiculo
class Car(Veiculo):
    def __init__(self,model,brand,fuel,passengers):
        super(). __init__(model,brand)
        self.fuel=fuel
        self.passengers=passengers
    def __str__(self):
        return f'marca:{self.brand}\nmodelo:{self.model}\ncombustivel:{self.fuel}\nQTD_passageiros:{self.passengers}'

car1=Car('uno','fiat','gasolina',5)
print(car1.__str__())
