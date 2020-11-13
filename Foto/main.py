import io
import tkinter.messagebox as mb
from tkinter import *

import matplotlib.pyplot as plt
from PIL import Image

I = [4, 30, 79, 117, 143, 165, 175, 174, 170, 163, 160, 154, 152, 147, 144]
U = [0.2, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]

my_I = [4, 14.5, 23, 33, 40, 80, 100, 115, 135, 145, 155, 165, 170, 175, 177,
        175, 170, 163, 152, 144]
my_U = [0.2, 0.32, 0.4, 0.52, 0.68, 1, 1.28, 1.48, 1.8, 2, 2.2, 2.56, 2.72, 3,
        3.2, 3.6, 4, 4.72, 6, 7]
U_enters = []
I_enters = []


def add_enter_place():
    U_enters.append(Entry(input_U))
    I_enters.append(Entry(input_I, state=DISABLED))
    U_enters[-1].grid(row=len(U_enters), column=0)
    I_enters[-1].grid(row=len(U_enters), column=0)


def delete_enter_place():
    if len(U_enters) > 1:
        U_enters[-1].destroy()
        I_enters[-1].destroy()
        U_enters.pop()
        I_enters.pop()


def calculate():
    class empty_place(BaseException):
        pass

    class out_of_range(BaseException):
        pass
    U_input = []
    I_disp = []
    try:
        for value_U in U_enters:
            get = value_U.get()
            if not get:
                raise empty_place

            U_input.append(float(get))

        if all(0.2 <= item <= 7 for item in U_input):

            for value_U in U_input:
                I_disp.append(calc(value_U))

            for value_I, value_I_disp in zip(I_enters, I_disp):
                value_I.configure(state=NORMAL)
                value_I.delete(0, END)
                value_I.insert(0, str(value_I_disp))
                value_I.configure(state=DISABLED)
            my_vach(U_input, I_disp)
        else:
            raise out_of_range

    except ValueError:
        mb.showerror(title='Warning',
                     message='Invalid format')
    except empty_place:
        mb.showerror(title='Warning',
                     message='Empty place')
    except out_of_range:
        mb.showerror(title='Warning',
                     message='Out of range')


def calc(a):  # функция вычисляет I(U)
    search = 0
    while a > U[search]:
        search += 1
    return (a - U[search - 1]) * ((I[search] - I[search - 1]) / (U[search] - U[search - 1])) + I[search - 1]


def my_vach(U=my_U, I=my_I):
    plt.figure()
    plt.plot(U, I)
    plt.title("Current–voltage characteristic Gunn's diod")
    plt.ylabel('I,µA')
    plt.xlabel('U,V')
    plt.grid(True)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    im = Image.open(buf)
    im.show()
    buf.close()

root = Tk()
root.title('Gunn effect')
root.geometry('400x250')

input_data = Frame(root)
Label(input_data, text='Data').grid(row=0, column=0,
                                    columnspan=2,
                                    sticky=W+E)
input_U = Frame(input_data)
input_I = Frame(input_data)
Label(input_U, text='U, V').grid(row=0, column=0,
                                 sticky=W+E)

Label(input_I, text='I, µA').grid(row=0, column=0,
                                  sticky=W+E)

add_enter_place()
input_U.grid(row=1, column=0)
input_I.grid(row=1, column=1)

tools = Frame(root)

Button(tools, text='Add data', command=add_enter_place).grid(row=0,
                                                             column=3,
                                                             sticky=W+E)
Button(tools, text='Delete data', command=delete_enter_place).grid(row=1,
                                                                   column=3,
                                                                   sticky=W+E)
Button(tools, text="Calculate", command=calculate).grid(row=2,
                                                        column=3,
                                                        sticky=W+E)
Button(tools, text="ВАХ диода", command=my_vach).grid(row=3,
                                                      column=3,
                                                      sticky=W+E)

input_data.pack(side=LEFT, expand=1, anchor=NW)
tools.pack(side=LEFT, expand=1, fill=BOTH, anchor=NE)


root.mainloop()
