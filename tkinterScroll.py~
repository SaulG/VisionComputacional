from Tkinter import *

## Main window
root = Tk()
## Grid sizing behavior in window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
## Canvas
cnv = Canvas(root)
cnv.grid(row=0, column=0, sticky='nswe')
## Scrollbars for canvas
hScroll = Scrollbar(root, orient=HORIZONTAL, command=cnv.xview)
hScroll.grid(row=1, column=0, sticky='we')
vScroll = Scrollbar(root, orient=VERTICAL, command=cnv.yview)
vScroll.grid(row=0, column=1, sticky='ns')
cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)
## Frame in canvas
frm = Frame(cnv)
## This puts the frame in the canvas's scrollable zone
cnv.create_window(0, 0, window=frm, anchor='nw')
## Frame contents
for i in range(20):
    b = Button(frm, text='Button n#%s' % i, width=40)
    b.pack(side=TOP, padx=2, pady=2)
## Update display to get correct dimensions
frm.update_idletasks()
## Configure size of canvas's scrollable zone
cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
## Go!
root.mainloop()
