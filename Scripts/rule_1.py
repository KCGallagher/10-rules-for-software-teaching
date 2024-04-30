# Quick vs Sustainable Code Development

import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()
 
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(1, 1, 1)
 
x = np.linspace(0, 1.2, 100)
y1 = np.power(x, 3) + np.power(x, 1.5)
y2 = np.power(x/2, 1/2)
 
ax.set_xticks([])
ax.set_yticks([])
 
ax.plot(x, y1, label='Sustainable', ls='-', color='green')
ax.plot(x, y2, label='Quick', ls='--', color='red')
 
ax.legend(title='Coding Style', loc='upper left')
ax.set_xlabel('Time Spent')
ax.set_ylabel('Results')
plt.savefig('Figures/rule_1_sustainable_vs_quick.png', dpi=600, bbox_inches='tight')