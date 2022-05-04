import drawtree as dr


class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

tree = Node(47) #The root node of our binary tree
tree.left = Node(36)
tree.right = Node(66)

tree.left.left = Node(25)
tree.left.right = Node(39)
tree.left.right.left = Node(38)
tree.left.right.right = Node(42)

tree.right.left = Node(63)
tree.right.left.right = Node(64)
tree.right.right = Node(68)

#dr.draw_level_order(tree)

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

value = int(input("Type a value to search for..."))

#Binary Search...
node = tree
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

