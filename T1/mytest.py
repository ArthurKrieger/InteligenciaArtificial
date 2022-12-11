import solucao

succ_esperados = {("abaixo", "2435_1687"), ("esquerda", "_23541687"), ("direita", "23_541687")}
sucessores = solucao.sucessor("2_3541687")
nodo = solucao.Nodo("2_3541687",None,None,0)
print(solucao.expande(nodo))