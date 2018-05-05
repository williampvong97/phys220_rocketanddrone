import numpy as np
import matplotlib.pyplot as plt

rocketdata = np.genfromtxt("rocketdata.txt")

accelx = rocketdata[:,0]
accely = rocketdata[:,1]
accelz = rocketdata[:,2]

accelmag = np.sqrt(accelx**2 + accely**2 + accelz**2)
trange_ms = np.linspace(0, 1490000, 5960) # time units is ms, for 5960 points in python, from t = 0 to t = 5960pts * 100ms * 2.5
trange_s = np.linspace(0, 1490, 5960)


f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_ms, accelmag, s = 0.1)
ax.set_title("Full graph, our rocket, milliseconds", fontsize = 15)
plt.xlabel("time (ms)", fontsize = 15)
plt.ylabel("accel mag (g)", fontsize = 15)
plt.xticks(rotation = 59.4)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("amag_full_ms.svg", format = "svg", dpi = 1200) # uncomment to save graph in current working directory
plt.show()


f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_ms, accelmag, s = 8)
plt.xlim(1482500, 1490750) # (296100, 298100) or (593000, 596300) 
ax.set_title("Zoom graph, our rocket, milliseconds", fontsize = 15)
plt.xlabel("time (ms)", fontsize = 15)
plt.ylabel("accel mag (g)", fontsize = 15)
plt.xticks(rotation = 59.4)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("amag_zoom_ms.svg", format = "svg", dpi = 1200) # uncomment to save graph in current working directory
plt.show()


f, ax = plt.subplots()
ax.scatter(trange_s, accelmag, s = 0.1)
ax.set_title("Full graph, our rocket, seconds", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("accel mag (g)", fontsize = 15)
ax.grid(True)
ax.minorticks_on()
#f.savefig("amag_full_s.svg", format = "svg", dpi = 1200) # uncomment to save graph in current working directory
plt.show()


f, ax = plt.subplots()
ax.scatter(trange_s, accelmag, s = 8)
plt.xlim(1482.5, 1490.75) # (296100, 298100) or (593.0, 596.3)
ax.set_title("Zoom graph, our rocket, seconds", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("accel mag (g)", fontsize = 15)
ax.grid(True)
ax.minorticks_on()
#f.savefig("amag_zoom_s.svg", format = "svg", dpi = 1200) # uncomment to save graph in current working directory
plt.show()


f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_s, accelmag, s = 18, color = "indigo")
ax.plot(trange_s, accelmag, color = "indigo")
plt.xlim(1485.2, 1487.2) # (296100, 298100) or (593.0, 596.3), launch: 1485.2 to 1487.2
ax.set_title("Comparison to E20W curve", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("accel mag (g)", fontsize = 15)
plt.xticks(rotation = 59.4)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("e20wmotorcomparison.svg", format = "svg", dpi = 1200) # uncomment to save graph in current working directory
plt.show()






















"""
def bub1 (i):
    x = 0
    
    zoomaccelmag = np.zeros(i)
    tempsize = np.shape(accelmag)
    size = tempsize[0]
    i = np.abs(size - i)    

    for i in range (i, size):
        zoomaccelmag[x] = accelmag[i]
        x+= 1    

    return (zoomaccelmag)


try1 = bub1()
trange2 = np.linspace(298100 - 50 * 400 / 1000, 298100, 400)

f, ax = plt.subplots()
ax.scatter(trange2, try1)
plt.show()



def plotter(i):
    
    try1 = bub1(i)
    trange2 = np.linspace(298100 - 50*i/1000, 298100, i)
    
    f, ax = plt.subplots()
    plot = ax.scatter(trange2, try1, s = 0.01)    
    return (plot)


plotter(3960)
"""








