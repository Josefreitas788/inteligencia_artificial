from tree import drawTree 
import random as rd

class Node:

  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
  
  def insert(self, value):
        x = rd.randint(0,1)
        if x == 0:
            if self.left is None:
               self.left = Node(value)
            else:
               self.left.insert(value)
        else:
               if self.right is None:
                  self.right = Node(value)
               else:
                  self.right.insert(value)

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
  nomes.append(currentNode.value)
  if currentNode.value == nome:
      print("Nome endcontrado!")
      break
      
  if currentNode.left!=None:
    queue.append(currentNode.left)
  if currentNode.right!=None:
    queue.append(currentNode.right)
if len(queue) == 0:
    print("O nome não foi encontrado")

print("Os valores percorridos foram:{}".format(nomes))


