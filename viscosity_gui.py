from tkinter import *
import math
import sys
import os
import numpy as np

root = Tk()
root.title("Viscosity GUI")
root.geometry("300x200")


def validate():
    try:
        int(entry.get())
        species = int(entry.get())
        button.config(state="disabled", bg="grey")
        button.update()
        c = Calculations_Page(species)
    except ValueError:
        validation_text.config(text="Enter a Valid Integer")


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


class Calculations_Page:
    def __init__(self, num):
        top = Toplevel()

        def calculation(self, x, M, mu, num):
            w, h = num, num
            phi = [[0 for x in range(w)] for y in range(h)]
            xphi = [[0 for x in range(w)] for y in range(h)]
            denominator = [0] * num
            numerator = [0] * num
            viscosity = [0] * num
            for i in range(0, num):
                for c in range(0, num):
                    phi[i][c] = get_phi(
                        mu[i].get(), mu[c].get(), M[i].get(), M[c].get()
                    )

            for a in range(0, num):
                for b in range(0, num):
                    xphi[a][b] = float(x[b].get()) * phi[a][b]
            # print(xphi)
            for i in range(0, num):
                xphi = np.array(xphi)
                xphi = xphi.astype(float)
                denominator[i] = sum(xphi[i])

            for i in range(0, num):
                numerator[i] = float(x[i].get()) * float(mu[i].get())

            for i in range(0, num):
                viscosity[i] = numerator[i] / denominator[i]
            # print("\n")
            # print("Viscosity [g/cm s]: " + str(round(sum(viscosity), 13)))
            viscosity_result.config(
                text="viscosity: " + str(round(sum(viscosity), 13)) + " g/cm s"
            )

        def get_phi(mui, muj, mi, mj):
            if mui == muj:
                return 1
            phi = (
                (1 / math.sqrt(8))
                * ((1 + (float(mi) / float(mj))) ** (-0.5))
                * (
                    1
                    + ((float(mui) / float(muj)) ** 0.5)
                    * ((float(mj) / float(mi)) ** 0.25)
                )
                ** 2
            )
            return phi

        labels = [
            "Enter Mole Fractions: ",
            "Enter Molecular Weights: ",
            "Enter Viscosities in g/cm s: ",
        ]
        w, h = num, 3
        entries = [[0 for x in range(w)] for y in range(h)]
        entrytext = [[StringVar() for x in range(w)] for y in range(h)]
        for r in range(0, 3):
            for i in range(0, num):
                entries[r][i] = Entry(top, textvariable=entrytext[r][i])
                entries[r][i].grid(column=i + 1, row=r)
        for i in range(0, 3):
            label = Label(top, text=labels[i])
            label.grid(column=0, row=i)

        calculate = Button(
            top,
            text="Calculate",
            command=lambda: calculation(
                self, entrytext[0], entrytext[1], entrytext[2], num
            ),
        )
        row, column = top.grid_size()
        calculate.grid(column=0, row=row, sticky="w")
        restart_btn = Button(top, text="exit", command=restart_program)
        restart_btn.grid(column=1, row=row, sticky="w")
        viscosity_result = Label(top, text="Viscosity: ")
        viscosity_result.grid(pady=10, sticky="w", row=row, column=2)


label = Label(root, text="How many species are in this gas mixture?")
label.pack(pady=20, padx=30)

entry = Entry(root, width="5")
entry.pack(pady=5)

button = Button(
    root, width="15", text="Continue", fg="white", bg="green", command=validate
)
button.pack(pady=5)

validation_text = Label(root, text="", fg="red")
validation_text.pack(pady="5")

credits = Label(root, text="RRPL", fg="green")
credits.pack(pady="5")


root.mainloop()

