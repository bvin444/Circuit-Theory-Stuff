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
            elif event == "YES_0":
                sg.popup("Capacitive Reactance = [2piFC]^-1. ('F' Denotes \n frequency and 'C' denotes Capacitance)."
                         "Dimensionally you have Hz * F ('F' denotes Ferads). But we know Hz = 1/s, and that one Ferad = Coulombs / Volt. \n"
                         "Therefore, we have coulombs / (s*V). However, Coulomb = A * s. Hence, we get As/s*V, which simplifies to A / V. \n"
                         "Looking back, though, at Capacitive Reactance we know that we need to invert A / V, and thus we get V / A. \n"
                         "According to Ohm's Law, V / A = R.")
            elif event == "YES_1":
                sg.popup("Inductive Reactance = [2piFL]. ('F' Denotes \n frequency and 'L' denotes Inductance). \n"
                         "Dimensionally you have Hz * H ('H' denotes Henry's). But we know Hz = 1/s, and that one Henry = V*s / A. \n"
                         "Therefore, we have Vs/A*(1/s). Multiplying this through results in V / A. According to Ohm's Law, V / A = R.")
            elif event in (sg.WIN_CLOSED, "EXIT"): break
        self.window.close()

    def create_window(self):

        layout = [
            [sg.Text("Please indicate what plot you would like: Inductive or Capacitive")],
            [sg.Button("Capacitive Reactance", key = "CAPACITIVE"), sg.Text("Breakdown of how Reactance in Ohms?"), sg.Button("Yes", key = "YES_0")],
            [sg.Button("Inductive Reactance", key = "INDUCTIVE"), sg.Text("Breakdown of how Reactance in Ohms?"), sg.Button("Yes", key = "YES_1")],
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
        Inductance = 1*(10**-3) # a 1uH Capacitor ... 'H' -> 'Henry'
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