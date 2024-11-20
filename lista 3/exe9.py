class aluno:
    def __init__(self,nota):
        self.nota=nota
    def exibir(self):
        if self.nota>=7:
            print("aprovado")
        else:
            print("reprovado")
nota=aluno(10)
nota1=aluno(6)
nota.exibir()
nota1.exibir()
        