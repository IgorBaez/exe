class Relogio:
    def __init__(self,hr,mn,seg):
        self.hr=hr
        self.mn=mn
        self.seg=seg
    def exibir(self):
        print(self.hr,self.mn,self.seg,sep=":")
x=Relogio(10,12,58)
x.exibir()