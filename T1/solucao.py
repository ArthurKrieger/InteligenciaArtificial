from collections import deque
class Nodo:
    def __init__(self, estado, pai, acao, custo,caminho):
        self.estado=estado
        self.pai=pai
        self.acao=acao
        self.custo=custo
        self.caminho=caminho
    def __repr__(self) -> str:
        return str(self)
    def __str__(self):
        return self.estado+" "+self.pai+" "+self.acao+" "+str(self.custo)

def sucessor(estado):
    lista = []
    pos = estado.find("_")
    if(pos != 0 and pos!= 3 and pos!=6):
        lista.append(("esquerda",changePos(estado,pos,pos-1)))
    if(pos !=2 and pos!=5 and pos!=8):
         lista.append(("direita",changePos(estado,pos,pos+1)))
    if(pos !=1 and pos!=2 and pos!=3):
         lista.append(("acima",changePos(estado,pos,pos-3)))
    if(pos !=6 and pos!=7 and pos!=8):
         lista.append(("abaixo",changePos(estado,pos,pos+3)))
    return lista       
      

def expande(nodo):
    lista = []
    for pair in sucessor(nodo.estado):
        caminho = nodo.caminho.copy()
        caminho.append(pair[0])
        lista.append(Nodo(pair[1],nodo.estado,pair[0],nodo.custo+1,caminho))
    return lista


def bfs(estado):
    x = set()
    f = deque()
    f.append(Nodo(estado,None,None,0,[]))
    while(True):
        if not f:
            raise RuntimeError
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
    f = deque()

    f.append(Nodo(estado,None,None,0,[]))
    while(True):
        if not f:
            raise RuntimeError
        curr = f.pop()
        if(curr.estado=="12345678_"):
            return curr.caminho
        else:
            x.add(curr.estado)
            for e in expande(curr):
                if e.estado not in x:
                   f.append(e)


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

def changePos(estado,x,y):
    lista = list(estado)
    temp = lista[x]
    lista[x]=lista[y]
    lista[y]=temp
    return "".join(lista)