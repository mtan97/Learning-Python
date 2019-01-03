#Michael Tan
#STAT 312R Homework #4 Chapter 6-101
#10/17/18

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#heights of two student groups (male, female)
fheight = [62, 64, 61, 67, 65, 68, 61, 65, 60, 65, 64, 63, 59, 68, 64, 66, 68, 69, 65, 67, 62, 66, 68, 67, 66, 65, 69, 65, 69, 65, 67, 67, 65, 63, 64, 67, 65]
mheight = [69, 67, 69, 70, 65, 68, 69, 70, 71, 69, 66, 67, 69, 75, 68, 67, 68, 69, 70, 71, 72, 68, 69, 69, 70, 71, 68, 72, 69, 69, 68, 69, 73, 70, 73, 68, 69, 71, 67, 68, 65, 68, 68, 69, 70, 74, 71, 69, 70, 69]
mu, std = norm.fit(fheight)
mu1, std1 = norm.fit(mheight)

# Plot the histograms on the same axes
plt.hist([fheight, mheight], bins = 10, density = True, alpha = 0.6, color = ['g', 'b'])

# Plot the PDFs 
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
m = norm.pdf(x, mu1, std1)
plt.plot(x, p, 'g', linewidth = 2)
plt.plot(x, m, 'b', linewidth = 2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title('Histograms of Female and Male Height')

plt.show()