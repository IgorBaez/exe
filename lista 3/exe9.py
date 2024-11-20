class Aluno:
    def __init__(self,nota):
        self.nota=nota
    def exibir(self):
        if self.nota>=7:
            print("aprovado")
        else:
            print("reprovado")
nota=Aluno(10)
nota1=Aluno(6)
nota.exibir()
nota1.exibir()
        