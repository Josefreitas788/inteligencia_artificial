from tree import drawTree 
import random as rd

class Node:

  def __init__(self, nome, distanciaAlfa, distanciaBeta, distanciaZulu ,alfa=None, beta=None, zulu=None):
    #TODO 
    '''Para a pesquisa heuristica é preciso é preciso subtrair a distancia percorrida pela distancia pelo distancia que falta e escolher o menor valor'''
    self.nome = nome
    self.vizinhoAlfa = alfa
    self.vizinhoBeta = beta
    self.vizinhoZulu = alfa
    self.distanciaAlfa = distanciaAlfa
    self.distanciaBeta = distanciaBeta
    self.distanciaZulu = distanciaZulu

  def insert(self, nome):
        x = rd.randint(0,1)
        if x == 0:
            if self.left is None:
               self.left = Node(nome)
            else:
               self.left.insert(nome)
        else:
               if self.right is None:
                  self.right = Node(nome)
               else:
                  self.right.insert(nome)


noTaguatinga = Node('Taguatinga',50,60,90)
noTaguatinga.vizinhoAlfa = Node('Ceilandia',50,70,100)
noTaguatinga.vizinhoBeta = Node('Aguas Claras',90,60,132)

noCeilandia = noTaguatinga.vizinhoAlfa
noCeialndia.vizinhoAlfa = noTaguatinga
noCeilandia.vizinhoBeta = Node('Samambaia',32,70,83)

noSamambaia = noCeilandia.vizinhoBeta
noSamambaia.vizinhoAlfa = no
for cidade in lista:
      tree.insert(cidade)
      

drawTree(tree)

nome = input("Digite um nome:")

#Busca em largura
queue = [tree]
nomes = []

while len(queue)!=0:
  NoAtual = queue.pop(0)
  nomes.append(NoAtual.nome)
  if Atual.nome == nome:
      print("Nome encontrado!")
      queue.append("")
      break   
  if NoAtual.left!=None:
    queue.append(NoAtual.left)
  if NoAtual.right!=None:
    queue.append(NoAtual.right)
if len(queue) == 0:
    print("O nome não foi encontrado")

print("Os valores percorridos foram:{}".format(nomes))


