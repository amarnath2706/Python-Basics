#!/usr/bin/env python
# coding: utf-8

# ## Range function 
# 
# We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).
# 
# We can also define the start, stop and step size as range(start,stop,step size). step size defaults to 1 if not provided.
# 
# This function does not store all the values in memory, it would be inefficient. So it remembers the start, stop, step size and generates the next number on the go.
# 
# To force this function to output all the items, we can use the function list().
# 
# The following example will clarify this.

# In[1]:


print(range(10))


# In[2]:


print(list(range(10)))


# In[3]:


print(list(range(2, 8)))


# In[4]:


print(list(range(2, 20, 5)))


# In[6]:


print(list(range(8,2,1)))


# In[7]:


print(list(range(8,2,-1)))


# We can use the range() function in for loops to iterate through a sequence of numbers. It can be combined with the len() function to iterate though a sequence using indexing. Here is an example.

# In[8]:


# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz','sapna']

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[0:2])


# In[9]:


# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz','sapna']

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])


# In[ ]:




