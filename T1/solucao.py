class Nodo:
    def __init__(self, estado, pai, acao, custo):
        self.estado=estado
        self.pai=pai
        self.acao=acao
        self.custo=custo
    def __repr__(self) -> str:
        return str(self)
    def __str__(self):
        return self.estado+" "+self.pai+" "+self.acao+" "+str(self.custo)

def sucessor(estado):
    lista = []
    pos = estado.find("_")
    if(pos != 0 != 3 !=6):
        lista.append(("esquerda",changePos(estado,pos,pos-1)))
    if(pos !=2 !=4 !=8):
         lista.append(("direita",changePos(estado,pos,pos+1)))
    if(pos !=1 !=2 !=3):
         lista.append(("acima",changePos(estado,pos,pos-3)))
    if(pos !=6 !=7 !=8):
         lista.append(("abaixo",changePos(estado,pos,pos+3)))
    return lista       
      

def expande(nodo):
    return list(map(lambda e:Nodo(e[0],nodo.estado,e[1],nodo.custo+1),sucessor(nodo.estado)))
   


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


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