#!/usr/bin/env python
# coding: utf-8

# ## Map, Reduce, Filter and Lambda

# In[1]:


def fah(T):
    return((float(9)/5)*T+32)
def cel(T):
    return(float(5)/9)*(T-32)
cel(45)


# Now i have a requirement to convert the above items from the list into celcius or farenheit.

# In[2]:


temp=[0,22.5,40,100]
l=[]
for i in temp:
    l.append(fah(i))
l


# ### Map
# 
# In a simple way we can do that also with the help of Map function.
# 
# * The map() is a function that takes in two arguments:
# 
# 1) A function 
# 2) A sequence iterable.
# 
# In the form: map(function, sequence)
# 
# * The first argument is the name of a function and the second a sequence (e.g. a list). map() applies the function to all the elements of the sequence. It returns a new list with the elements changed by the function.
# 
# * When we went over list comprehension we created a small expression to convert Fahrenheit to Celsius. Let's do the same here but use map.

# In[3]:


F_temp=list(map(fah,temp)) # Here fah is a function and temp is a collection(list)
F_temp


# In[4]:


F_cel=list(map(cel,temp))
F_cel


# In[5]:


#Convert back
list(map(cel,F_temp))


# In[6]:


#Dictionary and set are not an iterable


# ### Lambda function
# 

# * The lambda function is also called as ad-hoc function (or) Anonymous function. instead of writting a huge function i can go for lambda function which means i can create a function without any function name.

# In[8]:


list(map(lambda x:(5.0/9)*(x-32),F_temp))


# In[9]:


a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=[11,12,13,14,15]
list(map(lambda x,y:x+y,a,b))


# In[11]:


list(map(lambda x,y,z:x+y+z,a,b,c))


# ### Reduce function

# * Whenever you looking for an aggregation operation or sum kind of an summation operation or concatenation operation,where you have an entire range of the list then eventually you will get a single dataset as a output. In that case you can call reduce function.
# 

# In[12]:


from functools import reduce
lst=[47,11,42,16]
reduce(lambda x,y:x+y,lst)


# * The function reduce(function, sequence) continually applies the function to the sequence. It then returns a single value.
# 
# * If seq = [s1, s2, s3, ... , sn], calling reduce(function, sequence) works like this:
# 
# * At first the first two elements of sequence will be applied to function, i.e. func(s1,s2)
# * The list on which reduce() works looks like this: [ function(s1, s2), s3, ... , sn ]
# * In the next step the function will be applied on the previous result and the third element of the list, i.e.   function(function(s1, s2),s3)
# * The list looks like: [ function(function(s1, s2),s3), ... , sn ]
# * It continues like this until just one element is left and return this element as the result of reduce()

# In[14]:


#from IPython.display import Image
#Image('http://www.python-course.eu/images/reduce_diagram.png')


# In[15]:


#Find the maximum of a sequence (This already exists as max())
max_find = lambda a,b: a if (a > b) else b


# In[16]:


reduce(max_find,lst)


# ### Filter function
# The Flter function always gives you the dataset which means filterout the dataset based on the conditions True or False . If True it will gives you the data. If False it won't give any datas.
# 

# The function filter(function, list) offers a convenient way to filter out all the elements of an iterable, for which the function returns "True".
# 
# The function filter(function(),l) needs a function as its first argument. The function needs to return a Boolean value (either True or False). This function will be applied to every element of the iterable. Only if the function returns "True" will the element of the iterable be included in the result.

# In[17]:


#First let's make a function
def even_check(num):
    if num%2 ==0:
        return True
even_check(20)


# In[18]:


lst=range(20)
list(filter(even_check,lst))


# In[19]:


tup=tuple(range(10))
tuple(filter(even_check,tup))


# ### Lambda with Filter function
# Filter is most commonly used with lambda functions

# In[21]:


list(filter(lambda x:x%2==0,lst))


# In[ ]:




