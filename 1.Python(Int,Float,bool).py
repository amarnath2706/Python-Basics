#!/usr/bin/env python
# coding: utf-8

# # Basic Fundamental types - Primitive data types

# ## Integers

# In[1]:


x=6
print(x)


# In[2]:


# type function
type(x)


# In[3]:


# id function - it shows the memory address of the variable x.
id(x)


# ## Float- Numbers with decimal point

# In[4]:


x=20.06
print(x)


# In[5]:


type(x)


# ## Boolean - It gives the result whether the statement is True or False

# In[6]:


b1 = True
type(b1)


# ### 'And' operator with boolean conditions

# In[7]:


True and True


# In[8]:


True and False


# In[9]:


0 and 1


# In[10]:


False and False


# In[11]:


1 and 1


# In[12]:


0 and 0


# ### 'or' with bool

# In[13]:


True or False


# In[14]:


True or True


# In[15]:


False or False


# In[16]:


0 or 1


# In[18]:


1 or 1


# In[19]:


0 or 0


# In[53]:


True and True or False


# In[54]:


True and False or True


# In[55]:


True and False and False


# In[56]:


1 and 1 or 0


# ### 'Not' operator with bool

# In[20]:


not True


# In[21]:


not False


# In[25]:


not 1


# In[26]:


not 0


# ### 'is' operator with bool

# In[27]:


True is True


# In[28]:


True is False


# In[29]:


False is False


# In[30]:


0 is 0


# In[31]:


0 is 1


# In[32]:


1 is 1


# In[33]:


'a' is 'a'


# In[35]:


'Jasvee' is 'JASVEE'


# ### Arithmetic operations with bool

# In[36]:


True + True


# In[37]:


True + False


# In[38]:


False + False


# In[40]:


True - False


# In[43]:


(True*True)+(True*True)


# In[44]:


False-True


# In[45]:


False - False


# ### Equal to operator (==)

# In[46]:


'Jasvee'=='Jasvee'


# In[47]:


'Jasvee'=='JASVEE'


# In[48]:


20==20


# ### Not equal to operator(!=)

# In[49]:


'Jasvee'!='Jasvee'


# In[50]:


'Jasvee'!="JASVEE"


# In[51]:


20!=6


# ### <, > , <=, >=

# In[57]:


20<6


# In[58]:


6<20


# In[59]:


20>6


# In[60]:


6>20


# In[61]:


20<=6


# In[62]:


20<=20


# In[63]:


20>=6


# In[64]:


20>=27


# ### Bitwise left and right

# In[67]:


J=27
J>>2


# In[68]:


J<<2


# In[ ]:




