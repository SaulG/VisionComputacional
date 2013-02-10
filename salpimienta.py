import numpy as np
import Tkinter
from PIL import ImageDraw
import Image
import ImageTk
from sys import argv
from random import random
from random import choice

def efectoSaltPepper(original, densidadRuido):
    width, height = original.size
    print width, height
    original = original.convert('L')
    modificado = Image.new(mode='L', size =(width,height))
    org = original.load()
    mod = modificado.load()
    for y in xrange(height):
        for x in xrange(width):
            pixel = org[x,y]
            if(random() <= densidadRuido):
                if(choice([True, False])):
                       mod[x, y] = 0
                else:
                       mod[x, y] = 255
            else: 
                mod[x,y] = pixel
    data = np.array(modificado)
    print data
    print data.shape
    im = Image.fromarray(data)
    return im

def limpiandoEfectoSaltPepper(original):
    width, height = original.size
    print width, height
    original = original.convert('L')
    modificado = Image.new(mode='L', size = (width, height) )
    org = original.load()
    mod = modificado.load()
    for y in xrange(height):
        for x in xrange(width):
            pixel = org[x, y]
            contador = 0
            totalVecinos = 0
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
            promedio = (totalVecinos * 1.0)/ (contador * 1.0)
            if abs( promedio - pixel ) > 80:
                mod[x,y] = promedio
            else:
                mod[x,y] = pixel
    data = np.array(modificado)
    print data
    print data.shape
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

def iteracionesLimpiadoDeEfectoSaltPepper(imagen, iteraciones):
    if iteraciones == 0:
        return limpiandoEfectoSaltPepper(imagen)
    return iteracionesLimpiadoDeEfectoSaltPepper(limpiandoEfectoSaltPepper(imagen), iteraciones - 1)
    
def main():
    imagen = Image.open(argv[1])
    original = imagen
    escalaGrises = escalaDeGrises(imagen)
    modificado = efectoSaltPepper(escalaGrises, float(argv[2]))
    limpio = iteracionesLimpiadoDeEfectoSaltPepper(modificado, int(argv[3]))
    root = Tkinter.Tk()
    tkimageModf = ImageTk.PhotoImage(modificado)
    tkimageLimpio = ImageTk.PhotoImage(limpio)
    Tkinter.Label(root, image = tkimageModf).pack()
    Tkinter.Label(root, image = tkimageLimpio).pack()
    root.mainloop()
main()
