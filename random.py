import tkinter as tk
from tkinter import *
import random

root=tk.Tk()
root.geometry('250x280')
root.minsize(200,100)
root.maxsize(250,280)
root.iconphoto(False, tk.PhotoImage(file='C:/Users/Lubaba.DESKTOP-AE9JJH8/OneDrive/Desktop/ico.png'))
root.configure(background='white')
root.title('Random Number Generator')

def random_num():
    first=first_one.get()
    first_int=int(first)
    second=second_one.get()
    second_int=int(second)
    gene_num=random.randint(first_int,second_int)
    result.insert(0,gene_num)
    

def clearTextInput():
    result.delete(0,END)
    
label = Label(root, text = "Random Number Generator  ", bd=3,width=25,bg='#fff', fg='#00008b',font=("Roboto",13) )
label.place(x=5,y=10)

    
label2 = Label(root, text = "Enter First Number", bd=5,width=25,bg='#fff', fg='black',font=("Roboto",11) )
label2.place(x=5,y=30)
first_one= Entry(root,bd=2,width=20)
first_one.place(x=60,y=60)
label2 = Label(root, text = "Enter Last Number", bd=5,width=25,bg='#fff', fg='black',font=("Roboto",11) )
label2.place(x=5,y=80)
second_one= Entry(root,bd=2,width=20)
second_one.place(x=60,y=110)

button_one=tk.Button(root,bd=2,width=15,text='Generate Number',bg='#add8e6',font=("Roboto",8),command=random_num)
button_one.place(x=20,y=140)
button_two=tk.Button(root,bd=2,width=15,text='Reset',bg='#add8e6',font=("Roboto",8),command=clearTextInput)
button_two.place(x=140,y=140)
label3 = Label(root, text = "Get Number        ", bd=5,width=25,bg='#fff',  fg='#00008b',font=("Roboto",15) )
label3.place(x=5,y=170)
result= Entry(root,bd=2,width=20)
result.place(x=60,y=200)
button_exit=tk.Button(root,bd=2,width=15,text='Quit',bg='white',fg='black',font=("Roboto",10),command=root.destroy)
button_exit.place(x=60,y=230)
root.mainloop()