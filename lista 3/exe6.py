class animal:
    def __init__(self,especie,som):
        self.especie=especie
        self.som=som
    def exibir(self):
        print(self.som)

animal1=animal("dog",'au au')
animal2= animal("cat",'miau miau')
animal2.exibir()
animal1.exibir()

