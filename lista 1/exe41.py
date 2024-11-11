def fibonacci(n):
    sequencia=[0,1]
    while len(sequencia)<n:
        proximo=sequencia[-1]+sequencia[-2]
        sequencia.append(proximo)
    return sequencia
n=int(input("dgt um numero"))
print(fibonacci(n))










