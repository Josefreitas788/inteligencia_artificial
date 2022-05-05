from tree import drawTree 
import random as rd

class Node:

  def __init__(self, nome, left=None, right=None):
    self.nome = nome
    self.left = left
    self.right = right
  
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

f =  open('cidades.txt')
lista = f.read()
lista = lista.split(',')
lista.pop()
#lista = [list(row) for row in lista.columns]
print(lista)
tree = Node('Brasil')
for cidade in lista:
      tree.insert(cidade)
      

drawTree(tree)

nome = input("Digite um nome:")

#Busca em largura
queue = [tree]
nomes = []

while len(queue)!=0:
  currentNode = queue.pop(0)
  nomes.append(currentNode.nome)
  if currentNode.nome == nome:
      print("Nome encontrado!")
      queue.append("")
      break
      
  if currentNode.left!=None:
    queue.append(currentNode.left)
  if currentNode.right!=None:
    queue.append(currentNode.right)
if len(queue) == 0:
    print("O nome não foi encontrado")

print("Os valores percorridos foram:{}".format(nomes))


