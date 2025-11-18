#1
class Carro:
    def __init__(self, mostrar_estado):
        self.mostrar_estado = mostrar_estado

c1 = Carro('Novo')
c2 = Carro('Usado')
print(c1.mostrar_estado)
print(c2.mostrar_estado)

#2
class Motor:
    def __init__(self):
        self.ligado = False
    def ligar_motor(self):
        self.ligado = True
car = Motor()
car.ligar_motor()
print(car.ligado)

#3
class Banco:
    def __init__(self, clientes):
        self.clientes = clientes
        
n1 = Banco('Jose')
n2 = Banco('Maria')
n3 = Banco('Joao')  

print(n1.clientes)
print(n2.clientes)
print(n3.clientes)

#4
class Produto:
    def __init__(self, preço):
        self.preço = preço
    def desconto(self, percentual):
        self.preço -= self.preço * (percentual / 100)
p = Produto(100)
p.desconto(10)
print(p.preço)

#5
class Pessoa:
    def __init__(self):
      print("Pessoa criada!")
      
#6

def soma(a,b):
    return soma()
print(21+2)

#7
def soma_pares():
    