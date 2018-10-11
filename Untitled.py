
# coding: utf-8

# In[2]:


# %load sin_graph.py
import numpy as np
import matplotlib.pyplot as plt
# data
x = np.arange(0, 6, 0.1)
y = np.sin(x)

# plot graph
plt.plot(x, y)
plt.show()

