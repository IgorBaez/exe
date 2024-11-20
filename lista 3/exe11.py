class ContaBancaria:
        def __init__(self, saldo_inicial=0):
            self.saldo = saldo_inicial
    
        def deposito(self, valor):
            if valor > 0:
                self.saldo += valor
                print("Depósito de R$",valor," realizado com sucesso")
            else:
                print("Valor inválido")
    
        def sacar(self, valor):
            if valor > 0:
                if valor <= self.saldo:
                    self.saldo -= valor
                    print ("Saque de R$",valor," realizado com sucesso!")
                else:
                    print("Saldo insuficiente")
            else:
                print("Valor de saque inválido")
    

baz=ContaBancaria(10)
baz.sacar(1)
baz.deposito(2)
