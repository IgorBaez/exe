import soma,subtrair,multiplica,divide
class Calculadora:

    def body():
            while True:
                while True:
                    print("1-SOMA \n2-SUBTRAÇÃO\n3-MULTIPLICAÇÃO\n4-DIVISÃO\n0-SAIR\n")
                    x= int(input("Digite a opção desejada: "))
                    if x<0 or x>4:
                        print("Valor informado invalido")
                        continue
                    if x==0:
                        print("Saindo...")
                        break
                    break
                while True:
                    valor1=float(input("digite o primeiro valor: "))
                    valor2=float(input("digite o segundo valor: "))
                    if valor1==0 or valor2==0:
                        print("Valor informado não utilizavel")
                        continue
                    break
                if x==1:
                            print(soma.soma(valor1,valor2))
                elif x==2:
                            print(subtrair.subtrair(valor1,valor2))
                elif x==3:
                            print(multiplica.multiplica(valor1,valor2))                
                elif x==4:
                            print(divide.divide(valor1,valor2))
                    
    
