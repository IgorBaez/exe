class Conta:
    def __init__(self,numero_conta:int,titular:str,saldo:float):
        self.numero_conta=numero_conta
        self.titular=titular
        self.saldo=saldo

    def saque(self):
        print(self.saldo)
        valor=float(input("dgt o valor do saque"))
        if self.saldo>=valor:
            self.saldo-=valor
            print(self.saldo)
        else:
            print("valor insuficiente ")
        
    def deposito(self,valor:float):
        print(self.saldo)
        valor=float(input("dgt o valor do deposito"))
        self.saldo+=valor
        print(self.saldo)        









