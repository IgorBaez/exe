class Temperatura:
    def __init__(self,temp):
        self.temp=temp
    def exibir(self):
        far=(self.temp*(9/5)+32)
        print(far)
x=Temperatura(10)
x.exibir()