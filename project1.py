import numbers
import sys
from tkinter import *



def MultiTable():
	number = int(EnterTable.get())
	for j in range(1,number):
	  for i in range(1,11):print((j+1) , "X", i, "=", i*(j+1))
Table = Tk()		
Table.geometry('800x250+700+200')
Table.title('Multiplication Table')
EnterTable = StringVar()

label1 = Label(Table, text='MULTIPLICATION TABLES-BY lokesh:',
			font=30, fg='brown').grid(row=0, column=5)
label1 = Label(Table, text='					 ').grid(row=2, column=6)
entry = Entry(Table, textvariable=EnterTable,
			justify='center').grid(row=3, column=6)
label1 = Label(Table, text='					 ').grid(row=4, column=6)
button1 = Button(Table, text="CLICK", fg="green",
				command=MultiTable).grid(row=5, column=6)
label1 = Label(Table, text='					 ').grid(row=6, column=6)
EXIT = Button(Table, text="Quit", fg="red",
			command=Table.destroy).grid(row=7, column=6)

Table.mainloop()
