#---------------------------------------------------------------------------
# 4/18/17
# Author: Jacob Zahn
# Plotting CO2 and Solar Forcings over Earth's History
#---------------------------------------------------------------------------

# Those Sweet Imports
#---------------------------------------------------------------------------
from matplotlib import pyplot as plt
import CO2_Sol_globals as gl
import CO2_Sol_calc as calc


# Plotting dFSol, dF CO2, & dF over the last 400 My
#---------------------------------------------------------------------------
plt.figure(1)
plt.plot(gl.t,gl.dFCO2_fab,'g--',label="dFCO2")
plt.plot(gl.t,gl.dFSol,'r--',label="dFSol")
plt.plot(gl.t,gl.dF_fab,'b-',label="dF")
plt.xlabel('Time Since Formation of Earth [Mya]',fontsize=10)
plt.ylabel('Radiative Forcing [W/m2]',fontsize=10)
plt.title('Temporal Evolution of Climate Forcing with Estimated CO2 values',fontsize=16)
plt.axis([4300, 4700, -7, 13])
plt.grid(True)
plt.legend()
plt.ion()
plt.show()

plt.figure(2)
plt.plot(gl.t,gl.dFCO2_mea,'g--',label="dFCO2")
plt.plot(gl.t,gl.dFSol,'r--',label="dFSol")
plt.plot(gl.t,gl.dF_mea,'b-',label="dF")
plt.xlabel('Time Since Formation of Earth [Mya]',fontsize=10)
plt.ylabel('Radiative Forcing [W/m2]',fontsize=10)
plt.title('Temporal Evolution of Climate Forcing with Actual CO2 values',fontsize=16)
plt.axis([4300, 4700, -7, 13])
plt.grid(True)
plt.legend()
plt.ion()
plt.show()