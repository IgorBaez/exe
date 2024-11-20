class ConversorMoeda:
    def __init__(self,moeda):
        self.moeda=moeda
    def converter(self):
        dolar=5.77
        valor=self.moeda*dolar
        print("o valor em dolares",self.moeda,"em reais e",valor)
x=ConversorMoeda(290)
x.converter()