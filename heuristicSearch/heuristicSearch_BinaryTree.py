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



noTaguatinga = Node('Taguatinga',50,60,90)
noTaguatinga.vizinhoAlfa = Node('Ceilandia',50,70,100)
noTaguatinga.vizinhoBeta = Node('Aguas Claras',90,60,132)

noCeilandia = noTaguatinga.vizinhoAlfa
noCeilandia.vizinhoAlfa = noTaguatinga
noCeilandia.vizinhoBeta = Node('Samambaia',32,70,90)

noSamambaia = noCeilandia.vizinhoBeta
noSamambaia.vizinhoAlfa = noCeilandia
noSamambaia.vizinhoBeta = Node('Recanto das Emas',32,53,90)
noSamambaia.vizinhoZulu = noTaguatinga

noTaguatinga.vizinhoZulu = noSamambaia

noRecanto = noSamambaia.vizinhoBeta
noRecanto.vizinhoAlfa = noSamambaia
noRecanto.vizinhoBeta = Node('Guara',53,56,57)

noGuara = noRecanto.vizinhoBeta
noGuara.vizinhoAlfa = noRecanto
noGuara.vizinhoBeta = Node('Bandeirante',90,56,40)

noAguasclaras = noTaguatinga.vizinhoBeta
noAguasclaras.vizinhoAlfa = noGuara.vizinhoBeta
noAguasclaras.vizinhoBeta = noTaguatinga


noBandeirante = noAguasclaras.vizinhoAlfa

pesoEuristico = {'Ceilandia':200,'Taguatinga':180,'Samambaia':170,'Recanto das Emas':160,'Aguas Claras': 150,'Guara':100,'Bandeirante':0}

input("A cidade procurada será o Bandeirando a partir da Ceilandia: ")
nome = 'Bandeirante'
#Busca em largura
queue = [noCeilandia]
nomes = []
distancia_percorrida = 0

while len(queue)!=0:
  noAtual = queue.pop(0)
  print(noAtual.nome)
  nomes.append(noAtual.nome)
  if noAtual.nome == nome:
      print("Nome encontrado!")
      queue.append("")
      break   
    
  #Pesquisa euristica
  zulu = 9999999
  alfa = noAtual.distanciaAlfa + distancia_percorrida + pesoEuristico[noAtual.vizinhoAlfa.nome]
  beta = noAtual.distanciaBeta + distancia_percorrida + pesoEuristico[noAtual.vizinhoBeta.nome]
  if noAtual.vizinhoZulu != None:
    zulu = noAtual.distanciaZulu + distancia_percorrida + pesoEuristico[noAtual.vizinhoZulu.nome]

  x = min(alfa,beta,zulu)
  if x == alfa:
      queue.append(noAtual.vizinhoAlfa)
      distancia_percorrida = noAtual.distanciaAlfa + distancia_percorrida
  elif x == beta:
      queue.append(noAtual.vizinhoBeta)
      distancia_percorrida = noAtual.distanciaBeta + distancia_percorrida
  elif x == zulu:
      queue.append(noAtual.vizinhoZulu)
      distancia_percorrida = noAtual.distanciaZulu + distancia_percorrida
  if len(queue) == 0:
    print("O nome não foi encontrado")

print("Os valores percorridos foram:{}".format(nomes))


