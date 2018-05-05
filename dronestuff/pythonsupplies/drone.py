import numpy as np
import matplotlib.pyplot as plt

dronedata = np.genfromtxt("dronedata.txt")

accelx = dronedata[:,0]
accely = dronedata[:,1]
accelz = dronedata[:,2]


accelmag = np.sqrt(accelx**2 + accely**2 + accelz**2)
trange_ms = np.linspace(0, 175750, 703) # 703 pts, 1pt per 250ms => 703 * 250 = 175750ms total
trange_s = np.linspace(0, 175.75, 703)












































































