#!/usr/bin/env python
# coding: utf-8

# ## Break and Continue
# 
# In Python, break and continue statements can alter the flow of a normal loop.
# 
# Loops iterate over a block of code until test expression is false, but sometimes we wish to terminate the current iteration or even the whole loop without cheking test expression.
# 
# The break and continue statements are used in these cases.
# 
# break
# The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.
# 
# If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.
# 
# 

# In[7]:


st = "Jasvee Adithri"
for i in st:
    if i == 'r':
        break
    print(i,end='')
print("\nEnd")


# ### Continue
# The continue statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.

# In[8]:


for i in st:
    if i == 'e':
        continue
    print(i,end='')
print("\nEnd")


# In[10]:


#Swap first and last letter
str = 'Jasvee'
a=str[0]
b=str[len(str)-1]
nw_st=b+str[1:len(str)-1]+a
nw_st


# In[11]:


print("Jasvee's")


# In[ ]:




