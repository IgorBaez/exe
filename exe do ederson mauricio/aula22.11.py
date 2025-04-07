class ControRemoto:
    def __init__(self,cor,altura,profun,largura):
        self.cor=cor
        self.altura=altura
        self.profun=profun
        self.largura=largura

    def mudar_canal(self,botao):
        if botao=="+":
            print("\naumenta canal\n")
        elif botao=="-":
            print("\ndiminuir canal\n")
        elif botao=="1":
            print("\ntv ligada\n")
        elif botao=="2":
            print("\ntv desligada\n")
        elif botao=="n":
            nome=input("dgt seu nome ")
            email=input("dgt seu email ")
            telefone=("dgt seu telefone ")
            cpf=input("dgt seu cpf ")
            plano=input("dgt qual plano\n1-Padrão\n2-Premium\n3-Padrão com anúncios ")
            cartao_credito=input("dgt os dados do cartao de credito ")
            print("Dados informados ",nome,email,telefone,cpf,plano,cartao_credito,"\n")

        else:
            print("\nValor invalido\n")
    

contro_tv_cozinha=ControRemoto("preto",12,2,5)
contro_tv_sala=ControRemoto("branco",15,3,7)
contro_tv_quarto1=ControRemoto("branco",12,2,6)
contro_tv_quarto2=ControRemoto("cinza",16,1,3)
contro_tv_banehiro=ControRemoto("preto",12,2,5)

contro_tv_cozinha.mudar_canal(input("(tv da cozinha)\n+ para aumentar\n- para dimunir de canal\n1 para liagar tv\n2 para desligar tv\nn para Netflix\n "))
contro_tv_sala.mudar_canal(input("(tv da sala)\n+ para aumentar\n- para dimunir de canal\n1 para liagar tv\n2 para desligar tv\nn para Netflix\n "))
contro_tv_quarto1.mudar_canal(input("(tv da quarto1)\n+ para aumentar\n- para dimunir de canal\n1 para liagar tv\n2 para desligar tv\nn para Netflix\n  "))
contro_tv_quarto2.mudar_canal(input("(tv da quarto2)\n+ para aumentar\n- para dimunir de canal\n1 para liagar tv\n2 para desligar tv\nn para Netflix\n  "))
contro_tv_banehiro.mudar_canal(input("(tv da banheiro)\n+ para aumentar\n- para dimunir de canal\n1 para liagar tv\n2 para desligar tv\nn para Netflix\n  "))











