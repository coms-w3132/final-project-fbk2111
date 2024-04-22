import tkinter as tk
from PIL import Image, ImageTk
import os
root = tk.Tk()
root.title('Crypto')
root.geometry('400x400')

def set_image():
    try:
        image_path = 'sodapdf-converted.gif'
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        img_lb.config(image=photo)
        img_lb.image = photo
    except Exception as e:
        print("Error loading image:", e)

img_lb = tk.Label(root)
img_lb.pack(pady=10)
set_image()

root.mainloop()




'''
external application
one button - for fetching market data
one button - to trade, we put the price, and the amount
one button - to analyze the data saved
their should be an api call where everything is put in a graph where it
shows the price fluctuation 
a button for an exit

'''