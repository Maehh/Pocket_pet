import tkinter as tk
from functions import *
 

def new_animal_class():
    current_dog_label.config(text=unpack_animals(name_in))

dog_window = tk.Tk()
dog_window.title('Seu Cachorro')

dog_name_label = tk.Label(dog_window, text='Nome do Cachorro:')
current_dog_label = tk.Label(dog_window, text='')


name_in = tk.Entry(dog_window)

new_dog_btn = tk.Button(dog_window, text='NOVO DOG', command=new_animal_class)


name_in.grid(column=1, row=0)


dog_name_label.grid(column=0, row=0)


new_dog_btn.grid(column=1, row=3)
current_dog_label.grid(column=1, row=4)


dog_window.mainloop()