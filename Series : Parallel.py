## Code to calculate Series and Parallel Resistance
## Code to calculate Series and Parallel Capacitance



import PySimpleGUI as sg




layout = [
    [sg.Button("Capacitance", key = "CAP"), sg.Button("Resistance", key = "RES")],
    [sg.Button("Parallel")]
    [sg.Text("How many components are you wish to calculate?"), sg.Input("", key = "NUM")]
    [sg.Text("Equivalent "), sg.Input("", key = "NUM")]
]

window = sg.Window("Parallel / Series Calculator", layout, resizable = True)

while True:
    event, values = window.read()
    if event == "CAP":
        new_window = (sg.Button("Parallel", key = "PAR"), sg.Button("Series", key = "SER"))
        event, values = window.read()

        Equivalent
        Number = values["NUM"]
        for i in range(1, Number + 1):
            Equivalent = Equivalent

