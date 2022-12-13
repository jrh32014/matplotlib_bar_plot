Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> data = [[30, 25, 50, 20],
    [40, 23,51,17],
    [35,22,45,19]]
>>> X = np.arange(4)
>>> fig = plt.figure()
>>> ax = fig.add_axes([0,0,1,1])
>>> ax.bar(X+0.00,data[0], color = 'b', width = 0.25)
<Container object of 4 artists>
>>> ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
<Container object of 4 artists>
>>> ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
<Container object of 4 artists>
>>> 
