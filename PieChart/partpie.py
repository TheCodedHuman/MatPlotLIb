# Here we are fabricating the circular pie chart considering usage

import matplotlib.pyplot as plt

x = [25, 35, 20, 10, 10] 

plt.pie(x, radius=1.5, colors=['gold', 'springgreen', 'orangered', 'lightcoral', 'deepskyblue'])
cr= plt.Circle(xy=(0, 0), radius=1.2, facecolor='white')
plt.gca().add_artist(cr)
plt.show()