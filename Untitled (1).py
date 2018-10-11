
# coding: utf-8

# In[14]:



import numpy as np
import matplotlib.pyplot as plt

class iamaking:
    def __init__(self,x):
        self.x = np.arange(0, 6, 0.1)
    def sin(self):
        
        y = np.sin(self.x)
        plt.plot(self.x,y)
        plt.show()
    def cos(self):
        y = np.cos(self.x)
        plt.plot(self.x,y)
        plt.show()


# In[15]:



m = iamaking("")
m.sin()
m.cos()


# In[ ]:




