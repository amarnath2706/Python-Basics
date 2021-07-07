#!/usr/bin/env python
# coding: utf-8

# ## Dictionaries
# We have learned about "Sequences" in the previous session. Now, let's switch the gears and learn about "mappings" in Python. These dictionaries are nothing but hash tables in other programming languages.
# 
# In this section, we will learn briefly about an introduction to dictionaries and what it consists of:
# 
# 1.) Constructing a Dictionary
# 2.) Accessing objects from a Dictionary
# 3.) Nesting Dictionaries
# 4.) Basic Dictionary Methods
# Before we dive deep into this concept, let's understand what are Mappings?
# 
# Mappings are a collection of objects that are stored by a "key". Unlike a sequence, mapping store objects by their relative position. This is an important distinction since mappings won't retain the order since they have objects defined by a key.
# 
# A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.

# In[1]:


#Constructing a dictionary
my_dict={'key1':'value1','key2':'value2'}
my_dict


# In[2]:


type(my_dict)


# In[3]:


len(my_dict)


# In[4]:


my_dict['key2']


# In[5]:


my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
my_dict['key3']


# In[6]:


my_dict['key3'][0]


# In[7]:


my_dict['key3'][0].upper()


# In[8]:


# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123


# In[9]:


my_dict['key1']


# In[10]:


# Create a new dictionary
d = {}


# In[11]:


# Create a new key through assignment
d['animal'] = 'Dog'


# In[12]:


# Can do this with any object
d['answer'] = 42


# In[13]:


#Show
d


# ### Nesting Dictionaries

# In[14]:


# Dictionary nested inside a dictionary nested in side a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}


# In[15]:


# Keep calling the keys
d['key1']['nestkey']['subnestkey']


# ### Dictionary methods

# In[16]:


# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}


# In[17]:


# Method to return a list of all keys 
d.keys()


# In[18]:


# Method to grab all values
d.values()


# In[19]:


# Method to return tuples of all items  (we'll learn about tuples soon)
d.items()


# ### Dictionary comprehension
# 

# In[21]:


{x:x**2 for x in range(10)}


# In[22]:


{x:x/5 for x in range(20)}


# In[23]:


{x:4 for x in range(10)}


# In[ ]:




