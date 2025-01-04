class TV:
    def __init__(self,au_canal,au_vlome):
        self.au_canal=au_canal
        self.au_vlome=au_vlome

    def canal(self):
        print(self.au_canal)
        x=int(input("0 para aumentar\n1 para diminuir"))
        if x==1:
            x=int(input("dgt o canal de 0 a 100"))
            if x<0 or x>100:
                print("canal invalido")
            elif x>-1 or x<101:
                self.au_canal=x
                print(self.au_canal)
        elif x==0:
            x=int(input("dgt o volume de 0 a 100"))
            if x<0 or x>100:
                print("canal invalido")
            elif x>-1 or x<101:
                self.au_vlome=x
                print(self.au_vlome)
            


    #     self.au_canal=int(input("Dgt um canal de 0 a 100"))

    # def diminuir_canal(self):
tv1=TV(0,0)
tv1.canal()
tv1.canal()

















