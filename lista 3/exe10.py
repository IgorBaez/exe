class temperatura:
    def __init__(self,temp):
        self.temp=temp
    def exibir(self):
        far=(self.temp*(9/5)+32)
        print(far)
x=temperatura(10)
x.exibir()