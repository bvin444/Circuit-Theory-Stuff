import matplotlib.pyplot as plt
import math as math
import PySimpleGUI as sg
import matplotlib
# Time to add a Tag
# Attempt_2
matplotlib.use("TkAgg")  # Ensures compatibility with PySimpleGUI

class Reactance_Analysis:
    def __init__(self):
        pass
    def main(self):
        self.create_window()
        while True:
            event, values = self.window.read()
            if event == "CAPACITIVE":
                self.Capacitive_Reactance()
            elif event == "INDUCTIVE":
               self.Inductive_Reactance()
            elif event in (sg.WIN_CLOSED, "EXIT"): break
        self.window.close()

    def create_window(self):

        layout = [
            [sg.Text("Please indicate what plot you would like: Inductive or Capacitive")],
            [sg.Button("Capacitive Reactance", key = "CAPACITIVE")],
            [sg.Button("Inductive Reactance", key = "INDUCTIVE")],
            [sg.Button("Exit", key = "EXIT")]
        ]
        self.window = sg.Window("Reactance Analysis: R and L", layout, resizable = True)
        return self.window
        
    # Code to plot Capacitive Reactance
    # Remember one Ferad = 1 C / 1 V
    def Capacitive_Reactance(self):
        Capacitance = 1e-06 # a 1uF Capacitor
        Frequency_Array = []
        Capacitive_Reactance_Array = []
        for Frequency in range(100, 1000100, 100):
            Frequency_Array.append(math.log(Frequency, 10))
            Capacitive_Reactance_Array.append(
                round(float(1/(2*math.pi*Frequency*Capacitance)), 2))
        self.plot(Frequency_Array, Capacitive_Reactance_Array, "Capacitive")

    # Code to plot Capacitive Reactance

    def Inductive_Reactance(self):
        Inductance = 1*(10**-6) # a 1uH Capacitor ... 'H' -> 'Henry'
        Frequency_Array = []
        Inductive_Reactance_Array = []
        for Frequency in range(100, 1000100, 100):
            Frequency_Array.append(math.log(Frequency, 10))
            Inductive_Reactance_Array.append((float((2*math.pi*Frequency*Inductance))))
        self.plot(Frequency_Array, Inductive_Reactance_Array, "Inductive")

    def plot(self, x, y, name):
        fig, ax = plt.subplots() 
        ax.plot(x, y)
        ax.set_ylabel(f"{name} Reactance (Ohms)")
        ax.set_xlabel("Frequency (Hz) - Logarithmic Scale")
        ax.set_title(f"{name} Reactance (Ohms) vs. Frequency (Hz)")
        ax.grid()
        fig.canvas.manager.show()

if __name__ == "__main__":
    Executable = Reactance_Analysis()
    Executable.main()