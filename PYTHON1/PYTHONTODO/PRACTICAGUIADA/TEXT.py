#https://www.youtube.com/watch?v=Qrmab6lSzU4

from tkinter import *
raiz = Tk()
my_text = Text(raiz, width= 40, height = 10, font=("Helvetica", 16))
my_text.pack(pady=20, padx=5)

#VACIAR EL TEXTO
def clear():
    my_text.delete(1.0, END)

#GRAB THE TEXT FROM THE TEXT BOX
def get_text():
    my_label.config(text=my_text.get(1.0, 4.0))

button_frame = Frame(raiz)
button_frame.pack()
clear_button = Button(button_frame, text="Clear Screen", command=clear)
clear_button.grid(row=0, column=0)

get_text_button = Button(button_frame, text="Get text", command = get_text)
get_text_button.grid(row=0, column=1, padx= 20)

my_label = Label(raiz, text='')
my_label.pack(pady=20)

raiz.mainloop()
