#!/usr/bin/env python
# coding: utf-8

# ## Iterators
# for i in "amar":
#     print(i)
# * Here i can able to iterate over the string

# In[1]:


for i in "amar":
    print(i)


# In[2]:


next('amar')


# In[3]:


iter('amar')


# In[4]:


iter(5)


# * Suppose if i'm gng to pass an integer into iter function,then also we got an error, So why this things are happened, before    we getting solution for this, we need to know few things like
# 1) Iterator
# 2) Iterable
# 3) Generator
# 
# * This are the terms you supposed to understand
# 
# 1) Itrator - Iterator is basically an kind of an object,which you can make it as an iterable. 
# 2) Iterable - you will be able to extract the informations one by one are called as iterable object.
# 
# * Suppose if an object is an Iterable, only in that condition you will be able to make anyone as Iterator.
# * If object is not iterable in that case you won't be able to make anything as an iterator.
# * "amar" - Here the string is not an iterator but it is iterable, so whatever you findout is an iterable, some how you will be able to convert this object into a iterator and when an object is an iterator it leads to it will be able to extract the informations one by one out of it
# * Int is not an iterable which means that you  will not be able to makes this things as a iterator because it never contains indexes.
# * So string is an iterable object and you can make it as an iterator, where as int is not an iterable object and you can't make it as an iterator.
# * In forloop it takes the responsibility for making this particular thing as a iterator object, so that's a reason you are able to get the data one by one
# * Suppose instead of string i pass integer(5) over here in for loop in that case for sure it will raise an issue. it will not be able to iterate over to it.
# * list,string,range,tuple,set -- Iterable objects
# * Next function is a kind of iterator function and this function will be able to extract the information or dataset out of an iterable object.
# 

# In[5]:


a=iter('Jasvee')
next(a)


# In[6]:


next(a)


# In[7]:


next(a)


# * This are the two functions are implemented in for loop logic.

# ## Generators
# * Generator is a kind of object it will generate a new dataset.
# * range(5) - range(0,5) --> basically it gives you the range object but not the data's from 0 to 5
# * Suppose if i call the range function inside the list
# * list(range(5)) --- > you will be get an output like [0,1,2,3,4]
# * Basically the range function is behaving like a generators.It tries to generate the dataset for me.

# In[8]:


#Generator function for the cube of numbers(power of 3)
def gencube(n):
    for num in range(n):
        yield num**3
gencube(5)


# * Yield - Make the function as an generator. if i return the value of list for 10000 then it will occupy more memory and also more time to execute to overcome this or avoid such things i just mentioned yield.
# * Which means i want to create a function which can be a generator. so i want to create an object basically which will not give me a data unless or untill i dont want to extract the data
# * I just to want to create a such kind of object which will give me a data when i will try to extract the data out of it otherwise it will keep this things as an object.

# In[10]:


# Fibanocci
def fibfn(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b
fibfn(20)


# In[13]:


#Fibanocci normal method
def fib_fn(n):
    a=1
    b=1
    output=[]
    for i in range(n):
        output.append(a)
        #Swap operations
        a,b=b,a+b
    return output
fib_fn(27)


# In[ ]:




