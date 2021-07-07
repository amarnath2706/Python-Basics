#!/usr/bin/env python
# coding: utf-8

# ## Functions
# Introduction to Functions
# What is a function in Python and how to create a function?
# 
# Functions will be one of our main building blocks when we construct larger and larger amount of code to solve problems.
# 
# So what is a function?
# 
# A function groups a set of statements together to run the statements more than once. It allows us to specify parameters that can serve as inputs to the functions.
# 
# Functions allow us to reuse the code instead of writing the code again and again. If you recall strings and lists, remember that len() function is used to find the length of a string. Since checking the length of a sequence is a common task, you would want to write a function that can do this repeatedly at command.
# 
# Function is one of the most basic levels of reusing code in Python, and it will also allow us to start thinking of program design.

# In[1]:


def name_of_function(arg1,arg2):
   '''
   This is where the function's Document String (doc-string) goes
   '''
   # Do stuff here
   #return desired result


# We begin with def then a space followed by the name of the function. Try to keep names relevant and simple as possible, for example, len() is a good name for a length() function. Also be careful with names, you wouldn't want to call a function the same name as a built-in function in Python (such as len).
# 
# Next, comes the number of arguments separated by a comma within a pair of parenthesis which acts as input to the defined function, reference them and the function definition with a colon.
# 
# Here comes the important step to indent to begin the code inside the defined functions properly. Also remember, Python makes use of whitespace to organize code and lot of other programming languages do not do this.
# 
# Next, you'll see the doc-string where you write the basic description of the function. Using iPython and iPython Notebooks, you'll be able to read these doc-strings by pressing Shift+Tab after a function name. It is not mandatory to include docstrings with simple functions, but it is a good practice to put them as this will help the programmers to easily understand the code you write.
# 
# After all this, you can begin writing the code you wish to execute.
# 
# The best way to learn functions is by going through examples. So let's try to analyze and understand examples that relate back to the various objects and data structures we learned.

# In[3]:


#Simple print hello function
def hello():
    print("Hello")
hello()


# In[4]:


def greet(name):
    print("Hello {}".format(name))
greet('Jasvee')


# In[6]:


def test():
    pass


# In[7]:


# return keyword is used to return the output to the user
def test1():
    return 'Jasvee'
test1()


# In[9]:


type(test1())


# In[12]:


def addfn(x1,x2):
    return x1+x2
addfn(20,6)


# In[14]:


# Can also save as variable due to return
result = addfn(4,5)
print(result)


# In[15]:


def testfn(a,b):
    return a+b
testfn("Adithri",str(20))


# In[20]:


# To fin min value
l=[1,2,3,4,5,6,7,9,10]
def minfn(l):
    return min(l)
minfn(l)


# In[21]:


#Function to convert list to set
def tosetfn(a,b):
    return set(a+b)
tosetfn([1,1,2,3,4,4,5,5,5,6],[8,8,8,8,9,10,10,20,6,27,18,25,4])


# In[22]:


def test5(a,b):
    return set(a+b),a+b
x,y=test5([1,1,2,3,4,5],[10,11,12])
x


# In[23]:


y


# In[25]:


def test6(a,b):
    if a==0:
        return True
    elif a==6:
        return False
    else:
        print('no idea')
    return set(a+b),a+b
x,y=test6([1,1,1,3,3,3],[101,10])
x


# In[26]:


y


# In[27]:


#Type safety
def test7(a,b):
    if type(a) == int:
        return a


# In[29]:


#default or optional parameter
def test8(a,b,c=4):
    return a+b+c
test8(20,6)
#now i override the c values too
test8(20,6,27)


# In[31]:


#Prime no
def isprime_no(num):
    for n in range(2,num):
        if num%n==0:
            print("not prime")
            break
    else:
        print('Prime')
isprime_no(16)


# In[ ]:




