class Conta_Corrente:
    def __init__(self,N_conta,nome_corren,saldo):
        self.N_conta=N_conta
        self.nome_corren=nome_corren
        self.saldo=saldo
    def aletrar_nome(self):
        print(self.nome_corren)
        self.nome_corren=input("dgt o nome desejado: ")
        print(self.nome_corren)

    def deposito(self):
        print(self.saldo)
        self.saldo+=float(input("dgt o valor do deposito"))
        print(self.saldo)

    def saque(self):
        self.saldo-=float(input("dgt o valor do saque"))
        if self.saldo<=0:
            print("saldo insuficiente")
        elif self.saldo>0:
            print(self.saldo)

conta=Conta_Corrente(123213,"baz",0)
conta.deposito()
conta.saque()





