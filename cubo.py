class Cubo:
    '''Classe para calcular o cubo de um número'''

    def __init__(self, valor):
        self.x=valor
        print("Objeto Criado")

    def calculacubo(self):
        cubox =self.x * self.x *self.x
        return ("o valor calculado é :" + str(cubox))
'''  
print(type(Cubo))
teste=Cubo(400)
c=teste.calculacubo()
print(c)
'''
class Gato:
    tipo_animal="felino" #Atributo de classe
    def __init__(self,nome):
        self.nome=nome
        print("O seu gato chama ", self.nome)

    def peso_gato(self, peso):
        self.peso=peso
        if (self.peso> 5.0):
                return ("É seu  gato está gordinho")
        elif (self.peso>3.5):
                return ("Peso parece normal")
        else:
                return ("o animal está abaixo do peso")

    def _dieta_gato(self):
        self.msg ="Está tudo bem"
        if (self.peso>=5.0):
            self.msg="Precisa reduzir a comida do gato"
        if (self.peso<=3.5):
            self.msg="Precisa aumentar a comida do gato"

        return self.msg

    def dados_gato(self):
        print("\n O gato", self.nome, "esta com ", self.peso, "KG")
        print(self._dieta_gato())

nome_gato=input("Digite o nome do seu gato: ")
g1 =Gato(nome_gato)
peso=float(input("\nQual o peso do seu gato, em Kg ?"))
c=g1.peso_gato(peso)
print (" O gato ", g1.nome, " tem o peso de ", peso,  c)
g1.dados_gato()








#Gato.tipo_animal="PET "    
#g1=Gato("Cristal")
#g2=Gato("gordinho")

#print(g1.tipo_animal, " = ", g1.nome)
#print(g2.tipo_animal, " = ", g2.nome)

#print(g1.nome)
#print(g2.nome)


#nome_gato=input("Digite o nome do seu gato")
#g1=Gato(nome_gato)

        