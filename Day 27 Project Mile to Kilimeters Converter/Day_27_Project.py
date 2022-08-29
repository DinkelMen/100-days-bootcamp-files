import tkinter
# from tkinter import *

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=400, height=200)

my_label = tkinter.Label(text='0', font=('Arial', 12, 'bold'))
my_label.grid(column=1, row=1)  # expand=True side='left'
my_label.config(padx=20, pady=20)

my_label1 = tkinter.Label(text='Miles', font=('Arial', 12, 'bold'))
my_label1.grid(column=2, row=0)
my_label1.config(padx=20, pady=20)

my_label2 = tkinter.Label(text='Km', font=('Arial', 12, 'bold'))
my_label2.grid(column=2, row=1)
my_label2.config(padx=20, pady=20)

my_label3 = tkinter.Label(text='Is equal to:', font=('Arial', 12, 'bold'))
my_label3.grid(column=0, row=1)
my_label3.config(padx=20, pady=20)


def button_click():
    text1 = input1.get()
    my_label['text'] = (float(text1) * 1.609)
    my_label.grid(column=1, row=1)

    # expand=True side='left'
    # print('Please stop!')


button = tkinter.Button(text='Calculate', command=button_click)
button.grid(row=2, column=1)
button.config(pady=20, padx=20)

# new_button = tkinter.Button(text='New Button', command=button_click)
# new_button.grid(row=0, column=2)

# Entry

input1 = tkinter.Entry()
input1.grid(row=0, column=1)


window.mainloop()


# def add(*args):
#     res = 0
#     for n in args:
#         res += n
#     return res
#
#
# a = add(1, 2, 3, 4, 10)
# print(a)
