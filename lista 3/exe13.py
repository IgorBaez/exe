class veiculo:
    def __init__(self,modelo, velocidade):
        self.modelo=modelo
        self.velocidade=velocidade 

    def aumento_Velo(self, incremento):
        incremento+=self.velocidade
        print("modelo :",self.modelo,'\nvelocidade anterior:',self.velocidade,"\nvelocidade atual :",incremento)

x=veiculo("ferrari",290)
x.aumento_Velo(200)

