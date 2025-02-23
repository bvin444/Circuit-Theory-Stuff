import matplotlib.pyplot as plt
import math
import os

V_s = 5
R = 100 # resistance in our circuit
C = 0.000001 # capacitance in our circuit
e = math.e
ResistorVoltage = []
CapacitorVoltage = []
t = []
for n in range(1, 501):
    time = n / 1000000
    t.append(time)
    CapacitorVoltage.append(round(V_s*(1  - (e ** (-time/(R * C)))), 2))
    ResistorVoltage.append(round(V_s*(e ** (-time/(R * C))), 2))
    if time == 0.0001:
        x_63 = time
        y_63 = round(V_s*(e ** (-time/(R * C))), 2)
        
plt.plot(t, ResistorVoltage, label = 'High-Pass Filter Output')
plt.plot(t, CapacitorVoltage, label = 'Low-Pass Filter Output')
plt.annotate('One time-constant', xy = (x_63, y_63+0.7), xytext = (x_63 + 0.00004, y_63 - 0.5), arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.xlabel("Time")
plt.ylabel("Resistor Voltage")
plt.vlines(x_63, 0, 5, linestyles = '--', color = 'black')
plt.title("RC LP & HP Filter Curves: Time vs. Voltage")
plt.legend()
plt.show()