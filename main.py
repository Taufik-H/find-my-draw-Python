from PIL import Image, ImageTk, ImageDraw
import tkinter as tk
import numpy as np
import Ai

model =Ai.load_ai()

window =tk.Tk()

img = Image.new(mode="1", size=(500, 500), color=0 )
tkimage = ImageTk.PhotoImage(img)
canvas = tk.Label(window, image=tkimage)
canvas.pack()

titik_akhir = (0, 0)
draw = ImageDraw.Draw(img)
prediction = tk.StringVar()
label = tk.Label(window, textvariable=prediction)

def draw_image(event):
    global titik_akhir,tkimage, prediction
    titik_gerak = (event.x, event.y)
    draw.line([titik_akhir, titik_gerak], fill=255, width=30)
    titik_akhir = titik_gerak
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()
    img_board =img.resize((50, 50))
    img_board = np.array(img_board)
    img_board = img_board.flatten()
    output = model.predict([img_board])
    if(output[0] == 0):
        prediction.set("SATU (1)")
    elif(output[0] == 1):
        prediction.set("DUA (2)")
    else:
        prediction.set("TIGA (3)")
    label.pack()
def start_draw(event):

    global titik_akhir
    titik_akhir =(event.x, event.y)

def hapus_line(event):
    global tkimage, img, draw
    img = Image.new(mode="1", size=(500, 500), color=0 )
    draw = ImageDraw.Draw(img)
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()

satu = 0
dua = 0
tiga =0

def save_image(event):
    global satu, dua, tiga
    img_board = img.resize((50,50))

    if(event.char == "q"):
        img_board.save(f"satu/{satu}.png")
        satu += 1
    elif (event.char == "w"):
        img_board.save(f"dua/{dua}.png")
        dua += 1
    elif (event.char == "e"):
        img_board.save(f"tiga/{tiga}.png")
        tiga += 1
        


window.bind("<B1-Motion>", draw_image)
window.bind("<ButtonPress-1>", start_draw)
window.bind("<ButtonPress-3>", hapus_line)
window.bind("<Key>", save_image)


label.pack()
window.mainloop()

