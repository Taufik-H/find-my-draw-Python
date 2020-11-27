import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

window =tk.Tk()

img = Image.new(mode="1", size=(500, 500), color=255 )
tkimage = ImageTk.PhotoImage(img)
canvas = tk.Label(window, image=tkimage)
canvas.pack()
titik_akhir = (0, 0)
draw = ImageDraw.Draw(img)


def draw_image(event):
    global titik_akhir,tkimage
    titik_gerak = (event.x, event.y)
    draw.line([titik_akhir, titik_gerak], fill=0, width=1)
    titik_akhir = titik_gerak
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()

def start_draw(event):

    global titik_akhir
    titik_akhir =(event.x, event.y)

def hapus_line(event):
    global tkimage, img, draw
    img = Image.new(mode="1", size=(500, 500), color=255 )
    draw = ImageDraw.Draw(img)
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()

window.bind("<B1-Motion>", draw_image)
window.bind("<ButtonPress-1>", start_draw)
window.bind("<ButtonPress-3>", hapus_line)
window.mainloop()

