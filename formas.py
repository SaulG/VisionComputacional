def load():
    entrada = open('formas.txt', 'r')
    imagen = list()
    altura = 0
    ancho = None
    for linea in entrada.readlines():
        linea = linea.strip()
        k = len(linea)
        if k > 0:
            if ancho is None:
                ancho = k
            else:
                if not ancho == k:
                    print 'La imagen no es un rectangulo.'
                    entrada.close()
                    return (None, None, None)
            fila = list()
            for c in linea:
                fila.append(c)
            imagen.append(fila)
            altura += 1
            #print linea
    entrada.close()
    return (imagen, ancho, altura)

def bfs(imagen, simbolo, original, cola, ancho, altura):
    (fila, columna) = cola.pop(0)
    actual = imagen[fila][columna]
    if not actual == original:
        return False
    imagen[fila][columna] = simbolo
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            candidato = (fila + dy, columna + dx)
            if candidato[0] >= 0 and candidato[0] < altura and \
                    candidato[1] >= 0 and candidato[1] < ancho:
                contenido = imagen[candidato[0]][candidato[1]]
                if contenido == original:
                    cola.append(candidato)
    return True

def imprime(imagen):
    cadena = ''
    for linea in imagen:
        for columna in linea:
            cadena += columna
        cadena += '\n'
    print cadena
    return

def espera():
    raw_input('\nPica enter para continuar')
    return

def main():
    (imagen, ancho, altura) = load()
    if imagen is None:
        return
    imprime(imagen)
    espera()
    total = ancho * altura
    agregados = 0
    grupo = 1
    grupos = list()
    max = 0
    fondo = None
    while agregados < total:
        nuevo = None
        for fila in xrange(altura):
            for columna in xrange(ancho):
                original = imagen[fila][columna]
                if not original in grupos:
                    # print 'Separando los %s en grupo %d.' % (original, grupo)
                    nuevo = '%d'% grupo
                    break
            if not nuevo is None:
                break
        cola = list()
        cola.append((fila, columna))
        antes = agregados
        while len(cola) > 0:
            if bfs(imagen, nuevo, original, cola, ancho, altura):
                agregados += 1
        grupos.append(original)
        grupos.append(nuevo)
        pixeles = agregados - antes
        print 'Grupo %s (de los %s) tiene %d pixeles' \
            % (nuevo, original, pixeles)
        if pixeles > max:
            max = pixeles
            fondo = grupo
        grupo += 1
    print 'Grupo %d parece ser el fondo' % fondo
    espera()
    imprime(imagen)
    return

main()
