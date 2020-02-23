#!/usr/bin/env python
import control as ct
# from control.rlocus import root_locus
import numpy as np
import matplotlib.pyplot as plt
import sys

# create a transfer function
gs_tf=ct.tf([1,10,5],[1,0,0])

kvect=np.linspace(0,1.5,1000)

rlist,klist=ct.root_locus(gs_tf,kvect=None,plot=True)
plt.title("None")
plt.show()

# root locus plot
rlist,klist=ct.root_locus(gs_tf,kvect=kvect,plot=True)
plt.title("kvect")
plt.legend(loc='best')
plt.show()

# calculate the root locus for matplotlib plot
rlist,klist=ct.root_locus(gs_tf,kvect=kvect,Plot=False)

# matplotlib plot
plt.title("matplotlib")
for index in range(len(rlist[0])):
	plt.plot(np.real(rlist[:,index]),np.imag(rlist[:,index]))
plt.show()
