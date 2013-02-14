import numpy as np
from Tkinter import *
from PIL import ImageDraw
import Image
import ImageTk
from sys import argv
from random import random
from random import choice

#Toma como parametro la imagen original y la densisdad de ruido
def efectoSaltPepper(original, densidadRuido):
    #toma las proporciones la imagen
    width, height = original.size
    # imprime proporciones
    print width, height
    #lo convierte en escala de grises
    original = original.convert('L')
    #se crea una nueva imagen con las proporciones de la original
    modificado = Image.new(mode='L', size =(width,height))
    #se carga la imagen original para poder manipularlo
    org = original.load()
    #se carga la imagen modifica para poder manipularlo
    mod = modificado.load()
    # se iteran las proporciones para acceder al pixel
    # de la imagen original, según
    for y in xrange(height):
        for x in xrange(width):
            # se toma el pixel
            pixel = org[x,y]
            #dependiendo de la densidad es lo que se toma de probabilidad
            # para definir el pixel como negro o blanco
            #dicho pixel se pasa a una nueva imagen
            if(random() <= densidadRuido):
                if(choice([True, False])):
                       mod[x, y] = 0
                else:
                       mod[x, y] = 255
            else: 
                mod[x,y] = pixel
    #se guarda en un arreglo la imagen cargada
    data = np.array(modificado)
    print data
    print data.shape
    #se crea imagen apartir del arreglo
    im = Image.fromarray(data)
    return im

#Toma como parametro la imagen original
def limpiandoEfectoSaltPepper(original):
    #toma las proporciones de la imagen original
    width, height = original.size
    #imprime las proporciones
    print width, height
    #convierte la imagen en escala de grises
    original = original.convert('L')
    #se crea una imagen nueva apartir de las proporciones de la origina
    modificado = Image.new(mode='L', size = (width, height) )
    #se carga la imagen original para poder manipularlo
    org = original.load()
    #se carga la imagen nueva para poder manipularlo
    mod = modificado.load()
    # se iteran las proporciones de la imagen para acceder al pixel
    for y in xrange(height):
        for x in xrange(width):
            # se obtiene pixel en coordenadas x y y
            pixel = org[x, y]
            #se inicializa contador y totalVecinos
            contador = 0
            totalVecinos = 0
            # se suma cada vecinos en totalVecinos y se agrega un +1 al contador
            try:
                totalVecinos += org[x+1, y]
                contador += 1            
            except:
                pass
            try:
                totalVecinos += org[x-1, y]
                contador += 1
            except:
                pass
            try:
                totalVecinos += org[x, y+1]
                contador += 1
            except:
                pass
            try:
                totalVecinos += org[x, y-1]
                contador += 1
            except:
                pass
            #se toma el promedio de todos los vecinos
            promedio = (totalVecinos * 1.0)/ (contador * 1.0)
            #si la diferencia es mayor a 80 se toma el promedio sino
            #se deja el original
            if abs( promedio - pixel ) > 80:
                mod[x,y] = promedio
            else:
                mod[x,y] = pixel
    #se carga el array en data
    data = np.array(modificado)
    print data
    print data.shape
    # se crea imagen apartir del array
    im = Image.fromarray(data)
    return im

def escalaDeGrises(im):
    width, height = im.size
    print width, height
    im = im.convert('RGB')
    pix = im.load()
    promedio = 0.0
    for y in xrange(height):
            for x in xrange(width):
                r, g, b = pix[x, y]
                promedio = (r+g+b)/3.0
                pix[x, y] = int(promedio), int(promedio), int(promedio)
    data = np.array(im)
    im2 = Image.fromarray(data)
    return im2

#iterarcion recursiva del limpiador del efecto de sal pimienta
def iteracionesLimpiadoDeEfectoSaltPepper(imagen, iteraciones):
    if iteraciones == 0:
        return limpiandoEfectoSaltPepper(imagen)
    return iteracionesLimpiadoDeEfectoSaltPepper(limpiandoEfectoSaltPepper(imagen), iteraciones - 1)
    
def main():
    #carga imagen apartir del parametro argv[1]
    imagen = Image.open(argv[1])
    original = imagen
    escalaGrises = escalaDeGrises(imagen)
    #se crea el efecto sal pimienta dando imagen y densidad de sal y pimienta
    modificado = efectoSaltPepper(escalaGrises, float(argv[2]))
    #se limpia el efecto sal y pimienta apartir de la imagen y el numero de iteraciones
    limpio = iteracionesLimpiadoDeEfectoSaltPepper(modificado, int(argv[3]))
    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    tkimageModf = ImageTk.PhotoImage(modificado)
    tkimageLimpio = ImageTk.PhotoImage(limpio)
    Label(root, image = tkimageModf).pack(side="left")
    Label(root, image = tkimageLimpio).pack(side="right")
    root.mainloop()
main()
