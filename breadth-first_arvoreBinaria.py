from tree import drawTree #This library will only be used to draw the binary tree on the screen
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
#lista = [list(row) for row in lista.columns]
print(lista)
tree = Node("Brasil")
for cidade in lista:
    tree.insert(cidade)

    


drawTree(tree)

#---> Implementation of the Breadth-First Traversal:

#We first initialise a queue with a single node: the root of the tree
print("\n---> Breath First Traversal:")
queue = [tree]
values = []

while len(queue)!=0:
  #Dequeue the first node
  currentNode = queue.pop(0)
  #Read the node value:
  values.append(currentNode.value)
  
  #Enqueue child nodes (if any)
  if currentNode.left!=None:
    #Enqueue the left node at the end of the queue:
    queue.append(currentNode.left)
  if currentNode.right!=None:
    #Enqueue the right node at the end of the queue:
    queue.append(currentNode.right)
    
#The end, let's print the list of values resulting from the breadth first traversal of our tree:
print(values)

value = input("Type a value to search for...")

#TODO busca cega 
found=False
while node!=None:
  if value==node.value:
    found=True
    print("Yeah value found!")
    break
  elif value<node.value:
    node = node.left
  elif value>node.value:
    node = node.right
  
if found==False:
  print("Not found")

