class bola:
    def __init__(self,cor1,circu,material):
        self.cor1=cor1
        self.circu=circu
        self.material=material
    def troca_cor(self):
        self.cor1=input("dgt a cor da bola ")
        print("a cor atual e ",self.cor1)
       

    def cor(self):
        print("a cor atual e ",self.cor1)


bola1=bola("preta",12,"plastico")
bola1.cor()
bola1.troca_cor()
bola1.cor()

bola2=bola("marrom",12,"plastico")
bola2.cor()
bola2.troca_cor()
bola2.cor()



        