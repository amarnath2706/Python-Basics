#!/usr/bin/env python
# coding: utf-8

# ## Files

# In[3]:


#Open the txt file
my_file=open('JA.txt')


# In[2]:


pwd


# ### Read operation

# In[4]:


#read the file
my_file.read()
#It returns the value in the form of single string


# In[12]:


type(my_file.read())


# In[5]:


#What happens when we try to read the file again
my_file.read()


# I opened the file and i already performed the read operation and now whenever i gng to perform the read operation the pointer will be available on the last stage.After last nothing to read.

# In[11]:


# I want to read my file from the first index or from 5 th index with the help of seek function
#seek(0) - reset the file read operation
#seek - used to read the data at any index location.
my_file.seek(0)


# In[9]:


my_file.read()


# In[14]:


my_file.seek(0)
#Readline
my_file.readline()


# In[15]:


type(my_file.readline())


# In[16]:


my_file.seek(0)


# In[17]:


#Readlines
my_file.readlines()
#it returns in the form of list


# In[18]:


type(my_file.readlines())


# ### Write operation

# In[19]:


#Add the second argument to the function,'W' which stands for write
#w - override
#w+ - append and write
#core python will support onlt txt file only not .csv excel file and all. 
my_file=open('JA.txt','w+')


# In[23]:


my_file.write('This is aaaaaa new line')


# In[24]:


my_file.seek(0)


# In[25]:


my_file.readlines()


# ### Iterating through a file

# In[26]:


get_ipython().run_cell_magic('writefile', 'JA.txt ', "#This operation equals to my_file.write('xxxxx')\nFirst line\nSecond line\nJA")


# In[28]:


for line in open('JA.txt'):
    print(line)


# ## String io

# In[29]:


#The StringIO module implements an in-memory file like object. it stores the data in volatile memory
from io import StringIO
message = "normal string"
#Use string IO method to set as file object
f=StringIO(message)
#read
f.read()


# In[ ]:


#Files are stored in permamnent memory - harddisk
#strings are stored in volatile memory - Ram

