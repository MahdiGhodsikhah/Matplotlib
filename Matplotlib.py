#%%
import matplotlib.pyplot as plt
import numpy as np

# Line Plot (simple)
x = np.linspace(0, 10, 1000)
# plt.plot(x, np.sin(x))
# plt.show()

# Object-Oriented API
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), 'r--', linewidth=2, label='sin(x)' , alpha=0.5)
ax.plot(x, np.cos(x), 'b-', linewidth=2, label='cos(x)' , alpha=0.5)
ax.set_title('sin(x) and cos(x)')
ax.set_yticks([-1, 0, 1])
ax.set_xticks([0, 5, 10])
ax.legend()
# ax.grid(True)
# ax.legend(loc='upper center')
plt.show()
# %%
