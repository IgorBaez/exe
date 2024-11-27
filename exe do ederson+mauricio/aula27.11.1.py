from aula27 import *
class Conta_premium(Conta):
    def __str__(self):
        return f"saldo:{self.saldo}"
    
    def __init__(self,numero_conta:int,titular:str,saldo:float,limite_emprestimo:float):
        super().__init__(numero_conta,titular,saldo)
        self.limite_emprestimo=limite_emprestimo

    def emprestimo(self):
        valor=float(input("dgt o valor do emprestimo"))
        if self.limite_emprestimo>=valor:
            self.saldo+=valor
            print(self.saldo)
            self.limite_emprestimo-=valor
            print(self.limite_emprestimo)
        else:
            print("valor solicitado maior q o limite disponivel")


conta1=Conta(123,"baz",0)
conta2=Conta_premium(123,"bazz",0,1000)
conta2.emprestimo()
conta2.saque()
conta2.__str__()











