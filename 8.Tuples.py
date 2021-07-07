#!/usr/bin/env python
# coding: utf-8

# ## Tuples
# In Python, tuples are similar to lists but they are immutable i.e. they cannot be changed. You would use the tuples to present data that shouldn't be changed, such as days of week or dates on a calendar.

# In[1]:


tup = (1,20.6,'Jasvee',True,['amar',27])
tup


# In[9]:


t1=tuple('arj')
t1


# In[2]:


len(tup)


# In[3]:


type(tup)


# In[4]:


#Indexing and slicing
tup[4][1]


# In[5]:


tup[3]


# In[6]:


tup[::-1]


# ### Tuple function 
# Tuple having only two functions
# 1. Index
# 2. Count

# In[7]:


tup.index('Jasvee')


# In[8]:


tup.count('e')


# In[ ]:




