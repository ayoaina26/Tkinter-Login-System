from tkinter import *

#Basic root screen
root = Tk()
root.title('Login Application')
e = Entry(root, text='Please enter your password here: ', width='50', bg='white', fg='red', borderwidth='5')
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
root.iconbitmap('c:/Python27/Dakirby309-Windows-8-Metro-Folders-OS-Windows-8-Metro.ico')

#functions that define what each button does

def button_enter():
    first_number = e.get()
    global password
    password = str(364609)
    e.delete(0, END)
    if first_number != password:
        print('Please try again')
    if first_number == password:
        print('Welcome!')

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

    

#Define buttons (What it says, how wide or tall it is, and what it is called by)
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=60, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=50, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=60, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=50, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=60, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=50, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_enter = Button(root, text='Enter', padx=40, pady=20, command=button_enter)
button_clear = Button(root, text='Clear', padx=49, pady=20, command=button_clear)


#Put Buttons on the scren
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_enter.grid(row=4, column=2)


root.mainloop()
