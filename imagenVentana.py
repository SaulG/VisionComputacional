import numpy as np
import Tkinter
from PIL import ImageDraw
import Image
import ImageTk

imagen = Image.open('comida_indu.png')

root = Tkinter.Tk()
tkimage = ImageTk.PhotoImage(imagen)
Tkinter.Label(root, image = tkimage).pack()
root.mainloop()
