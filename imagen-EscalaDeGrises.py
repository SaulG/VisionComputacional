import numpy as np
import Tkinter
from PIL import ImageDraw
import Image
import ImageTk

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
imagen = Image.open('comida_indu.png')
imagenModificada = imagen
imagenModificada = escalaDeGrises(imagen)
root = Tkinter.Tk()
tkimage = ImageTk.PhotoImage(imagen)
tkimageMod = ImageTk.PhotoImage(imagenModificada)
Tkinter.Label(root, image = tkimage).pack()
Tkinter.Label(root, image = tkimageMod).pack()
root.mainloop()
