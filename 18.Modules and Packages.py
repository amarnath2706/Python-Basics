#!/usr/bin/env python
# coding: utf-8

# ## Modules and Packages
# Modules in Python are simply Python files with the .py extension, which implement a set of functions. Modules are imported from other modules using the import command. Before you go ahead and import modules, check out the full list of built-in modules in the Python Standard library.
# 
# When a module is loaded into a running script for the first time, it is initialized by executing the code in the module once. If another module in your code imports the same module again, it will not be loaded twice but once only - so local variables inside the module act as a "singleton" - they are initialized only once.
# 

# In[1]:


import math
math.sqrt(16)


# In[2]:


math.ceil(27.20)


# In[3]:


math.exp(8)


# In[4]:


math.floor(27.20)


# In[7]:


math.trunc(27.80)


# In[8]:


#Built in methods
print(dir(math))


# In[ ]:




