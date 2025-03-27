# Code to calculate output voltage from a voltage-divider configuration
# Test_push
import PySimpleGUI as sg
from typing import ClassVar

class VoltageDivider:

    x_Frame : ClassVar[int] = 250
    y_Frame : ClassVar[int] = 200
    def __init__(self):

        self.main()
    
    def main(self):

        self.window = self.create_main_window()

        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "EXIT"): break
            elif event == "SUBMIT":
                if self.input_Validation("R_1", "R_2", "V_IN", values = values): continue
                self.window["OUTPUT"].update(f"{round(self.numerical_Dictionary["V_IN"] * self.numerical_Dictionary["R_2"]/(self.numerical_Dictionary["R_1"] + self.numerical_Dictionary["R_2"]), 2)}")

    def create_main_window(self):

        voltage_Divider_frame = sg.Frame("Voltage Divider", 
            [
                [sg.Text("Please enter a value for R_1"), sg.Input("", key = "R_1")],
                [sg.Text("Please enter a value for R_2"), sg.Input("", key = "R_2")],
                [sg.Text("Please enter your input voltage"), sg.Input("", key = "V_IN")],
                [sg.Button("Submit", key = "SUBMIT"), sg.Text("Output"), sg.Input("", key = "OUTPUT", size = (5, 10)), sg.Text("V")],
                 [sg.Button("Exit", key = "EXIT")]
            ], size = (VoltageDivider.x_Frame, VoltageDivider.y_Frame))
        
        layout = [[voltage_Divider_frame]]
        return sg.Window("Voltage Divider Calculator", layout, resizable = True)
    
    def input_Validation(self, *args, values):

        for test_Input in args:
            print(values[test_Input])
            if values[test_Input] == '':
                print("Hello, Benjamin")
                sg.popup("Input cannot be blank!")
                return True
            try:
                float(values[test_Input])
            except:
                sg.popup("Input must be a numeric.")
                return True
            
        self.numerical_Dictionary = {key : float(values[key]) for key in args}
        return False
    
if __name__ ==  "__main__":

    Executable = VoltageDivider()
        