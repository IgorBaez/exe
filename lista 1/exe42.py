list=[]
def soma_recursiva(n):
    x=0
    for a in range(n):
        x+=1
        list.append(x)
print(soma_recursiva(9))
print(list)
print(sum(list))