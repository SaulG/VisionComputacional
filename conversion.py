import math

#Proporciones son tomados de esta manera
# 16:9 donde 16 = a y 9 es igual a b
# c va ser los pixeles
def resolucion(a, b, c):
    tot = math.floor(math.sqrt(c/a*b))
    totAncho = tot * b
    totLargo = tot * a
    Total = totLargo * totAncho
    print Total

def main():
    pixeles = raw_input('Teclea los pixeles(abrev. 1 pxl, 1 kpxl, 1 mpx, 1 gpx):')
    pixeles.split(' ')
    num_pix = int(pixeles[0])
    print num_pix
    pxl = pixeles[1]
    print pixeles
    exponente = 0
    if(pxl == 'pxl'):
        exponente = 1
    elif(pxl == 'kpxl'):
        exponente = 2
    elif(pxl == 'mpx'):
        exponente = 3
    elif(pxl == 'gpx'):
        exponente = 4
    pixelesR = (1024 **exponente) * (num_pix * 1.0)
    proporciones = raw_input('Teclea la resolution:')
    proporciones = proporciones.split(':')
    print proporciones, pixeles
    resolucion(pixelesR, float(proporciones[0]), float(proporciones[1]))
main()
