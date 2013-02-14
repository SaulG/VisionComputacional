def dfs(posicion):
    if marcado(posicion):
        return
    else:
        marca(posicion)
        for fulano in vecinos(posicion):
            bfs(fulano)

def bfs(cola):
    pos = cola.primero()
    marca(pos)
    for vecinos in vecinos(pos):
        if not marcado(vecino):
            cola.append(vecino)
        if not cola.vacio():
            bfs(cola)
