import PySimpleGUI as sg
import numpy as np
from typing import ClassVar


# from PIL import Image

# # Resize the image using Pillow
# image_path = "/Users/benjaminevincent/Documents/Software/Images/Inverting.png"
# image = Image.open(image_path)
# image = image.resize((200, 200))  # Adjust the size as needed
# resized_image_path = "/Users/benjaminevincent/Documents/Software/Images/resized_Inverter_image3.png"
# image.save(resized_image_path)

class Op_Amp:

    # class variables
    x_Pad : ClassVar[int] = 150
    y_Pad : ClassVar[int] = 0
    x_Frame : ClassVar[int] = 500
    y_frame : ClassVar[int] = 320
    def __init__(self):

        self.main()

    def main(self):

        self.window = self.create_main_window()
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "EXIT"): break
            if event == "SUBMIT_INVERTING":
                if self.input_validation("VIN_INVERTING", "RF_INVERTING", "RI_INVERTING", values = values): continue
                self.window["OUTPUT_INVERTING"].update(f"{round(-1*self.Numerical_Dictionary["VIN_INVERTING"]*self.Numerical_Dictionary["RF_INVERTING"]/self.Numerical_Dictionary["RI_INVERTING"], 2)}")
            if event == "SUBMIT_NON_INVERTING":
                if self.input_validation("VIN_NON_INVERTING", "RF_NON_INVERTING", "R2_NON_INVERTING", values = values): continue
                self.window["OUTPUT_NON_INVERTING"].update(f"{round((self.Numerical_Dictionary["VIN_NON_INVERTING"])*(1 + self.Numerical_Dictionary["RF_NON_INVERTING"])/self.Numerical_Dictionary["R2_NON_INVERTING"], 2)}")

    def create_main_window(self):

        Inverting_Operational_Amplifier_frame = sg.Frame("Inverting Op Amp", 
            [
                [sg.Image(filename="/Users/benjaminevincent/Documents/Software/Images/resized_Inverter_image3.png", pad = (Op_Amp.x_Pad, Op_Amp.y_Pad))],
                [sg.Text("Please enter your Feeback Resistance value:"), sg.Input("", key = "RF_INVERTING")],
                [sg.Text("Please enter your Input Resistance value:"), sg.Input("", key = "RI_INVERTING")],
                [sg.Text("Please enter your Input Voltage value:"), sg.Input("", key = "VIN_INVERTING")],
                [sg.Button("Submit", key = "SUBMIT_INVERTING"), sg.Text("Output (-(Rf/Ri)*(Vin))"), sg.Input("", key = "OUTPUT_INVERTING")],
            ], size = (Op_Amp.x_Frame, Op_Amp.y_frame))
        
        Non_Inverting_Operational_Amplifier_frame = sg.Frame("Non-Inverting Op Amp", 
            [
                [sg.Image(filename="/Users/benjaminevincent/Documents/Software/Images/resized_Non-Inverting_image3.png", pad = (150, 0))],
                [sg.Text("Please enter your Feeback Resistance value:"), sg.Input("", key = "RF_NON_INVERTING")],
                [sg.Text("Please enter your Resistance value:"), sg.Input("", key = "R2_NON_INVERTING")],
                [sg.Text("Please enter your Input Voltage value:"), sg.Input("", key = "VIN_NON_INVERTING")],
                [sg.Button("Submit", key = "SUBMIT_NON_INVERTING"), sg.Text("Output ((1 + (Rf/Ri))*(Vin))"), sg.Input("", key = "OUTPUT_NON_INVERTING")],
            ], size = (Op_Amp.x_Frame, Op_Amp.y_frame))
        
        layout =[[Inverting_Operational_Amplifier_frame, Non_Inverting_Operational_Amplifier_frame]]
        return sg.Window("Operational Amplifiers", layout, resizable = True)
    
    def input_validation(self, *args, values):
        for test_Input in args:
            if values[test_Input] == "":
                print("Hello")
                sg.popup("Input cannot be blank")
                return True
            try:
                float(values[test_Input])
            except:
                sg.popup("Please enter a numerical value")
                return True
        self.Numerical_Dictionary = {test_Input: (float(values[test_Input])) for test_Input in args} # dictionary comprehension
        print(self.Numerical_Dictionary)
        return False
    
if __name__ == "__main__":
    Executable = Op_Amp()