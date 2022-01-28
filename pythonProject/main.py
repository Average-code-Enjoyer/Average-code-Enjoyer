from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('NFT stealer')
root.geometry('300x300')
photo = ImageTk.PhotoImage(Image.open("nft.png"))
def lol():
    lable = Label(image=photo)
    lable.pack()

button = Button(root, text='click for nft', command=lol, fg='red')
button.pack()
root.mainloop()