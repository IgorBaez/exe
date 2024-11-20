class Animal:
    def __init__(self,especie,som):
        self.especie=especie
        self.som=som
    def exibir(self):
        print(self.som)

animal1=Animal("dog",'au au')
animal2= Animal("cat",'miau miau')
animal2.exibir()
animal1.exibir()

