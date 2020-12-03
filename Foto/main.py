import io
import tkinter.messagebox as mb
from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
from PIL import Image
angle_to_length = {
    500: 3980, 550: 4000, 600: 4020, 650: 4040, 700: 4070, 750: 4100,
    800: 4120, 850: 4150, 900: 4190, 950: 4220,
    1000: 4260, 1050: 4280, 1100: 4300, 1150: 4340, 1200: 4380, 1250: 4420,
    1300: 4450, 1350: 4480, 1400: 4520, 1450: 4560, 1500: 4600, 1550: 4640,
    1600: 4680, 1650: 4720, 1700: 4770, 1750: 4820, 1800: 4870, 1850: 4930,
    1900: 4980, 1950: 5040, 2000: 5100, 2050: 5180, 2100: 5260, 2150: 5330,
    2200: 5410, 2250: 5490, 2300: 5570, 2350: 5650, 2400: 5730, 2450: 5800,
    2500: 5920, 2550: 6020, 2600: 6130, 2650: 6250, 2700: 6370, 2750: 6500,
    2800: 6620, 2850: 6750, 2900: 6890, 2950: 7040, 3000: 7200, 3050: 7400,
    3100: 7630, 3150: 7900, 3200: 8200, 3250: 8520, 3300: 8800,
}

length_to_current = {
    0.35: 0.013, 0.36: 0.016, 0.37: 0.021, 0.38: 0.025, 0.39: 0.03,
    0.398: 0.038, 0.4: 0.039, 0.402: 0.041, 0.404: 0.042, 0.407: 0.045,
    0.41: 0.047, 0.412: 0.048, 0.415: 0.051, 0.419: 0.055, 0.422: 0.058,
    0.426: 0.061, 0.428: 0.063, 0.43: 0.066, 0.434: 0.069, 0.438: 0.075,
    0.442: 0.08, 0.445: 0.083, 0.448: 0.088, 0.452: 0.09, 0.456: 0.095,
    0.46: 0.103, 0.464: 0.108, 0.468: 0.115, 0.472: 0.119, 0.477: 0.127,
    0.482: 0.133, 0.487: 0.142, 0.493: 0.151, 0.498: 0.16, 0.504: 0.171,
    0.51: 0.182, 0.518: 0.199, 0.526: 0.213, 0.533: 0.225, 0.541: 0.242,
    0.549: 0.258, 0.557: 0.276, 0.565: 0.29, 0.573: 0.306, 0.58: 0.322,
    0.592: 0.347, 0.602: 0.367, 0.613: 0.39, 0.625: 0.415, 0.637: 0.44,
    0.65: 0.466, 0.662: 0.489, 0.675: 0.513, 0.689: 0.538, 0.704: 0.567,
    0.72: 0.595, 0.74: 0.625, 0.763: 0.657, 0.79: 0.692, 0.82: 0.723,
    0.852: 0.748, 0.88: 0.766, 0.9: 0.774,
}

angle_enters = []
voltage_enters = []

voltage1_enters = []
slit1_enters = []


wavelengthA_enters = []
wavelengthM_enters = []
quantum_energy_enters = []
input_U_enters = []
relative_I_enters = []
eff_U_enters = []
G_enters = []



def add_enter_place_to_container():

    angle_enters.append(ttk.Entry(angle, width=8))
    voltage_enters.append(ttk.Entry(voltage, width=8))

    angle_enters[-1].grid(row=len(angle_enters), column=0)
    voltage_enters[-1].grid(row=len(angle_enters), column=0)


def add_enter_place_to_container1():
    voltage1_enters.append(ttk.Entry(voltage1, width=8))
    slit1_enters.append(ttk.Entry(slit1, width=8))

    voltage1_enters[-1].grid(row=len(voltage1_enters), column=0)
    slit1_enters[-1].grid(row=len(slit1_enters), column=0)


def delete_enter_place_in_container():
    if len(angle_enters) > 1:
        angle_enters[-1].destroy()
        voltage_enters[-1].destroy()
        angle_enters.pop()
        voltage_enters.pop()


def delete_enter_place_in_container1():
    if len(voltage1_enters) > 1:
        voltage1_enters[-1].destroy()
        slit1_enters[-1].destroy()
        voltage1_enters.pop()
        slit1_enters.pop()


def calculate():
    angles = [angle.get() for angle in angle_enters]
    lengthsA = []
    lengthsM = []
    energies = []
    voltages = [volt.get() for volt in voltage_enters]
    relatives_I = []
    effective_U = []
    delta_G = []


    class empty_place(BaseException):
        pass


    maintable = Tk()
    maintable.geometry("650x500")
    container = ttk.Frame(maintable)
    container.pack(side=LEFT)
    canvas = Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical",
                              command=canvas.yview)

    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    angle_frame = ttk.Frame(scrollable_frame)
    wavelengthA = ttk.Frame(scrollable_frame)
    wavelengthM = ttk.Frame(scrollable_frame)
    quantum_energy = ttk.Frame(scrollable_frame)
    input_U = ttk.Frame(scrollable_frame)
    relative_I = ttk.Frame(scrollable_frame)
    eff_U = ttk.Frame(scrollable_frame)
    G = ttk.Frame(scrollable_frame)

    Label(angle_frame, text='Деления').grid(row=0, column=0,
                                      sticky=W + E)
    Label(wavelengthA, text='Длина волны L,Å').grid(row=0, column=0,
                                                    sticky=W + E)
    Label(wavelengthM, text='Длина волны L,мкм').grid(row=0, column=0,
                                                      sticky=W + E)
    Label(quantum_energy, text='Энергия квантов hv, эВ').grid(row=0, column=0,
                                                              sticky=W + E)
    Label(input_U, text='U, B').grid(row=0, column=0,
                                     sticky=W + E)
    Label(relative_I, text='I, отн. Ед.').grid(row=0, column=0,
                                               sticky=W + E)
    Label(eff_U, text='Uэфф, B').grid(row=0, column=0,
                                      sticky=W + E)
    Label(G, text='ΔG, отн. Ед.').grid(row=0, column=0,
                                       sticky=W + E)

    def calc(a, where):
        temp_min = 100000
        if where.get(a, 0):
            return where[a]
        for value in where.keys():
            if abs(value-a) > temp_min:
                return where[value]
            else:
                temp_min = abs(value-a)

    def fill_table():

        for angle, volt in zip(angles, voltages):
            length = calc(int(angle), angle_to_length)
            lengthsA.append(length)
            lengthsM.append(length / 10**4)
            energies.append(round(1.24 / lengthsA[-1], 4))
            I = calc(lengthsM[-1], length_to_current)
            relatives_I.append(I)
            effective_U.append(round(float(volt) / relatives_I[-1], 5))

            Label(angle_frame, text=angle).grid(row=len(lengthsA),
                                                column=0,
                                                sticky=W + E)
            Label(wavelengthA, text=str(length)).grid(row=len(lengthsA),
                                                      column=0,
                                                      sticky=W + E)
            Label(wavelengthM,
                  text=str(lengthsM[-1])
                  ).grid(row=len(lengthsA), column=0, sticky=W + E)
            Label(quantum_energy,
                  text=str(energies[-1])).grid(row=len(lengthsA),
                                               column=0,
                                               sticky=W + E)
            Label(input_U, text=volt).grid(row=len(lengthsA),
                                           column=0,
                                           sticky=W + E)
            Label(relative_I,
                  text=str(relatives_I[-1])).grid(row=len(lengthsA),
                                                  column=0,
                                                  sticky=W + E)
            Label(eff_U,
                  text=str(effective_U[-1])).grid(row=len(lengthsA),
                                                  column=0,
                                                  sticky=W + E)



        max_U = max(effective_U)
        for U in effective_U:
            delta_G.append(round(U / max_U, 6))
            Label(G, text=str(delta_G[-1])).grid(row=len(delta_G), column=0,
                                                 sticky=W + E)

    try:
        fill_table()
    except ValueError:
        mb.showerror(title='Warning',
                     message='Invalid format')
    except empty_place:
        mb.showerror(title='Warning',
                     message='Empty place')


    angle_frame.grid(row=0, column=0)
    wavelengthA.grid(row=0, column=1)
    wavelengthM.grid(row=0, column=2)
    quantum_energy.grid(row=0, column=3)
    input_U.grid(row=0, column=4)
    relative_I.grid(row=0, column=5)
    eff_U.grid(row=0, column=6)
    G.grid(row=0, column=7)


    def create_file():
        pass

    Button(scrollable_frame,
           text="Create file",
           command=create_file).grid(row=len(lengthsA)+1,
                                     column=3,
                                     columnspan=2,
                                     sticky=W + E)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", expand=True, fill="both")
    container.pack(side=LEFT, expand=True, fill="both")
    root.mainloop()






root = Tk()
root.geometry('1000x500')
container = ttk.Frame(root)

canvas = Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)

scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)


Label(scrollable_frame, text='Data').grid(row=0, column=0,
                                          columnspan=3,
                                          sticky=W + E)


angle = ttk.Frame(scrollable_frame)
voltage = ttk.Frame(scrollable_frame)

Label(angle, text='Деления').grid(row=0, column=0,
                                  sticky=W + E)
Label(voltage, text='U, В').grid(row=0, column=0,
                                 sticky=W + E)


add_enter_place_to_container()





angle.grid(row=1, column=0)
voltage.grid(row=1, column=1)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left")






container1 = ttk.Frame(root)
container1.pack(side=LEFT)
canvas1 = Canvas(container1)
scrollbar1 = ttk.Scrollbar(container1,
                           orient="vertical",
                           command=canvas1.yview)
scrollable_frame1 = ttk.Frame(canvas1)

scrollable_frame1.bind(
    "<Configure>",
    lambda e: canvas1.configure(
        scrollregion=canvas1.bbox("all")
    )
)

canvas1.create_window((0, 0), window=scrollable_frame1, anchor="nw")


Label(scrollable_frame1, text='Data 2').grid(row=0, column=0,
                                             columnspan=3,
                                             sticky=W + E)

voltage1 = ttk.Frame(scrollable_frame1)
slit1 = ttk.Frame(scrollable_frame1)

Label(voltage1, text='U, V').grid(row=0, column=0,
                                  sticky=W + E)
Label(slit1, text='d, 10^(-2) m').grid(row=0, column=0,
                                       sticky=W + E)


add_enter_place_to_container1()



voltage1.grid(row=1, column=0)
slit1.grid(row=1, column=1)

canvas1.configure(yscrollcommand=scrollbar1.set)
canvas1.pack(side="left")
scrollbar1.pack(side="right", fill="y")














tools = Frame(root)

Label(tools, text='Input U (0.2-7 V)').grid(row=0,
                                            column=0,
                                            sticky=W + E)

Button(tools,
       text='Add data',
       command=add_enter_place_to_container).grid(row=1,
                                                  column=0,
                                                  sticky=W + E)
Button(tools,
       text='Delete data',
       command=delete_enter_place_in_container).grid(row=1,
                                                     column=1,
                                                     sticky=W+E)

Button(tools,
       text='Add data 2',
       command=add_enter_place_to_container1).grid(row=2,
                                                   column=0,
                                                   sticky=W + E)
Button(tools,
       text='Delete data 2',
       command=delete_enter_place_in_container1).grid(row=2,
                                                      column=1,
                                                      sticky=W+E)
Button(tools, text="Calculate", command=calculate).grid(row=3,
                                                        column=0,
                                                        columnspan=2,
                                                        sticky=W + E)


container.pack(side=LEFT)
tools.pack(side=RIGHT)

root.mainloop()

