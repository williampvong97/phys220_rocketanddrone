import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

rocketdata = np.genfromtxt("rocketdata.txt")

accelx = rocketdata[:,0]
accely = rocketdata[:,1]
accelz = rocketdata[:,2]
accelmag = np.sqrt(accelx**2 + accely**2 + accelz**2)

gyrox = rocketdata[:,3] # in deg/s
gyroy = rocketdata[:,4]
gyroz = rocketdata[:,5]
gyromag = np.sqrt(gyrox**2 + gyroy**2 + gyroz**2)

biotx = rocketdata[:,6] # in gauss
bioty = rocketdata[:,7]
biotz = rocketdata[:,8]
biotmag = np.sqrt(biotx**2 + bioty**2 + biotz**2)

trange_ms = np.linspace(0, 1684.97165055*1000, 5960) # time units is ms, for 5960 points in python, from t = 0 to t = 5960pts * 100ms * 2.5
trange_s = np.linspace(0, 1684.97165055, 5960)

"""
f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_ms, accelmag, s = 0.1, color = "forestgreen")
ax.set_title("Accel. Mag.: full-view, our rocket, milliseconds", fontsize = 15)
plt.xlabel("time (ms)", fontsize = 15)
plt.ylabel("Accel. Mag. (g)", fontsize = 15)
plt.xticks(rotation = 59.4)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("amag_full_ms.svg", format = "svg", dpi = 1200) # uncomment to save graph in current working directory
plt.show()


f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_ms, accelmag, s = 8, color = "forestgreen")
plt.xlim(1677500, 1685500) 
ax.set_title("Accel. Mag.: launch-zoom, our rocket, milliseconds", fontsize = 15)
plt.xlabel("time (ms)", fontsize = 15)
plt.ylabel("Accel. Mag. (g)", fontsize = 15)
plt.xticks(rotation = 59.4)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("amag_zoom_ms.svg", format = "svg", dpi = 1200) # uncomment to save graph in current working directory
plt.show()


f, ax = plt.subplots()
ax.scatter(trange_s, accelmag, s = 0.1, color = "forestgreen")
ax.set_title("Accel. Mag.: full-view, our rocket, seconds", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("Accel. Mag. (g)", fontsize = 15)
ax.grid(True)
ax.minorticks_on()
#f.savefig("amag_full_s.svg", format = "svg", dpi = 1200) # uncomment to save graph in current working directory
plt.show()


f, ax = plt.subplots()
ax.scatter(trange_s, accelmag, s = 8, color = "forestgreen")
plt.xlim(1677.5, 1685.5) 
ax.set_title("Accel. Mag.: launch-zoom, our rocket, seconds", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("Accel. Mag. (g)", fontsize = 15)
ax.grid(True)
ax.minorticks_on()
#f.savefig("amag_zoom_s.svg", format = "svg", dpi = 1200) # uncomment to save graph in current working directory
plt.show()


f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_s, accelmag, s = 18, color = "indigo")
ax.plot(trange_s, accelmag, color = "indigo")
plt.xlim(1679.25, 1682) 
ax.set_title("Accel. Mag.: Comparison to E20W thrust-curve", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("Accel. Mag. (g)", fontsize = 15)
plt.xticks(rotation = 59.4)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("e20wmotorcomparison.svg", format = "svg", dpi = 1200) # uncomment to save graph in current working directory
plt.show()


# delay stuff, for k-calculations ---------------------------------------------

tcalculated = np.array([23.7, 47, 637.3, 137.8, 177.4, 592.5]) # from points
tmeasured = np.array([60.23, 119.94, 1800.03, 380.19, 480.27, 1680.65]) # actually measured
krange = np.zeros(6)

for i in range(0, 6):
    krange[i] = tmeasured[i] / tcalculated[i] # vert.axis is expecte, horiz.axis is observed

# now we'll form a plot of tmeasured vs. tcalculated, along with its leastsqsregression

tmeasured_vs_tcalcReshape = tcalculated.reshape(-1, 1)
tmeasured_vs_tcalcLm = linear_model.LinearRegression()
tmeasured_vs_tcalcModel = tmeasured_vs_tcalcLm.fit(tmeasured_vs_tcalcReshape, tmeasured)
tmeasured_vs_tcalcPredictions = tmeasured_vs_tcalcLm.predict(tmeasured_vs_tcalcReshape)

tmeasured_vs_tcalc_slope = tmeasured_vs_tcalcLm.coef_
tmeasured_vs_tcalc_yint = tmeasured_vs_tcalcLm.intercept_
tmeasured_vs_tcalc_score = tmeasured_vs_tcalcLm.score(tmeasured_vs_tcalcReshape, tmeasured)

print ("\nvalues for plot of tmeasured vs. tcalc:")
print (tmeasured_vs_tcalc_slope)
print (tmeasured_vs_tcalc_yint)
print (tmeasured_vs_tcalc_score)

def tmeasured_vs_tcalc(t): # t is your observed time, obtained through n(points)
    
    texpected = t * tmeasured_vs_tcalc_slope + tmeasured_vs_tcalc_yint
    
    return (texpected) # returns in seconds

print ("\nexpected timescale of rocket data, from plot of tmeasured vs. tcalc:")
print (tmeasured_vs_tcalc(596)) # seconds
print (tmeasured_vs_tcalc(596)/60) # minutes


f, ax = plt.subplots()
ax.scatter(tcalculated, tmeasured, color = "crimson")
ax.plot(tmeasured_vs_tcalcReshape, tmeasured_vs_tcalcPredictions, color = "skyblue")
ax.set_title(r"Measured time ($T_m$) vs. Calculated time ($\tau$) ", fontsize = 15)
plt.xlabel("Calculated time (s)", fontsize = 15)
plt.ylabel("Measured time (s)", fontsize = 15)
plt.text(310, 760, r"$T_m(\tau) = 2.8508\tau - 14.1345$", fontsize = 11)
plt.text(310, 610, r"$R^{2} = 0.9999$", fontsize = 11)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("tmeasured_vs_tcalc.svg", format = "svg", dpi = 1200)
plt.show()
"""

# gyro-------------------------------------------------------------------------

"""
f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_ms, gyromag, s = 0.5, color = "firebrick")
ax.set_title("Gyro. Mag.: full-view, our rocket, milliseconds", fontsize = 15)
plt.xlabel("time (ms)", fontsize = 15)
plt.ylabel("Gyro. Mag. (deg/s)", fontsize = 15)
plt.xticks(rotation = 59.4)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("gyromag_full_ms.svg", format = "svg", dpi = 1200)
plt.show()

f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_ms, gyromag, s = 8, color = "firebrick")
ax.set_title("Gyro. Mag.: zoom-launch, our rocket, milliseconds", fontsize = 15)
plt.xlabel("time (ms)", fontsize = 15)
plt.ylabel("Gyro. Mag. (deg/s)", fontsize = 15)
plt.xlim(1677500, 1685500) 
plt.xticks(rotation = 59.4)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("gyromag_zoom_ms.svg", format = "svg", dpi = 1200)
plt.show()


f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_s, gyromag, s = 0.5, color = "firebrick")
ax.set_title("Gyro. Mag.: full-view, our rocket, seconds", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("Gyro. Mag. (deg/s)", fontsize = 15)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("gyromag_full_s.svg", format = "svg", dpi = 1200)
plt.show()


f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_s, gyromag, s = 8, color = "firebrick")
ax.set_title("Gyro. Mag.: zoom-view, our rocket, seconds", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("Gyro. Mag. (deg/s)", fontsize = 15)
plt.xlim(1677.500, 1685.500) 
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("gyromag_zoom_s.svg", format = "svg", dpi = 1200)
plt.show()


# biot-------------------------------------------------------------------------

f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_ms, biotmag, s = 0.5, color = "cornflowerblue")
ax.set_title(r"$\overrightarrow{B}$-field Mag.: full-view, our rocket, milliseconds", fontsize = 15)
plt.xlabel("time (ms)", fontsize = 15)
plt.ylabel("Magnetic field mag. (gauss)", fontsize = 15)
plt.xticks(rotation = 59.4)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("biotmag_full_ms.svg", format = "svg", dpi = 1200)
plt.show()


f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_ms, biotmag, s = 8, color = "cornflowerblue")
ax.set_title(r"$\overrightarrow{B}$-field Mag.: zoom-view, our rocket, milliseconds", fontsize = 15)
plt.xlabel("time (ms)", fontsize = 15)
plt.ylabel("Magnetic field mag. (gauss)", fontsize = 15)
plt.xlim(1670500, 1686000) 
plt.ylim(0.2, 0.55)
plt.xticks(rotation = 59.4)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("biotmag_zoom_ms.svg", format = "svg", dpi = 1200)
plt.show()


f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_s, biotmag, s = 0.5, color = "cornflowerblue")
ax.set_title(r"$\overrightarrow{B}$-field Mag.: full-view, our rocket, seconds", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("Magnetic field mag. (gauss)", fontsize = 15)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("biotmag_full_s.svg", format = "svg", dpi = 1200)
plt.show()


f, ax = plt.subplots(figsize = (6, 4.5))
ax.scatter(trange_s, biotmag, s = 8, color = "cornflowerblue")
ax.set_title(r"$\overrightarrow{B}$-field Mag.: zoom-view, our rocket, seconds", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("Magnetic field mag. (gauss)", fontsize = 15)
plt.xlim(1670.500, 1686.000) 
plt.ylim(0.2, 0.55)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("biotmag_zoom_s.svg", format = "svg", dpi = 1200)
plt.show()
"""














































# scraps-----------------------------------------------------------------------

"""
# DANIEL DATA -----------------------------------------------------------------
danieldata = np.genfromtxt("daniel_CONTROL.txt")
accel_daniel = np.sqrt(danieldata[:,0]**2 + danieldata[:,1]**2 + danieldata[:,2]**2)
trange_nonadjusted = np.linspace(0, 100, 1000)
trange_adjusted = np.linspace(0, 250, 1000)

f, ax = plt.subplots(figsize = (6, 8))

adjusted = plt.subplot(211)
adjusted.scatter(trange_adjusted, accel_daniel, s = 0.2)
plt.title("Daniel, adjusted", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("accel mag (g)", fontsize = 15)
plt.grid(True)
plt.minorticks_on()
plt.tight_layout()

adjusted = plt.subplot(212)
adjusted.scatter(trange_adjusted, accel_daniel, s = 3)
plt.title("Daniel, adjusted, zoom", fontsize = 15)
plt.xlabel("time (s)", fontsize = 15)
plt.ylabel("accel mag (g)", fontsize = 15)
plt.xlim(10, 20)
plt.grid(True)
plt.minorticks_on()
plt.tight_layout()
plt.savefig("daniel.svg", format = "svg", dpi = 1200)

plt.show()
# DANIEL DATA END -------------------------------------------------------------
"""

"""
tmeasured_vs_krangeReshape = tmeasured.reshape(-1, 1)
tmeasured_vs_krangeLm = linear_model.LinearRegression()
tmeasured_vs_krangeModel = tmeasured_vs_krangeLm.fit(tmeasured_vs_krangeReshape, krange)
tmeasured_vs_krangePredictions = tmeasured_vs_krangeLm.predict(tmeasured_vs_krangeReshape)

tmeasured_vs_krange_slope = tmeasured_vs_krangeLm.coef_
tmeasured_vs_krange_yint = tmeasured_vs_krangeLm.intercept_
tmeasured_vs_krange_score = tmeasured_vs_krangeLm.score(tmeasured_vs_krangeReshape, krange)

print ("k plot values:")
print (tmeasured_vs_krange_slope)
print (tmeasured_vs_krange_yint)
print (tmeasured_vs_krange_score)


f, ax = plt.subplots()
ax.scatter(tmeasured, krange)
#ax.plot(tmeasured_vs_krangeReshape, tmeasured_vs_krangePredictions) 
ax.set_title(r"$k$-values vs. Calculated time", fontsize = 15)
plt.xlabel("Calculated time (s)", fontsize = 15)
plt.ylabel(r"$k$", fontsize = 15)
ax.grid(True)
ax.minorticks_on()
plt.tight_layout()
#f.savefig("k_vs_tcalc.svg", format = "svg", dpi = 1200)
plt.show()


def k_vs_tmeasured(t):
    k = tmeasured_vs_krange_slope*t + tmeasured_vs_krange_yint
    return (k) # returns the k-value when inputted a measured time

print ("\nk when inputted a measured time (time obtained from tmeasured vs. tcalc):")
k_vs_tmeasured_kval = k_vs_tmeasured(1682.59773529) # ~28min
print (k_vs_tmeasured_kval)
"""

"""
print ("\n%err and %diff between k from tmeasured vs. k, and k from tmeasured vs. tcalc:")
pererr1 = np.abs(k_vs_tmeasured_kval - tmeasured_vs_tcalc_slope)/k_vs_tmeasured_kval*100 # expected is k from k vs. tmeasured
pererr2 = np.abs(tmeasured_vs_tcalc_slope - k_vs_tmeasured_kval)/tmeasured_vs_tcalc_slope*100 # expected is k from tmeasured vs. tcalc
perdiff = np.abs(tmeasured_vs_tcalc_slope - k_vs_tmeasured_kval)/(tmeasured_vs_tcalc_slope + k_vs_tmeasured_kval)*2*100
print (pererr1)
print (pererr2) 
print (perdiff)
"""

"""
mylist = [1, 2, 3, 4, 5, 6, 7]
N = 3
cumsum, moving_aves = [0], []

for i, x in enumerate(mylist, 1):
    cumsum.append(cumsum[i-1] + x)
    if i>=N:
        moving_ave = (cumsum[i] - cumsum[i-N])/N
        #can do stuff with moving_ave here
        moving_aves.append(moving_ave)
"""

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








