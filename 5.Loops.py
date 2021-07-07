#!/usr/bin/env python
# coding: utf-8

# In[1]:


st="Hello world"
m=""
for i in st:
    m=i+m
    print(m)


# In[2]:


st="Hello world"
m=""
for i in st:
    m=m+i
    print(m)


# In[3]:


#Reverse the string
st="Hello world"
m=""
for i in st:
    m=i+m
print(m)


# In[12]:


s="Hello Jasvee Adithri"
m=""
for i in s.split():
    m=m+i
print(m)


# In[28]:


genre=['Pop','Rock','Jazz']
len(genre)
for i in genre:
    print("I like :" ,i) 


# In[32]:


#for i in list(range(len(genre)-1,0,-1)):
genre=['A',"A",'Amar','A']
count=0
for i in genre:
    if i == 'Amar':
        count=count + 1
print(count)


# In[4]:


#Program to find the sum of all numbers stored in a list
numbers = [6, 5, 3, 8, 4, 2, 5, 4,9]
sum=0
for i in numbers:
    sum = sum+i

print("Total sum : {}".format(sum))


# ### For else

# In[11]:


digits = [1,2,3,4,5]
for i in digits:
    print(i,end=' ')
else:
    print("No items left")


# ### While loop
# 
# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
# 
# We generally use this loop when we don't know beforehand, the number of times to iterate.
# 
# In while loop, test expression is checked first. The body of the loop is entered only if the test_expression evaluates to True. After one iteration, the test expression is checked again. This process continues until the test_expression evaluates to False.
# 
# In Python, the body of the while loop is determined through indentation.
# 
# Body starts with indentation and the first unindented line marks the end.
# 
# Python interprets any non-zero value as True. None and 0 are interpreted as False.

# In[8]:


user_val=int(input("Enter no : "))
sum=0
i=1
while i<=user_val:
    sum = sum + i
    i = i+1
print("Total sum : {}".format(sum))


# In[ ]:





# In[ ]:




