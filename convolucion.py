import numpy as np
import Tkinter
from PIL import ImageDraw
import Image
import ImageTk
from sys import argv
import time

def convolucion(imagen, h):
    iwidth, iheight = imagen.size
    imagen = imagen.convert('L')
    im = imagen.load()
    mheight, mwidth = h.shape
    print "Imagen size: ",imagen.size
    print "H: ",h.shape
    g = np.zeros(shape=(iheight, iwidth))
    for x in xrange(iheight):
        for y in xrange(iwidth):
            sum = 0.0
            for j in xrange(mheight):
                zj = ( j - ( mheight / 2 ) )
                for i in xrange(mwidth):
                    zi = ( i - ( mwidth / 2 ) )
                    try:
                        sum += im[y + zi, x + zj] * h[i,j]
                    except:
                        pass
            print x, y
            g[x,y] = sum
    print "Convolucion"
    print g
    return g

def filtro(original):
    width, height = original.size
    print width, height
    original = original.convert('L')
    modificado = Image.new(mode='L', size =(width,height))
    org = original.load()
    mod = modificado.load()
    contador = 0
    min = 0
    max = 0
    for y in xrange(height):
        for x in xrange(width):
            pixel = org[x,y]
            if min >= pixel:
                min = pixel
            if max <= pixel:
                max = pixel
    print "MAX:",max," MIN:",min
    for y in xrange(height):
        for x in xrange(width):
            pixel = org[x,y]
            try:
                pixel += org[x-1,y]
                contador+=1
            except:
                None
            try:
                pixel += org[x+1,y]
                contador+=1
            except:
                None
            try:
                pixel += org[x,y+1]
                contador+=1
            except:
                None
            try:
                pixel += org[x,y-1]
                contador+=1
            except:
                None
            promedio = (pixel) / (contador)
            r = max - min
            prop = 256.0 / r
            p = int((promedio -min) * prop)
            if p <= 90:
                mod[x,y] = 0
            else: 
                mod[x,y] = 255
            print mod[x,y]
            print x,y
            contador = 1
            pixel = 0
    data = np.array(modificado)
    print data
    print data.shape
    im = Image.fromarray(data)
    return im
         
def filtroPorNumeros(im,n):
    for x in xrange(n):
        im = filtro(im)
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

def nuevaImagen(matriz):
    height, width = matriz.shape
    print matriz.shape
    imagen = Image.new(mode='L', size =(width,height))
    im = imagen.load()
    print imagen.size
    for x in xrange(height):
        for y in xrange(width):
            im[y, x] = matriz[x, y]
    data = np.array(imagen)
    print data
    im = Image.fromarray(data)
    return im

def binarizacion(imagen):
    width, height = imagen.size
    imagen = imagen.convert('L')
    im = imagen.load()
    for x in xrange(height):
        for y in xrange(width):
            pixel = im[y, x]
            if pixel < 3:
                im[y, x] = 0
            else:
                im[y, x] = 255
    data = np.array(imagen)
    im = Image.fromarray(data)
    return im

def main():
    imagen = Image.open(argv[1])
    original = imagen
    escalaGrises = escalaDeGrises(imagen)
    px = np.array([[-1,0,1], [-1,0,1], [-1,0,1]])
    py = np.array([[1,1,1], [0,0,0], [-1,-1,-1]])
    t1 = time.time()
    gx = convolucion(escalaGrises, px)
    gx = gx ** 2
    gy = convolucion(escalaGrises, py)
    gy = gy ** 2
    g = (gx + gy ) ** 1.0/2.0
    print g
    min = np.min(g)
    max = np.max(g)
    h, w = g.shape
    minimos = np.ones(shape=(h, w))
    minimos *= min
    g = g - min
    print "Restando el minimo", g
    g = g / (max - min)
    print "Dividiendo el max-min",g
    print "Max: ",np.max(g)," Min: ",np.min(g)
    bn = np.ones(shape=(h, w))
    bn *= 255
    g = g * bn
    print "Max: ",np.max(g)," Min: ",np.min(g)
    imagen_nueva = nuevaImagen(g)
    imagen_binaria = binarizacion(imagen_nueva)
    root = Tkinter.Tk()
    tkimageModf = ImageTk.PhotoImage(imagen_nueva)
    tkimageOrig = ImageTk.PhotoImage(imagen_binaria)
    Tkinter.Label(root, image = tkimageModf).pack(side="left")
    Tkinter.Label(root, image = tkimageOrig).pack(side="right")
    t2 =time.time()
    print "Tiempo total: ",t2-t1
    root.mainloop()
main()
