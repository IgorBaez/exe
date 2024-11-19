import soma,subtrair,multiplica,divide
class Calculadora:
    def __init__():
        while True:
            print("1-SOMA \n2-SUBTRAÇÃO\n3-MULTIPLICAÇÃO\n4-DIVISÃO\n0-SAIR\n")
            x=int(input("opção desejada "))
            if x<0 or x>4:
                print("Valor informado invalido")
                continue
            if x==0:
                print("Saindo...")
                break
            while True:
                valor1=float(input("digite o primeiro valor: "))
                valor2=float(input("digite o segundo valor: "))
                if valor1==0 or valor2==0:
                    print("Valor informado não utilizavel")
                    continue
                break
            if x==1:
                    print("\nO resultado :",soma.soma(valor1,valor2),"\n")
            elif x==2:
                    print("\nO resultado :",subtrair.subtrair(valor1,valor2),"\n")
            elif x==3:
                print("\nO resultado :",multiplica.multiplica(valor1,valor2),"\n")
            elif x==4:
                print("\nO resultado :",divide.divide(valor1,valor2),"\n")
    __init__()