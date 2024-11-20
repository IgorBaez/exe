class ContaBancaria:
        def __init__(self, saldo_inicial=0):
            self.saldo = saldo_inicial
    
        def deposito(self, valor):
            if valor > 0:
                self.saldo += valor
                print(f"Depósito de R$",valor," realizado com sucesso!")
            else:
                print("Valor de depósito inválido. O valor deve ser positivo.")
    
        def sacar(self, valor):
            # Método para sacar dinheiro da conta
            if valor > 0:
                if valor <= self.saldo:
                    self.saldo -= valor
                    print(f"Saque de R${valor:.2f} realizado com sucesso!")
                else:
                    print("Saldo insuficiente para o saque.")
            else:
                print("Valor de saque inválido. O valor deve ser positivo.")
    

baz=ContaBancaria(10)
baz.sacar(1)
baz.deposito(2)
