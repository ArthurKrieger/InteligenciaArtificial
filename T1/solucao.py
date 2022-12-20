from collections import deque
import heapq

class Nodo:
    def __init__(self, estado, pai, acao, custo,caminho=[],comparator=None):
        self.estado=estado
        self.pai=pai
        self.acao=acao
        self.custo=custo
        self.caminho=caminho
        self.comparator=comparator
    def __repr__(self) -> str:
        return str(self)
    def __str__(self):
        return self.estado+" "+self.pai+" "+self.acao+" "+str(self.custo)
    def __le__(self,other):
        return self.comparator(self.estado)+self.custo<=self.comparator(other.estado)+other.custo
    def __lt__(self,other):
        return self.comparator(self.estado)+self.custo<self.comparator(other.estado)+other.custo

def sucessor(estado):
    lista = []
    pos = estado.find("_")
    if(pos != 0 and pos!= 3 and pos!=6):
        lista.append(("esquerda",changePos(estado,pos,pos-1)))
    if(pos !=2 and pos!=5 and pos!=8):
         lista.append(("direita",changePos(estado,pos,pos+1)))
    if(pos !=0 and pos!=1 and pos!=2):
         lista.append(("acima",changePos(estado,pos,pos-3)))
    if(pos !=6 and pos!=7 and pos!=8):
         lista.append(("abaixo",changePos(estado,pos,pos+3)))
    return lista       
      

def expande(nodo):
    lista = []
    for pair in sucessor(nodo.estado):
        caminho = nodo.caminho.copy()
        caminho.append(pair[0])
        lista.append(Nodo(pair[1],nodo,pair[0],nodo.custo+1,caminho,nodo.comparator))
    return lista
    

def bfs(estado):
    x = set()
    f = deque()
    f.append(Nodo(estado,None,None,0,[]))
    while(f):
        curr = f.popleft()
        if(curr.estado=="12345678_"):
            return curr.caminho
        else:
            x.add(curr.estado)
            for e in expande(curr):
                if e.estado not in x:
                    f.append(e)
def dfs(estado):
    x = set()
    a=0
    f = deque()
    f.append(Nodo(estado,None,None,0,[]))
    while(f):
        curr = f.pop()
        if(curr.estado=="12345678_"):
            return curr.caminho
        else:
            x.add(curr.estado)
            for e in expande(curr):
                if e.estado not in x and e.custo<100:
                    f.append(e)


def astar_hamming(estado):
    x = set()
    priorityQueue = []
    heapq.heappush(priorityQueue,Nodo(estado,None,None,0,[],hamming))
    while(priorityQueue):
        curr = heapq.heappop(priorityQueue)
        if(curr.estado=="12345678_"):
            return curr.caminho
        else:
            x.add(curr.estado)
            for e in expande(curr):
                if e.estado not in x:
                    heapq.heappush(priorityQueue,e)

def astar_manhattan(estado):
    x = set()
    priorityQueue = []
    heapq.heappush(priorityQueue,Nodo(estado,None,None,0,[],manhattan))
    while(priorityQueue):
        curr = heapq.heappop(priorityQueue)
        if(curr.estado=="12345678_"):
            return curr.caminho
        else:
            x.add(curr.estado)
            for e in expande(curr):
                if e.estado not in x:
                    heapq.heappush(priorityQueue,e)

def changePos(estado,x,y):
    lista = list(estado)
    temp = lista[x]
    lista[x]=lista[y]
    lista[y]=temp
    return "".join(lista)

def hamming(estado):
    acc = 0
    desired = "12345678_"
    for i in range(len(estado)):
        if(estado[i]!=desired[i]):
            acc = acc+1
    return acc

def manhattan(estado):
	acc = 0
	desired = "12345678_"
	for i in range(len(estado)):
		des = desired.find(estado[i])
		if (estado[i] != "_"):
			acc = acc + abs(i%3-des%3) + abs(i//3-des//3)
	return acc